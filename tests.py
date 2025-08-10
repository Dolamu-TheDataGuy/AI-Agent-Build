from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_files import write_file
from functions.run_python import run_python_file

if __name__ == "__main__":
    # print("\nResult for 'pkg' directory:")
    # result2 = get_file_content("calculator", "main.py")
    # print(result2)

    # print("\nResult for '/bin' directory:")
    # result3 = get_file_content("calculator", "pkg/calculator.py")
    # print(result3)

    # print("\nResult for '../' directory:")
    # result4 = get_file_content("calculator", "/bin/cat")
    # print(result4)

    # print("\nResult for '../' directory:")
    # result5 = get_file_content("calculator", "pkg/does_not_exist.py")
    # print(result5)

    # result1 = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    # print(result1)
    # result2 = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    # print(result2)
    # result3 = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    # print(result3)

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
