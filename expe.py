import re
#import pyperclip

#text = pyperclip.paste()

#Reads the data to be extracted from list.txt file

with open("list.txt", 'r') as f:
		email = re.findall(r'[\w.-]+@[\w-]+[\.][\w]+', f.read())		
		with open("emailid.txt", 'w+') as f:
			for line in email:
				f.write(line+"\n")
				print(line)

with open("list.txt", 'r') as f:
	phone = re.findall(r'\+?\d{3}?\s?98[.-]?0?\d{0,10}', f.read())
	with open("phone.txt", 'w+') as f:
		for line in phone:
			f.write(line+"\n")
			print(line)
