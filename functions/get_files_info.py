import os
from google.genai import types

def get_files_info(working_directory: str, directory:str=None):
    # if directory is None:
    #     directory = '.'

    # working_dir = os.path.abspath(working_directory)
    # target_dir = os.path.abspath(os.path.join(working_directory, directory))
    try:
        working_dir = os.path.abspath(working_directory)
        target_dir = working_directory

        if directory:
            target_dir = os.path.normpath(os.path.join(working_dir, directory))
            print(target_dir)

        if not target_dir.startswith(working_dir):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'

    
        full_path_contents = os.listdir(target_dir)

        str = ""
        for content in full_path_contents:
            str += f"- {content}: file_size={os.path.getsize(os.path.join(target_dir,content))} bytes, is_dir={os.path.isdir(os.path.join(target_dir,content))}\n"
        return str.strip()

    except Exception as e:
        return f"Error listing files: {str(e)}"


schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "List files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                }
            }
        }
    }
}
