def print_last_digit(number):
    last_digit = abs(number) % 10
    print(last_digit, end='')
    return last_digit

# Example usage:
result = print_last_digit(-123)
print(f"\nResult: {result}")
