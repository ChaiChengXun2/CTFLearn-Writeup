# Accumulator - CTF Challenge Writeup

Challenge: Accumulator
Points: 10
Category: Binary

## Objective
In the Accumulator challenge, the objective is to understand and manipulate how numbers are stored in programs. Specifically, you'll explore how integer overflow can lead to unexpected behavior in a program.

## Solution
To successfully complete the Accumulator challenge, follow these steps:

1. **Understanding Integer Storage**: Start by grasping the concept of how numbers are stored in computer programs. In this challenge, you will be working with integers.

2. **The Accumulator as an Integer**: The challenge defines the accumulator as an integer in the C programming language. In this context, it's important to know that an `int` in C is typically 4 bytes (32 bits).

3. **Threshold for Overflow**: In many programming languages, including C, there's a limit to how large or small an integer can be represented. In the case of a 32-bit `int`, the maximum positive value is 2,147,483,647, and the minimum negative value is -2,147,483,648.

4. **Integer Overflow Behavior**: When you input the value 2,147,483,647 into the program, it treats it as a positive number, which is within the representable range of a 32-bit signed integer.

5. **Overflow Scenario**: However, once you exceed this threshold by adding 1 to 2,147,483,647, the program interprets it as a negative number due to integer overflow. This is because the binary representation of 2,147,483,648 is the same as -2,147,483,648 in two's complement notation.

6. You can use this knowledge to exploit the program and discover the hidden flag.

## Flag
The flag for this challenge is in the format: `CTF{XXXXXXXXXX}`.

By understanding how integer overflow affects the behavior of the program, you'll be able to uncover the flag in the Accumulator challenge. Good luck!
