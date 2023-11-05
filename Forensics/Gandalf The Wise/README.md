# CTF Challenge Writeup
**Name:** Gandalf The Wise  
**Points:** 30  
**Category:** Forensics  
**Objective:** To learn about metadata of images

## Solution

1. **Examine Metadata with ExifTool**
   - Run `exiftool gandalf.jpg` to inspect the image's metadata.

2. **Suspicious Comments**  
   - Identify any suspicious comments in the metadata.

3. **Decrypt the Comment**  
   - Decrypt the suspicious comment using appropriate techniques.

4. **Flag Extraction**  
   - Extract the flag in the format `CTFlearn{XXXXXXXXXX}` from the decrypted comment.

## Flag
`CTFlearn{XXXXXXXXXX}`

Congratulations on completing this Forensics challenge!
