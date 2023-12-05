# CTF Challenge Writeup
**Name:** So Many 64s
**Points:** 80
**Category:** Cryptography

## Objective

The objective of the "So Many 64s" challenge is to decode a flag that has been repeatedly encoded in Base64 format multiple times. The flag is hidden behind multiple layers of Base64 encoding, and the goal is to reveal the correct flag.

## Solution

This challenge can be solved by repeatedly decoding the flag using Base64 until the original flag is revealed. Two approaches to solve it are presented below:

1. **Using CyberChef**
   - One way to tackle this challenge is by utilizing online tools such as CyberChef, which allows you to create data transformation recipes.
   - In CyberChef, you can stack multiple Base64 decode blocks.
   - After applying this sequence of decodes, the hidden flag will be revealed.

2. **Using Python Script**
   - Alternatively, you can solve this challenge programmatically using a Python script.
   - The script reads the encoded flag from a file (in this case, "flag.txt") and decodes it repeatedly using a loop.
   - The result is printed out to reveal the flag.

Here's the Python script used to solve the challenge:

```python
import base64 

with open("flag.txt", "r") as file:
    encoded_flag = file.read()

    for i in range(32):
        encoded_flag = base64.b64decode(encoded_flag).decode()

    print(encoded_flag)
```

# Flag

The flag for the "So Many 64s" challenge is `ABCTF{XXXXXXXXXX}`. It was hidden behind multiple layers of Base64 encoding, and by decoding it multiple times, the original flag was successfully revealed.

This challenge emphasizes the importance of understanding encoding and decoding techniques, as well as the iterative application of transformations to reveal concealed information.
