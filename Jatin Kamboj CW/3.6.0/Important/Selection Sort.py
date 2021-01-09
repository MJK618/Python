#Selction Sort
#By Jatin Kamboj
A=[]
n=int(input("Enter The Number Of Elements To Be Entered"))
A=[0]*n
for i in range (0,n):
    A[i]=int(input("Enter The Values In The Array"))
print(A)

for j in range(0,n):
    small=A[j]
    index=j
    for i in range (j+1,n):
        if A[i]<small:
            small=A[i]
            index=i
    A[index]=A[j]
    A[j]=small
print(A)        
    
