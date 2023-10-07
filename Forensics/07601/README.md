# 07601 - CTF Challenge Writeup

Challenge: 07601
Points: 60
Category: Forensics

## Objective
The objective of the 07601 challenge is to explore image metadata and uncover hidden content within the image. Your task is to reveal the flag by following forensics methods.

## Solution
To successfully complete this challenge, follow these steps:

1. **Image Examination**: The challenge provides you with an image. Start by inspecting the image to find clues about hidden content.

2. **Metadata Analysis**: Use a tool like `exiftool` to check for metadata in the image. In some challenges, the flag may be hidden within the metadata.

3. **Binwalk Discovery**: If you don't find the flag in the image's metadata, consider using `binwalk`, a tool commonly used in CTF challenges. Run `binwalk` on the image to reveal any hidden files or data within it.

4. **Extraction**: Once `binwalk` detects hidden files, extract them to reveal their content. In this challenge, you mentioned that you found a bunch of zip files.

    ```
        binwalk -e <file>
    ```

5. **Hidden Image**: Examine the extracted files and look for hidden content. In some cases, hidden flags are revealed within images, using various forensics methods.

6. **Flag Discovery**: By carefully inspecting the hidden image and applying forensics techniques, you will eventually discover the flag.

The flag format for this challenge is `CTFlearn{XXXXXXXXXX}`, where `XXXXXXXXXX` represents the actual flag you uncover through these steps.

## Flag
The flag for this challenge is in the format: `CTFlearn{XXXXXXXXXX}`.

Enjoy your exploration of image metadata and uncovering hidden content, and happy hacking!
