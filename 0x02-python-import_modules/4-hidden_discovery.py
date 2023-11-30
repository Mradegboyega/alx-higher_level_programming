#!/usr/bin/python3.8
import dis
import sys
import marshal

def print_names(filename):
    try:
        with open(filename, 'rb') as file:
            code = marshal.load(file)

            # Extract names that do not start with '__'
            names = [name for name in code.co_names if not name.startswith('__')]

            # Print names in alphabetical order
            for name in sorted(names):
                print(name)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./4-hidden_discovery.py <hidden_4.pyc>")
        sys.exit(1)

    filename = sys.argv[1]
    print_names(filename)
