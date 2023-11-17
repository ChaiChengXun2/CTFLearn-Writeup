# Forensics 101 - CTF Challenge Writeup

Challenge: Forensics 101
Points: 30
Category: Forensics

## Objective
The objective of the Forensics 101 challenge is to learn about the basics of digital forensics, particularly focusing on steganography. Your task is to uncover hidden information within a given image.

## Solution
To successfully complete this challenge, follow these steps:

1. **Understanding Forensics**: This challenge falls under the category of forensics, where you explore metadata and concealed data within data.

2. **Metadata Examination**: To investigate metadata within an image, you can use the `exiftool` tool. Exiftool is commonly used to extract metadata information from various file types.

3. However, in this case, using Exiftool will not directly reveal the flag.

4. **Strings Analysis**: To uncover hidden information, a common tool used in basic forensics challenges is `strings`. The `strings` command is used to extract readable text from binary data.

5. Running `strings` on the provided image may reveal the hidden flag.

6. The flag format is `flag{XXXXXXXXXX}`, where `XXXXXXXXXX` is the actual flag you discover using the `strings` command.

## Flag
The flag for this challenge is in the format: `flag{XXXXXXXXXX}`.

Enjoy your journey into the basics of forensics and steganography, and happy hacking!
