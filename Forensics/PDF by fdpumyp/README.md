# CTF Challenge Writeup
**Name:** PDF by fdpumyp  
**Points:** 20  
**Category:** Forensics  
**Objective:** To learn about data hidden within data

## Solution

1. **Initial Observation**  
   - I started by examining the PDF file provided in the challenge. At first glance, it appeared empty with no visible content.

2. **Highlighting Text in the PDF**  
   - To investigate further, I tried highlighting text within the PDF by selecting and dragging the mouse cursor over the document.
   - This revealed the text "oo oo oo" within the PDF, but I quickly realized that it wasn't the flag.

3. **Exploring Metadata with Exiftool and PDFinfo**  
   - To uncover any hidden information, I attempted to use standard tools such as `exiftool` and `pdfinfo` to extract metadata from the PDF. However, these tools didn't provide any useful insights.

4. **Using xxd for Byte-Level Analysis**  
   - My next approach was to explore the PDF at the byte level using the `xxd` utility.
   - Within the binary data, I spotted a base64-encoded string that wasn't visible in the standard PDF viewer.

5. **Decoding Base64 with Strings**  
   - To extract the hidden information, I employed the `strings` command to extract and display the base64-encoded string from the PDF.
   - After decoding the base64 string, I found the flag.

6. **Flag Extraction**  
   - The flag was in the format:
        ```
        CTFlearn{XXXXXXXXXX}
        ```

I replaced the 'XXXXXXXXXX' with the actual flag I obtained after decoding the base64 string from the PDF.

## Flag
The flag for the PDF by fdpumyp challenge is `CTFlearn{XXXXXXXXXX}`. I successfully solved this Forensics challenge and learned about uncovering hidden data within data!
