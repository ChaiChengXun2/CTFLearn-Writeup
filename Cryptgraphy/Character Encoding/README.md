# Character Encoding

## Basic Information
Category: Cryptography  
Difficulty: Easy  
Points: 20  

## Solving
The concept of of this challenge is to familiarise yourself with ASCII.
  
**Step 1:**  
You can use hexadecimal to ASCII converters online or a python script. The one I like to use is [RapidTables](https://www.rapidtables.com/convert/number/hex-to-ascii.html)   

Alternatively, you can you a python script as follows 
```
#!/usr/bin/python3

import binascii

def main():
	flag = []
	hexadecimal = "41 42 43 54 46 7B 34 35 43 31 31 5F 31 35 5F 55 35 33 46 55 4C 7D".split(" ")
	for char in hexadecimal:
		flag.append(bytes.fromhex(char).decode("utf-8"))

	print(''.join(flag))

main()
```

**Step 2:**   
Copy and paste the flag to complete the challenge  
```ABCTF{45C11_15_U53FUL}```  

**SOLVED**  
