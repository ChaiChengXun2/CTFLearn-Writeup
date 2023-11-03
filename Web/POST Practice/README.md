# CTF Challenge Writeup
**Name:** POST Practice
**Points:** 40
**Category:** Web

## Objective

The objective of this challenge is to understand and practice making POST requests in a web application context.

## Solution

1. **Changing the Request Type**
   - The first step in solving this challenge is to change a GET request into a POST request. This involves sending data to the web server using a POST method instead of a GET method.

2. **Method 1: Using Burp Suite**
   - One way to accomplish this task is by using Burp Suite, a powerful web vulnerability scanner and proxy tool. To do this:
     - Utilize Burp Suite's repeater function to send the request again, but this time as a POST request.
     - Ensure to modify the request, changing it from a GET request to a POST request.
     - Depending on your payload, you may need to add a ```Content-Type``` header to specify how the data is formatted. For instance, if you're sending data in the format ```username=admin&password=71urlkufpsdnlkadsf```, you need to add the ```Content-Type: application/x-www-form-urlencoded``` header.

3. **Method 2: Programmatically in Python**
   - Alternatively, you can perform this task programmatically in Python using the requests library. Here's an example code snippet:
     ```python
     import requests

     url = "http://165.227.106.113/post.php"

     data = {
         "username": "admin",
         "password": "71urlkufpsdnlkadsf"
     }

     r = requests.post(url, data=data)
     print(r.text)
     ```
   - This Python code sends a POST request to the specified URL with the provided data (username and password). The response from the server is then printed.

4. **Explanation of the Python Code**
   - In the Python code, we first import the requests library to work with HTTP requests. We specify the target URL and the data we want to send as part of the POST request, including the ```username``` and ```password``` fields.
   - We use the `requests.post()` function to send the POST request to the server. The response from the server is stored in the variable `r`.
   - Finally, we print the text content of the response using `print(r.text)`.

## Flag
The flag for the POST Practice challenge is `CTFlearn{XXXXXXXXXX}`. Please replace 'XXXXXXXXXX' with the actual flag you obtained after successfully making a POST request and obtaining the response.

Congratulations on completing this Web challenge! You've practiced changing request types and making POST requests, which are essential skills for web application security and testing.
