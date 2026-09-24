def is_palindrome(value):
    value = value.lower()
    return value == value[::-1]


def main():
    value = input("Enter a word or number: ")

    if is_palindrome(value):
        print(f"{value} is a palindrome.")
    else:
        print(f"{value} is not a palindrome.")


if __name__ == "__main__":
    main()
