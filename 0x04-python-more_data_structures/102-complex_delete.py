def complex_delete(a_dictionary, value):
    # Use a dictionary comprehension to create a new dictionary with desired keys
    return {key: val for key, val in a_dictionary.items() if val != value}
