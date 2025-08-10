from google.genai import types

from functions.get_files_info import schema_get_files_info, get_files_info
from functions.write_files import schema_write_file, write_file
from functions.run_python import schema_run_python_file, run_python_file
from functions.get_file_content import schema_get_file_content, get_file_content
from functions.config import WORKING_DIRECTORY


available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info, schema_write_file, schema_run_python_file, schema_get_file_content
    ]
)

def call_function(function_call_part, verbose=False):
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    func_dict = {
        "get_files_info": get_files_info,
        "write_file": write_file,
        "run_python_file": run_python_file,
        "get_file_content": get_file_content,
        }

    if function_call_part.name in func_dict:
        function_name = func_dict[function_call_part.name]
        args = function_call_part.args
        args["working_directory"] = WORKING_DIRECTORY

        function_response = function_name(**args)
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"result": function_response},
                )
            ],
        )
    else:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"error": f"Unknown function: {function_call_part.name}"},
                )
            ],
        )
