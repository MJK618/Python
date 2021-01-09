#Multiplication Of Matrices
#By Jatin Kamboj

m1=int(input("Enter Number Of Rows Of First Matrix"))
n1=int(input("Enter Number Of Columns Of First Matrix"))


m2=int(input("Enter Number Of Rows Of Second Matrix"))
n2=int(input("Enter Number Of Columns Of Second Matrix"))


if n1!=m2:
    print("ERROR:Matrices Are Not Compatible For Multiplication")

else:
    mat1=[]
    mat2=[]
    mat3=[]
    

for i in range(0,m1):
    mat1.append([])
for i in range(0,m2):
    mat2.append([])
for i in range(0,m1):
    mat3.append([])
    
for i in range(0,m1):
    for j in range (0,n1):
        mat1[i].append(j)
        mat1[i][j]=0
for i in range(0,m2):
    for j in range (0,n2):
        mat2[i].append(j)
        mat2[i][j]=0
for i in range(0,m1):
    for j in range (0,n2):
        mat3[i].append(j)
        mat3[i][j]=0

print("Enter First Matrix")
for i in range(0,m1):
    for j in range (0,n1):
        mat1[i][j]=int(input())

print("Enter Second Matrix")
for i in range(0,m2):
    for j in range (0,n2):
        mat2[i][j]=int(input())
        

print("First Matrix")
for r in mat1:
    for c in r:
        print(c,end=" ")
    print()

print("Second Matrix")
for r in mat2:
    for c in r:
        print(c,end=" ")
    print()

#Multiply
for  i in range(0,m1):
    for j in range (0,m1):
        sum=0
        for k in range(0,m2):
             sum=sum+mat1[i][k]*mat2[k][j]
             mat3[i][j]=sum
print()
print("Resultant Matrix")
for r in mat3:
    for c in r:
        print(c,end=" ")
    print()
    
