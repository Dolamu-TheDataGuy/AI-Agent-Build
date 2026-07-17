# import os
# import sys
# from dotenv import load_dotenv
# from google import genai
# from google.genai import types

# from prompt import system_prompt
# from call_functions import available_functions, call_function

# def main():
#     load_dotenv()

#     args = sys.argv[1:]
#     # print(args)

#     if not args:
#         print("AI Code Assistant")
#         print('\nUsage: python main.py "your prompt here"')
#         print('Example: python main.py "How do I build a calculator app?"')
#         sys.exit(1)

#     verbose = "--verbose" in args

#     user_prompt = args[0]

#     api_key = os.environ.get("GEMINI_API_KEY")

#     client = genai.Client(api_key=api_key)

#     messages = [
#         types.Content(role="user", parts=[types.Part(text=user_prompt)]),

#     ]


#     for step in range(20):
#         try:
#             result = generate_content(client, messages, verbose)

#             if result is not None:
#                 print("Final response")
#                 print(result)
#                 break
#         except Exception as e:
#             print(f"Error in generate_content: {e}")


# # function that generate content via LLM calls
# def generate_content(client, messages, verbose):
#     # The LLM call
#     response = client.models.generate_content(
#         model="gemini-2.0-flash-001",
#         contents=messages,
#         config=types.GenerateContentConfig(
#             tools=[available_functions], system_instruction=system_prompt
#         ),
#     )

#     if response.candidates:
#         for candidate in response.candidates:
#             messages.append(candidate.content)

#     # print tokens if the verbose flag is set in arguments --> uv run main.py --verbose "your prompt here"
#     if verbose:
#         print("Prompt tokens:", response.usage_metadata.prompt_token_count)
#         print("Response tokens:", response.usage_metadata.candidates_token_count)

#     # check if the response has function calls
#     if not response.function_calls:
#         return response.text

#     # Handles function calls ---> "run_python_file", "get_files_info",
#     function_responses = []
#     for function_call_part in response.function_calls:
#         function_call_result = call_function(function_call_part, verbose)

#         if (not function_call_result.parts or not function_call_result.parts[0].function_response):
#             raise Exception("empty function call result")
#         if verbose:
#             print(f"-> {function_call_result.parts[0].function_response.response}")
#         function_responses.append(function_call_result.parts[0])


#     if not function_responses:
#         raise Exception("no function responses generated, exiting.")

#     messages.append(types.Content(role="user", parts=function_responses))
#     return None

import os
import argparse
from dotenv import load_dotenv
from openai import OpenAI
from prompt import system_prompt




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
    
    generate_content(client, messages, args.verbose)
    

def generate_content(client:OpenAI, messages:list, verbose:bool)->None:
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        temperature=0
    )
    
    if not response.usage:
        raise RuntimeError("usage property is none, please try again")
    
    
    if verbose:
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")
    print("Response:")
    print(response.choices[0].message.content)
    
    
if __name__ == "__main__":
    main()
