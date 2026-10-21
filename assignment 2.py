n1 = int(input("Enter number one: "))
n2 = int(input("Enter number two: "))
n3 = int(input("Enter number three: "))

if n1 >= n2 and n1 >= n3:
    print("Maximum value is:", n1)
elif n2 >= n1 and n2 >= n3:
    print("Maximum value is:", n2)
else:
    print("Maximum value is:", n3)