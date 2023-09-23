# Base 2 2 the 6

## Basic Information
- **Category**: Cryptography
- **Difficulty**: Easy
- **Points**: 20

## Solving
The objective of this challenge is to familiarize yourself with BASE64 encoding.

**Method 1: Using Online Tools**
- To decode the BASE64-encoded flag, you can use online tools such as [CyberChef](https://cyberchef.org/) or [dcode](https://www.dcode.fr/en).

**Method 2: Using a Python Script**
- Alternatively, you can use a Python script to decode the flag:
```python
#!/usr/bin/python3

import base64

def main():
    hexadecimal = "Q1RGe0ZsYWdneVdhZ2d5UmFnZ3l9"
    print(base64.b64decode(hexadecimal).decode())

main()
```
**Copy and Paste the Flag**

This challenge provides an opportunity to practice decoding BASE64-encoded messages, a fundamental skill in cryptography and cybersecurity.

**Challenge Completed**
