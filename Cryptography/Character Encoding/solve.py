#!/usr/bin/python3

import binascii

def main():
    flag = []
    hexadecimal = "41 42 43 54 46 7B 34 35 43 31 31 5F 31 35 5F 55 35 33 46 55 4C 7D".split(" ")
    for char in hexadecimal:
        flag.append(bytes.fromhex(char).decode("utf-8"))

    print(''.join(flag))

main()
