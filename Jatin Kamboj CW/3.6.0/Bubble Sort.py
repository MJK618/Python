#Bubble Sort
#BY Jatin Kamboj
while(1):
    print("\t\t\t\tBubble Sorting")
    print("Press 0 To Exit")
    A=[]
    n=int(input("Enter The Number Of Elements To Be Entered"))
    if n==0:
        exit()
    else:    
        A=[0]*n
        for i in range (0,n):
            A[i]=int(input("Enter The Values In The Array"))
        print("Original Array=",A)

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
        print("\nAfter Sorting")
        print("Sorted Array=",A)            
    
