# Simple Steganography - CTF Challenge Writeup

Challenge: Simple Steganography
Points: 30
Category: Forensics

## Objective
The "Simple Steganography" challenge falls under the Forensics category and aims to teach participants how to use ```steghide```, a tool commonly employed in steganography. Steganography is the practice of concealing data within another file. In this challenge, the objective is to extract hidden information from an image using steghide.

## Solution
To complete this challenge, you need to utilize steghide and follow these steps:

1. **Download the Image**: Begin by downloading the image provided in the challenge. This image contains hidden information.

2. **Use Steghide**: Like the challenge suggested, use ```steghide```. But you may notice it requires a passphrase or password. This can often be found using another popular tool for forensics, ```exiftool```.

3. **Exiftool**: Look for any password or hint within the image's metadata, specifically in the ```keywords``` column. This password will be required for extracting the hidden content.

4. **Use Steghide**: With the extracted password, employ the steghide tool to extract the hidden information. The tool should be used with the password to access the concealed data within the image.

5. **Flag Extraction**: The extracted information should contain the flag.

The flag for this challenge is in the format: `CTFlearn{XXXXXXXXXX}`, where `XXXXXXXXXX` represents the actual flag that you obtain after using steghide to uncover the hidden data.

## Flag
The flag for this challenge is: `CTFlearn{XXXXXXXXXX}`.

By completing this challenge, you've gained experience in steganography and using tools like steghide to reveal hidden content within images. Great work!
