#!/usr/bin/python3

import base64

def main():
    hexadecimal = "Q1RGe0ZsYWdneVdhZ2d5UmFnZ3l9"
    print(base64.b64decode(hexadecimal).decode())

main()
