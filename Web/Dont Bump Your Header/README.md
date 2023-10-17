# CTF Challenge Writeup
**Name:** Dont Bump Your Header
**Points:** 40
**Category:** Web

## Objective

The objective of the "Dont Bump Your Header" challenge was to access a web application by configuring the correct user-agent and referer header, ultimately leading to the discovery of the hidden flag.

## Solution

1. **Initial Assumption**
   - At the beginning, it was assumed that the challenge might require changing the GET request to a HEAD request. However, this initial assumption turned out to be incorrect.

2. **User-Agent Requirement**
   - Upon opening the challenge website, it became clear that the key to solving the challenge involved setting the user-agent to a specific value. The webpage provided a hint indicating that the current user-agent was incorrect.

3. **User-Agent Configuration**
   - To meet the challenge's requirements, I changed the user-agent to the value specified in the HTML comment:
     - `User-Agent: Sup3rS3cr3tAg3nt`

4. **Referer Header Modification**
   - In addition to configuring the user-agent, the referer header also needed to be adjusted according to the URI mentioned in the HTML comment:
     - `Referer: awesomesauce.com`
   - This header configuration was vital to progress in the challenge.

5. **Accessing the Hidden Flag**
   - With the user-agent and referer header correctly set, I revisited the webpage. This time, I was able to access the hidden flag.

6. **Alternative Python Script Solution**
   - As an alternative approach, one could use a Python script to automate the process. A Python script could be designed to set the user-agent and referer headers and access the website to retrieve the flag programmatically.

        ```
        import requests
        
        url = "http://165.227.106.113/header.php"
        
        headers = {
        	"User-Agent": "Sup3rS3cr3tAg3nt",
        	"Referer": "awesomesauce.com"
        }
        
        r = requests.get(url, headers=headers)
        
        print(r.text)
        ```

7. **Flag**
   - The flag for the "Dont Bump Your Header" challenge is `flag{XXXXXXXXXX}`. I replaced 'XXXXXXXXXX' with the actual flag that was uncovered once I correctly configured the user-agent and referer header.

This challenge underscored the significance of understanding HTTP headers and how their modification can enable or restrict access to web resources. It served as a practical exercise in web header manipulation and the subsequent flag retrieval.
