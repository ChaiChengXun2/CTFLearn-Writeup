# QR Code

**Points:** 30  
**Category:** Miscellaneous

## Objective

In this challenge, you are presented with a QR code. Your objective is to retrieve the hidden flag from this QR code. To do this, you will need to follow a sequence of steps to decode the message contained within the QR code.

## Solution

1. Scan the QR Code:
   - You can manually scan the QR code using your smartphone or use the `zbarimg` tool on Linux. The latter option saves you from having to copy and paste the QR code contents manually.

2. Decode the QR Code:
   - After scanning the QR code, you will obtain a Base64 encoded message.

3. Decrypt with ROT13:
   - The Base64 encoded message is encrypted using the ROT13 cipher. ROT13 is a simple letter substitution cipher that shifts characters 13 positions down the alphabet.
   - Decrypt the message using ROT13 to reveal the flag.

Now that you've successfully decoded the QR code and decrypted the message, you should have the flag.

## Flag

The flag for this challenge is: `CTFlearn{XXXXXXXXXX}`.

This challenge tests your skills in decoding QR codes and understanding basic encryption techniques like ROT13.
