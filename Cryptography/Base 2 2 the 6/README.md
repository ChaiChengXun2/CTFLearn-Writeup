# Base 2 2 the 6

## Basic Information
Category: Cryptography  
Difficulty: Easy  
Points: 20  

## Solving
The concept of of this challenge is to familiarise yourself with BASE64.
  
**Step 1:**  
You can use online tools such as [CyberChef](https://cyberchef.org/) or [dcode](https://www.dcode.fr/en)  

Alternatively, you can use a python script
```
#!/usr/bin/python3

import base64

def main():
	hexadecimal = "Q1RGe0ZsYWdneVdhZ2d5UmFnZ3l9"
	print(base64.b64decode(hexadecimal))

main()
```

**Step 2:**   
Copy and paste the flag to complete the challenge  
```CTF{FlaggyWaggyRaggy}```  

**SOLVED**  
