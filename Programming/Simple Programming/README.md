# Simple Steganography - CTF Challenge Writeup

Challenge: Simple Programming
Points: 30
Category: Programming

## Objective
The "Simple Steganography" challenge falls under the Programming category and aims to introduce participants to the concepts of programming. In this challenge, you are required to write a program to analyze the content of a data file (data.dat) and determine the number of 0's and 1's in each line.

## Solution
To complete this programming challenge, you can use any programming language, but the following solution outlines using Python:

1. **Open Data File**: Start by opening the "data.dat" file in Python for reading. This file contains lines of data with binary values (0 or 1).

2. **Initialize Counters**: Initialize variables to count the number of 0's and 1's in the data.

3. **Iterate Through Lines**: Iterate through each line in the file. Within each line, iterate through each character, which represents a bit.

4. **Count Bits**: For each bit in the line, check if it's '0' or '1' and update the respective counters accordingly.

5. **Display Results**: Finally, display the count of 0's and 1's.

    ```python
    with open("data.dat", "r") as file: 
    	lines = file.readlines()
    
    	count = 0
    
    	for line in lines: 
    		noOf0 = 0
    		noOf1 = 0
    
    		for bit in line[:-1]:
    			if int(bit) == 1: 
    				noOf1 += 1
    			else:
    				noOf0 += 1
    
    		if noOf0 % 3 == 0 or noOf1 % 2 == 0:
    			count += 1
    
    	print(count)
        ```
