# CTF Challenge Writeup
**Name:** Exif  
**Points:** 20  
**Category:** Forensics  
**Objective:** To learn about exiftool

## Solution

1. **Use Exiftool**  
   - As the challenge suggests, the objective is simple. Use `exiftool` on the given image to uncover hidden information.

   ```shell
   exiftool image.jpg
   ```
   
Running the command above will display the metadata and any concealed details within the image.

## Flag
The flag for the Exif challenge is `CTFlearn{XXXXXXXXXX}`. Ensure that you replace the 'XXXXXXXXXX' with the actual flag you obtain by using `exiftool` on the image.

## Congratulations
Congratulations on completing this Forensics challenge! You've learned about the power of `exiftool` for examining image metadata and finding hidden information.
