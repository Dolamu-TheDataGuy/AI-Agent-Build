from functions.get_files_info import get_files_info

if __name__ == "__main__":
    print("Result for current directory:")
    result1 = get_files_info("calculator", ".")
    print(result1)

    print("\nResult for 'pkg' directory:")
    result2 = get_files_info("calculator", "pkg")
    print(result2)

    print("\nResult for '/bin' directory:")
    result3 = get_files_info("calculator", "/bin")
    print(result3)

    print("\nResult for '../' directory:")
    result3 = get_files_info("calculator", "../")
    print(result3)
