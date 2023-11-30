def magic_calculation(a, b):
    if a < b:
        add = __import__('magic_calculation_102', fromlist=['add']).add
        sub = __import__('magic_calculation_102', fromlist=['sub']).sub

        c = add(a, b)

        for i in range(4, 6):
            c = add(c, i)

        return c
    else:
        return __import__('magic_calculation_102', fromlist=['sub']).sub(a, b)
