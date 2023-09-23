# Character Encoding

## Basic Information
- **Category**: Cryptography
- **Difficulty**: Easy
- **Points**: 20

## Solving
The objective of this challenge is to familiarize yourself with ASCII encoding.

**Method 1: Using an Online Tool**
- You can use online hexadecimal to ASCII converters such as [RapidTables](https://www.rapidtables.com/convert/number/hex-to-ascii.html).

**Method 2: Using a Python Script**
- Alternatively, you can use the following Python script to convert the hexadecimal values to ASCII:
```python
#!/usr/bin/python3

import binascii

def main():
    flag = []
    hexadecimal = "41 42 43 54 46 7B 34 35 43 31 31 5F 31 35 5F 55 35 33 46 55 4C 7D".split(" ")
    for char in hexadecimal:
        flag.append(bytes.fromhex(char).decode("utf-8"))

    print(''.join(flag))

main()
```
**Solved**
