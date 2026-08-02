from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

if __name__ == "__main__":
    result1 = run_python_file("calculator", "main.py")
    print(result1)
    result2 = run_python_file("calculator", "main.py", ["3 + 5"])
    print(result2)
    result3 = run_python_file("calculator", "tests.py")
    print(result3)
    result4 = run_python_file("calculator", "../main.py")
    print(result4)
    result5 = run_python_file("calculator", "nonexistent.py")
    print(result5)
