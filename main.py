import os
import sys
import json
import argparse
from dotenv import load_dotenv
from openai import OpenAI
from prompt import system_prompt
from call_functions import available_functions, call_function
from functions.config import MAX_ITERS




def main()->None:
    parser = argparse.ArgumentParser(description="AI Code Assistant")
    parser.add_argument("user_prompt", type=str, help="Prompt to send to the LLM")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if api_key is None:
        raise RuntimeError(
        "OPENROUTER_API_KEY is not set in the environment variables. Please set it in the .env file."
    )
    
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": args.user_prompt}
    ]
    
    if args.verbose:
        print(f"User prompt: {args.user_prompt}\n")
    
    for _ in range(MAX_ITERS):
        try:
            final_response = generate_content(client, messages, args.verbose)
            if final_response:
                print("Final response:")
                print(final_response)
                return
        except Exception as e:
            print(f"Error in generate_content: {e}")
            
    print(f"Maximum iterations ({MAX_ITERS}) reached")
    sys.exit(1)
    
    

def generate_content(client:OpenAI, messages:list, verbose:bool)->str | None:
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        tools=available_functions,
        temperature=0
    )
    
    if not response.usage:
        raise RuntimeError("usage property is none, please try again")
    
    
    if verbose:
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")

    message = response.choices[0].message
    messages.append(message)
    
    # read the content of message variable in a json file.
    with open("response.json", "w") as f:
        json.dump(message.model_dump(), f, indent=4)
    
    print("checking message_tool_calls content:")    
    print(message.tool_calls)
    
    # if there are no tool calls, return the content of the message, this finally end the loop in main()
    if not message.tool_calls:
        return message.content
    
    for tool_call in message.tool_calls:
        result_message = call_function(tool_call, verbose)
        if not result_message["content"]:
            raise Exception("content is empty.")
        if verbose:
            print(f"-> {result_message['content']}")
        messages.append(result_message)
    
    return None

    
if __name__ == "__main__":
    main()
