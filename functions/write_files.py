import os
from google.genai import types

def write_file(working_directory: str, file_path: str, content: str) -> str:
    
    try:
        absolute_working_dir = os.path.abspath(working_directory)
        absolute_file_path = os.path.abspath(os.path.join(working_directory, file_path))
        
    
        # Check if file path is within the working directory
        if not absolute_file_path.startswith(absolute_working_dir):
            return f'Error: Cannot write to {file_path} as it is outside the permitted working directory'


        # check if filepath points to an existing directory
        if os.path.isdir(absolute_file_path):
            return f"Error: Cannot write to {file_path} as it is a directory, not a file"
        os.makedirs(os.path.dirname(absolute_file_path), exist_ok=True)
        
        
        # create file and write into file
        with open(absolute_file_path, "w") as f:
            f.write(content)
            return (f'Successfully wrote to "{file_path}" ({len(content)} characters written)')
    
    except Exception as e:
        return f"Error: writing to file {str(e)}"


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a file within the working directory. Creates the file if it doesn't exist.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write to the file",
            ),
        },
        required=["file_path", "content"],
    ),
)
