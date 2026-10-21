import numpy as np 

A=[]
print("enter the elements for the first matrix A:")
for i in range (2):
    row=[]
    for j in range(2):
        row.append(int(input("Enter the element: ")))
    A.append(row)
B=[]
print ("enter the elements for the 2nd matrix B:")
for i in range (2):
    row=[]
    for j in range(2):
        row.append(int(input("enter the element: ")))
    B.append(row)

add=[[0,0],[0,0]]
for i in range(2):
    for j in range(2):
        add[i][j]=A[i][j]+B[i][j]
print ("result using lists:")
for row in add:
    print (row)

rA=np.array(A)   
rB=np.array(B)
rR=rA+rB
print ("Result using numpy")     
print(rR)
