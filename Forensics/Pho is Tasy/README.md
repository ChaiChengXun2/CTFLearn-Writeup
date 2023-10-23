# CTF Challenge Writeup
**Name:** Pho is Tasy!
**Points:** 30
**Category:** Forensics
**Objective:** To learn about the basics of forensics

## Solution

1. **Forensics and Images**
   - Dealing with images in CTF challenges often leads me to familiar tools like `exiftool` and `strings`. These are essential for inspecting metadata and extracting information hidden within the image file.

2. **Running ExifTool and Strings**
   - Initially, I used both `exiftool` and `strings` to investigate the image, but to my surprise, I couldn't locate the flag. It seemed that the flag was cleverly hidden.

3. **Frustration Sets In**
   - Frustration started to set in as I began to suspect the file might be corrupted or contain other hidden files. This is not uncommon in CTF challenges, and I needed to dig deeper.

4. **Using Hexedit for a Closer Look**
   - To investigate further, I decided to use `hexedit`, a hexadecimal file editor, to check the image for anomalies. This tool allowed me to view the raw hexadecimal data of the file.

5. **Discovering the Flag**
   - Upon closer examination in `hexedit`, I made a significant discovery. The flag was present, but it was cleverly separated by bytes that are not recognised by ```strings```. This was a technique to bypass the typical `strings` command. I gathered the separated portions and reassembled the flag.

## Flag
The flag for the Pho is Tasy! challenge is `CTFlearn{XXXXXXXXXX}`. Remember to replace 'XXXXXXXXXX' with the actual flag you found after dissecting the image using `hexedit`.

Congratulations on completing this Forensics challenge! You've gained valuable experience in the basics of forensic analysis, uncovering hidden information within images.
