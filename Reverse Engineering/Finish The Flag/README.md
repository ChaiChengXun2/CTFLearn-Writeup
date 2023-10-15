## Challenge: Finish the Flag

- **Category:** Reverse Engineering
- **Points:** 30

### Objective

The objective of this challenge is to complete the flag hidden within a given executable binary.

### Solution

This challenge proved to be more challenging than expected. The README file provides a hint about using a Linux command to decode something, but it requires the flag to start with. To proceed, I scanned the QR code using `zbarimg` and retrieved a Base64 encoded message.

I decoded the Base64 message and found that it represented an ELF executable binary. To convert it back to a binary file, I used the following command:

```bash
base64 -d <<< "base64 encoded message" > output
```

Next, I analyzed the binary using Ghidra, but the flag was not immediately apparent. Instead, I noticed some important details:

- The binary didn't have a main function.
- It appeared to stay in a loop, performing XOR operations.

Suspecting that the flag might be the result of these XOR operations, I turned to GDB for further analysis. Here's how I set up GDB:

```bash
set disassembly-flavor intel
set pagination off
```

To identify the functions in the binary, I used the command:

```
info functions
```

Since the XOR operations were within the `bite_of_flag` function, I set a breakpoint just after it and printed the value of the `dl` register as I continued the execution. Initially, I thought I didn't have the flag, as the `dl` register contained an invalid address.

However, as I pressed "c" to continue the execution, I noticed that the addresses in the `dl` register were hexadecimal and decodable. Running the program again and tracking the addresses, I decoded them to reveal the flag.

The flag is: `CTFlearn{XXXXXXXXXX}`.
