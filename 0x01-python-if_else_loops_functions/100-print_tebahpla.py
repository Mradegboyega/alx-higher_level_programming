#!/usr/bin/python3

for i in range(ord('z'), ord('a') - 1, -1):
    print("{:c}".format(i), end="")
    if i % 2 == 0:
        print("{:c}".format(i - 32), end="")
print()

