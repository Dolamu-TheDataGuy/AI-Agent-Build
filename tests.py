from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

if __name__ == "__main__":
    print("\nResult for 'pkg' directory:")
    result2 = get_file_content("calculator", "main.py")
    print(result2)

    print("\nResult for '/bin' directory:")
    result3 = get_file_content("calculator", "pkg/calculator.py")
    print(result3)

    print("\nResult for '../' directory:")
    result4 = get_file_content("calculator", "/bin/cat")
    print(result4)

    print("\nResult for '../' directory:")
    result5 = get_file_content("calculator", "pkg/does_not_exist.py")
    print(result5)
    