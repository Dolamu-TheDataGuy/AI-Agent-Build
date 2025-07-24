import os

def get_file_content(working_directory, file_path):

    working_dir = os.path.abspath(working_directory)
    target_dir = working_directory
    
    if file_path:
        target_dir = os.path.abspath(os.path.join(working_dir, file_path))
        
    if not target_dir.startswith(working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(target_dir):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    MAX_CHARS = 10000
            
    try:
        with open(target_dir, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            check_more = f.read(1)
            if file_content_string and len(check_more) > 0:
                return file_content_string + '[...File "{file_path}" truncated at 10000 characters]'
            return file_content_string
    except Exception as e:
        return f"Error: {str(e)}"