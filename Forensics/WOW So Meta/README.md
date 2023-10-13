# WOW... So Meta - CTF Challenge Writeup

Challenge: WOW... So Meta
Points: 20
Category: Forensics

## Objective
The objective of the WOW... So Meta challenge is to learn the basics of digital forensics and steganography, specifically focusing on metadata extraction. Your task is to uncover hidden information within the metadata of a file.

## Solution
To successfully complete this challenge, follow these steps:

1. **Understanding Metadata**: As suggested by the challenge name, this is a metadata-based challenge. Metadata refers to data about data and is often found in various file types, including images.

2. **Exiftool Usage**: Start your investigation by using a tool like `exiftool` to extract metadata information from the provided file. `Exiftool` is a commonly used utility to extract metadata details.

3. Your initial step in any metadata challenge is to use `exiftool` to explore the metadata.

4. **Flag Discovery**: Once you've used `exiftool` to examine the metadata, you'll discover the flag hidden within it. Copy the flag, and you've successfully completed the challenge.

5. The flag format is `flag{XXXXXXXXXX}`, with `XXXXXXXXXX` being the actual flag you find within the metadata.

## Flag
The flag for this challenge is in the format: `flag{XXXXXXXXXX}`.

Enjoy your exploration of metadata extraction in forensics, and happy hacking!
