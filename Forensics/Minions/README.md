# CTF Challenge Writeup
**Name:** Minions  
**Points:** 20  
**Category:** Forensics  
**Objective:** To learn about basic forensic tools such as strings and binwalk

## Solution

1. **Inspect the Minion Image with ExifTool**  
   - Initially, use `exiftool` to inspect the minion image, but you won't find the flag in the metadata.

2. **Search for Hidden Information with Strings**  
   - Use the `strings` command to analyze the image. You may discover hidden directories or clues within the image.

3. **Extract Hidden Files with Binwalk**  
   - Employ `binwalk` to extract files hidden beneath the Minion image. This tool can help you reveal concealed data.

4. **Follow the Trail to Another Image**  
   - You might come across a text file during the extraction process, which provides instructions to download another image.
   - Download the specified image and proceed to the next step.

5. **Repeat Binwalk on the Second Image**  
   - Apply `binwalk` to the newly downloaded image. This step aims to uncover hidden files within this image as well.

6. **Decode Base64 in the Final Image**  
   - Run `strings` on the final image. This time, you will find the flag encoded in Base64.
   - Follow the challenge's suggestion and decode it. You might need to decode it multiple times if there are multiple layers of encoding.

## Flag
The flag for the Minions challenge is `CTFlearn{XXXXXXXXXX}`. Ensure that you replace the 'XXXXXXXXXX' with the actual flag you obtain after successfully decoding the Base64-encoded string in the final image.

Well done on completing this Forensics challenge! You've practiced using basic forensic tools like `strings` and `binwalk` to uncover hidden information within images.
