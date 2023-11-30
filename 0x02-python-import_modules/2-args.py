#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    argc = len(argv)

    print("{} argument{}{}".format(argc - 1, 's' if argc != 2 else '', ':' if argc > 1 else '.'))

    for i in range(1, argc):
        print("{}: {}".format(i, argv[i]))
