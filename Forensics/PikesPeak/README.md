# PikesPeak - CTF Challenge Writeup

Challenge: PikesPeak
Points: 20
Category: Forensics

## Objective
The objective of the PikesPeak challenge is to uncover hidden information within an image. Your task is to use forensic techniques to extract the flag hidden within the image.

## Solution
To successfully complete the PikesPeak challenge, follow these steps:

1. **Using Strings on the Image**: Start by using the `strings` command on the image. This command extracts sequences of printable characters from a binary file. In many forensics challenges, important information, including flags, is hidden within these character sequences.

2. **Search for the Flag**: To narrow down your search, focus on finding the flag. You can use the `grep` command to search for the term "ctf" within the strings extracted from the image. The `-i` option makes the search case-insensitive, ensuring that you don't miss the flag even if the capitalization differs.

  - ```strings <image> | grep -i "ctf"```

3. The flag for this challenge is in the format `CTFlearn{XXXXXXXXXX}`, where `XXXXXXXXXX` represents the actual flag you discover while examining the image using these techniques.

By running the `strings` and `grep` commands on the image, you'll be able to reveal the hidden flag and successfully complete the PikesPeak challenge.

## Flag
The flag for this challenge is in the format: `CTFlearn{XXXXXXXXXX}`.

Happy forensic investigation in the PikesPeak challenge, and best of luck in uncovering the flag!
