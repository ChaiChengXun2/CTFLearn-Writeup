output = ""

with open("TheMessage.txt", "r") as file: 
	content = file.read()
	for char in content:
		if char == " ":
			output += "0"
		else:
			output +="1"

print(bytearray.fromhex(hex(int(output, 2))[2:]).decode(errors="ignore"))