# Chalkboard - CTF Challenge Writeup

Challenge: Chalkboard
Points: 30
Category: Forensics

## Objective
The objective of the Chalkboard challenge is to learn about image metadata and decode a flag hidden within it. Your task is to uncover the hidden flag by inspecting the metadata of the image.

## Solution
To successfully complete this challenge, follow these steps:

1. **Metadata Inspection**: Start by using a tool like `exiftool` to inspect the metadata of the provided image. Metadata contains information about the image, and sometimes it can hide secrets.

2. **Flag Discovery**: After examining the metadata, you will find the flag; however, it is encoded. 

3. **Mathematical Equation**: The challenge instructions suggest that you should follow a mathematical equation to decode the flag.

4. **Flag Decoding**: Apply the mathematical operations as instructed to decode the flag.

5. The flag format is `CTFlearn{XXXXXXXXXX}`, where `XXXXXXXXXX` represents the actual flag you derive from the mathematical operations.

## Flag
The flag for this challenge is in the format: `CTFlearn{XXXXXXXXXX}`.

Enjoy your exploration of image metadata and decoding, and happy hacking!
