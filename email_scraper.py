import re
file = open("toronto_bus_list.txt", "r")
out = open("email_list.txt", "w")
file_str = file.read()
pattern = re.compile("[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?")
for email in re.findall(pattern, file_str):
	print(email) #debugging purposes
	out.write(email + ", \n")


out.close()
file.close()
