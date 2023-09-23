# Basic Injection

## Basic Information
- **Category**: Web
- **Difficulty**: Easy
- **Points**: 30

## Solving
The objective of this challenge is to familiarize yourself with SQL Injections.

**Step 1: SQL Injection Payload**
- SQL Injections involve manipulating a web application's database by injecting malicious SQL code. You can experiment with various SQL Injection payloads to find vulnerabilities. An example payload that worked for me is:
  ```plaintext
  ' OR '' = '
  ```
- This payload is designed to manipulate the SQL query to always evaluate as true, effectively bypassing authentication.

**Step 2: Retrieving the Flag**
- Upon successfully executing the SQL Injection, you will gain unauthorized access to the system and can retrieve the flag

**Solved**
