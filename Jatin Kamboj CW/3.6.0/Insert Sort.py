#Insertion Sort
#By Jatin Kamboj
while(1):
    print("\t\t\t\tInsertion Sort")
    print("Press 0 To Exit")
    A=[]
    n=int(input("Enter The Number Of Elements To Be Entered"))
    if n==0:
        exit()
    else:    
        A=[0]*n
        for i in range (0,n):
            A[i]=int(input("Enter The Values In The Array"))
        print(("Originl Array="),A)

          
        def insertsort(a,n):
            for i in range (1,n):

                currentv=a[i]
                pos=i
                while pos>0 and a[pos-1]>currentv:
                    a[pos]=a[pos-1]
                    pos-=1
                a[pos]=currentv
        insertsort(A,n)        
        print("\t\t\tAfter Sorting\t\t\t")
        print("Sorted Array=",A)
        
