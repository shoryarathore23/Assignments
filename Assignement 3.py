def triangle(a,b,c):
    if (a*a+b*b==c*c) or (a**2+c**2==b**2) or (c**2+b**2==a**2):
        print ("it is a right angled triangle")
    else:
        print ("it is not a right angles triangle")
        
a=int(input("enter the 1st side "))
b=int(input("enter the 2nd side "))        
c=int(input("enter the 3rd side "))

triangle(a,b,c)