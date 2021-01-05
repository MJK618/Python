#2-D Arrays
#By Jatin Kamboj
m=int(input("Enter Number Of Rows"))
n=int(input("Enter Number Of Columns"))
    
mat=[]

for i in range(0,m):
    mat.append([])
for i in range(0,m):
    for j in range(0,n):
        mat[i].append(j)
        mat[i][j]=0
print("Enter The Elements")

for i in range(0,m):
    for j in range(0,n):
        mat[i][j]=int(input())
print(mat)

for r in mat:
    for c in r:
        print(c,end=" ")
    print()
print("\t\t\t\tAddition of matrices\t\t\t\t")    
mat1=[]
mat2=[]
mat3=[]

for i in range(0,m):
    mat1.append([])
    mat2.append([])
    mat3.append([])
    
for i in range(0,m):
    for j in range(0,n):
        mat1[i].append(j)
        mat2[i].append(j)
        mat3[i].append(j)
        mat1[i][j]=0
        mat2[i][j]=0
        mat3[i][j]=0
print("Enter First Matrix")
for i in range(0,m):
    for j in range(0,n):
        mat1[i][j]=int(input())
print("First Matrix=",(mat1))

for r in mat:
    for c in r:
        print(c,end=" ")
    print()


print("Enter Second Matrix")
for i in range(0,m):
    for j in range(0,n):
        mat2[i][j]=int(input())
print("Second Matrix=",(mat2))

for r in mat:
    for c in r:
        print(c,end=" ")
    print()

for i in range(0,m):
    for j in range(0,n):
        mat3[i][j]=mat1[i][j]+mat2[i][j]
print("Third Matrix=",(mat3))
for r in mat3:
    for c in r:
        print(c,end=" ")
    print()

        
        
