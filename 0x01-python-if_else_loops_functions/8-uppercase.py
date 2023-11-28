def uppercase(s):
    for char in s:
        if 97 <= ord(char) <= 122:  # Check if the character is lowercase
            print("{:c}".format(ord(char) - 32), end='')
        else:
            print("{:c}".format(ord(char)), end='')

    print()  # Print a new line after the loop

# Example usage:
uppercase("Hello, World!")

