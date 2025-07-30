import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_dir):
        return f"Error: Cannot execute {file_path} as it is outside the permitted working directory"

    if not os.path.exists(abs_file_path):
        return f"Error: {file_path} not found"

    if not abs_file_path.endswith(".py"):
        f'Error: "{file_path}" is not a Python file.'

    try:
        # if args:
        #     result = subprocess.run(["python3", abs_file_path, *args], check=True, timeout=30, cwd=abs_working_dir)
        # else:
        #     result = subprocess.run(["python3", abs_file_path], check=True, timeout=30, cwd=abs_working_dir)

        command = ["python3", abs_file_path, *args] if args else ["python3", abs_file_path]
        
        result = subprocess.run(command, check=True, timeout=30, cwd=abs_working_dir)

        print(f"STDOUT = {result.stdout}")
        print(f"STDERR = {result.stderr}")

        if result.returncode != 0:
            return f"Error: Python script exited with code {result.returncode}"

        if not result.stdout:
            return "No output produced"

    except Exception as e:
        return f"Error: {str(e)}"
