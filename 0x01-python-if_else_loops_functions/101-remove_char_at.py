def remove_char_at(s, n):
    # Check if the index is valid
    if 0 <= n < len(s):
        # Use string slicing to create a new string without the character at position n
        return s[:n] + s[n+1:]
    else:
        # If the index is invalid, return the original string
        return s
