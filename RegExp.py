import re

ipAdd=input("Enter the ip address: ")

ip = re.compile("(^[2][0-5][0-5]|^[1]{0,1}[0-9]{1,2})\.([0-2][0-5][0-5]|[1]{0,1}[0-9]{1,2})\.([0-2][0-5][0-5]|[1]{0,1}[0-9]{1,2})\.([0-2][0-5][0-5]|[1]{0,1}[0-9]{1,2})$")

if ip.match(ipAdd):
    print("valid")
else:
    print("Invalid Ip Address")

print("====================================================================\n")


email=input("Enter email address: ")

em=re.compile(r"(^[a-zA-Z0-9_.+\-]+@[a-zA-Z0-9\-]+\.[a-zA-Z.]{2,5}$)")

if em.match(email):
    print("valid")
else:
    print("invalid email id")

print("====================================================================\n")

print("\nPhone number should be in the formate XXX[citycode]-XXX-XXXX")

phnum=input("Enter Phone Number: ")

phone=re.compile("(^[0-9]{3}-[0-9]{3}-[0-9]{4}$)")

if phone.match(phnum):
    print("valid")
else:
    print("invalid Phone Number")

print("====================================================================\n")

num=input("Enter Only Numbers: ")

numbers=re.compile("(^[0-9]+$)")

if numbers.match(num):
    print("valid")
else:
    print("invalid Number")
print("====================================================================\n")
char=input("Enter Only characters \nNote:spaces are allowed: ")

characters=re.compile("(^[ a-zA-Z]+$)")

if characters.match(char):
    print("valid")
else:
    print("should only be characters")

print("====================================================================\n")

special=input("Enter only special Characters(&, -, (, ),): ")

spechar=re.compile("(^[&\-\)\(]+$)")

if spechar.match(special):
    print("valid")
else:
    print("only above listed special characters are allowed")
