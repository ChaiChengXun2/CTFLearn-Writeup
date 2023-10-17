# CTF Challenge Writeup
**Name:** Rubber Duck
**Points:** 10
**Category:** Forensics
**Objective:** To learn about the basics of forensics in CTF

## Solution

1. **Introduction to Forensics**
   - Whenever I encounter a forensics challenge, I've noticed that most of the time, it requires you to dig deep and find hidden information within the data, which is essentially metadata.

2. **The Power of ExifTool**
   - To tackle this challenge, I turned to the powerful tool called `exiftool`. This tool is a go-to for extracting metadata from various types of files.

3. **Running ExifTool**
   - With ExifTool, I started by running it on the provided file to inspect its metadata. This revealed valuable information hidden within the file.

4. **Discovering the Flag**
   - After using ExifTool, I found the flag tucked away within the metadata. The flag was hidden, but not too well-hidden for ExifTool to uncover it.

## Flag
The flag for the Rubber Duck challenge is `CTFlearn{XXXXXXXXXX}`. Be sure to replace 'XXXXXXXXXX' with the actual flag you discovered in the metadata using ExifTool.

Congratulations on completing this Forensics challenge! You've taken the first steps in learning the basics of forensic analysis in CTFs.
