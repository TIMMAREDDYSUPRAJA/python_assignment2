import re
print("Password should contain atleast 1 uppercase,1 lower case,numbers and special symbols ")
password = input("Enter a number:")
a=0
while True:  
	if (len(password)<6):
		a=-1
		break
	elif (len(password)>15):
		a=-1
		break
	elif not re.search("[a-z]", password):
		a=-1
		break
	elif not re.search("[A-Z]", password):
		a=-1
		break
	elif not re.search("[0-9]", password):
		a=-1
		break
	elif not re.search("[%^_@$#]", password):
		a=-1
		break
	elif re.search("\s", password):
		a=-1
		break
	else:
		a=0
		print("Password Valid")
		break
  
if a==-1:
    print("Not a Valid Password")
