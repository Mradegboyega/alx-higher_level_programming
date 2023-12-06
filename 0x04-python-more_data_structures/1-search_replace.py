#!/usr/bin/python3

def search_replace(my_list, search, replace):
    # Create a new list to store the modified elements
    result_list = []

    # Iterate through each element in the original list
    for item in my_list:
        # If the element is equal to the 'search' value, replace it with 'replace'
        if item == search:
            result_list.append(replace)
        else:
            result_list.append(item)

    return result_list
