#Bubble Sort
#BY Jatin Kamboj
A=[]
n=int(input("Enter The Number Of Elements To Be Entered"))
A=[0]*n
for i in range (0,n):
    A[i]=int(input("Enter The Values In The Array"))
print(A)

def bubsort(A,n):
    pass1=0
    while pass1 <(n-1):
        for i in range(0,(n-1)):
            if A[i]>A[i+1]:
                temp=A[i]
                A[i]=A[i+1]
                A[i+1]=temp
        pass1=pass1+1
bubsort(A,n)   
print("\t\t\t\tSorted Array\t\t\t\t")         
print(A)            
    
