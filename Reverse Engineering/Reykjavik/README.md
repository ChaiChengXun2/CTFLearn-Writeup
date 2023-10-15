# CTF Challenge Writeup
**Name:** Reykjavik
**Points:** 10
**Category:** Reverse Engineering
**Objective:** To learn about the basics of reverse engineering, targeting C programs

## Solution

1. **Introduction to Reverse Engineering C Programs**
   - When dealing with reverse engineering C programs, my go-to tools are `Ghidra` and `GDB`. These tools are indispensable for dissecting and understanding the inner workings of C code.

2. **Using Ghidra to Paint a Picture**
   - If assembly code seems daunting, `Ghidra` can be your friend. It can help paint a rough picture of the program's logic, even if the variables appear cryptic.

3. **Understanding the Program Flow**
   - In reverse engineering, the primary objective is to comprehend the overall flow of the program. This is crucial in uncovering hidden information.

4. **Inspecting with GDB**
   - I used `GDB` to examine the program. The setup I typically use with `GDB` includes the following commands:
      - `set pagination off`: Disabling pagination for smoother output.
      - `set disassembly-flavor intel`: Setting the disassembly flavor to Intel syntax.
      - `disassemble main`: Analyzing the main function to understand its structure.

5. **Flag Location - Runtime Inspection**
   - During my initial analysis, I couldn't find the flag anywhere in the code. To my knowledge, it is only available during the runtime of the program.

6. **Inspecting Stack Content Before strcmp**
   - My method involved examining the stack content just before the `strcmp` function is called. We can identify the relevant line in the disassembled code: ```
        ```
        0x0000555555555168 <+200>: call 0x555555555080 <strcmp@plt>
        ```

7. **Setting a Breakpoint**
   - To achieve this, I set a breakpoint just before `strcmp` is called using the command:
      - `break *main+196`
      - This sets a breakpoint at the `main` function at the offset 196.

8. **Examining Stack Content**
   - I ran the program with the parameter `r CTFlearn{fake_flag}` and examined the stack using the command:
      - `x/5s $rsp`
      - The register `$rsp` points to the stack, and this command allows me to inspect 5 strings from the stack.

9. **Revealing the Flag**
   - Through this process, I successfully revealed the flag.

## Flag
The flag for the Reykjavik challenge is `CTFlearn{XXXXXXXXXX}`. Replace 'XXXXXXXXXX' with the actual flag you uncovered during the reverse engineering process.

Congratulations on completing this Reverse Engineering challenge! You've gained valuable insights into the basics of dissecting and understanding C programs.
