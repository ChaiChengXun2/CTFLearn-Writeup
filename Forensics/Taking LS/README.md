# Taking LS - CTF Challenge Writeup

Challenge: Taking LS
Points: 10
Category: Forensics

## Objective
The objective of the Taking LS challenge is to familiarize yourself with directories and hidden files. Your goal is to navigate through directories, discover hidden files, and uncover the flag hidden within a password-protected PDF.

## Solution
To successfully complete this challenge, follow these steps:

1. **Unzip Files**: Start by unzipping the downloaded files to access their contents.

2. **Ignore MACOSX**: Inside the unzipped files, you may notice a directory or folder named "MACOSX." This folder can be safely ignored for this challenge.

3. **Flag Location**: The flag is located within a directory named "The Flag". You need to navigate to this directory.

4. **PDF File**: Inside the "flag" directory, you may encounter a PDF file. This PDF file is password-protected and holds the flag.

5. **Password Extraction**: You can use PDF password-cracking tools, such as `pdfcrack`, to find the password for the PDF. However, there's a more straightforward way. NOTE: pdfcrack used with rockyou.txt did not work for me.

6. **Hidden Files**: Hidden files in Unix-like systems are prefixed with a dot (`.`) and are not displayed when you use the `ls` command. To reveal hidden files, use `ls -la`.

7. **Hidden Password File**: By using `ls -la`, you will see hidden files, and you'll find a file containing the password for the PDF.

8. **PDF Password**: Use the password you've found to unlock the PDF file and access the flag.

9. The flag is hidden within the unlocked PDF.

10. The flag format is `ABCTF{XXXXXXXXXX}`, with `XXXXXXXXXX` representing the actual flag you find within the PDF.

## Flag
The flag for this challenge is in the format: `ABCTF{XXXXXXXXXX}`.

Congratulations on navigating directories, uncovering hidden files, and extracting the flag from a password-protected PDF, and happy hacking!
