**Name of Challenge:** gobustme?
**Points:** 30
**Category:** Web

**Objective:** The objective is to learn how to use Gobuster for directory enumeration.

**Solution:**
- This challenge requires you to discover the flag hidden within directories on the target website.
- To accomplish this, you need to first identify the directories available on the website.
- Gobuster is a powerful tool for directory enumeration. It allows you to brute force directories by trying different words or phrases from a wordlist.
- To use Gobuster, you can execute the following command:
    ```
    gobuster dir -u "url" -w "wordlist"
    ```
- In this specific challenge, the wordlist used is "big.txt."
- You can locate the "big.txt" wordlist on your system, and then use it with Gobuster.
- Here's an example command to run Gobuster with the "big.txt" wordlist:
    ```
    gobuster dir -u "https://gobustme.ctflearn.com/" -w /usr/share/dirb/wordlists/big.txt
    ```
- To find the location of ```big.txt```, you can use the following: 
    ```
    locate big.txt
    ```
- Keep in mind that running Gobuster with a large wordlist like "big.txt" may take a considerable amount of time.
- Once Gobuster has completed its enumeration, explore the directories it discovered to find the hidden flag.

**Flag:** CTFlearn{XXXXXXXXXX}
