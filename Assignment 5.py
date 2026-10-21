import re 
user_string=input("enter the string: ")
pattern=r'^[a-zA-Z0-9]+$'
if re.match(pattern,user_string):
    print("Valid string, contians only alphanumerics.")
else:
    print("invalid string, Contains other characters")