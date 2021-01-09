#Arithematic Operators Applied In Array
#By Jatin Kamboj
while(1):
    print("\t\t\tArithematic Operators Applied In Array")
    print("Press 0 To Exit")
    n=int(input("Enter The Length Of The Array"))
    if n==0:
        exit()
    else:
        arr1=[0]*n
        arr2=[0]*n
        arr3=[0]*n
        arr4=[0]*n
        arr5=[0]*n

        for i in range(0,n):
            arr1[i]=int(input("Enter Values In First Array"))
        for i in range(0,n):
            arr2[i]=int(input("Enter Values In Second Array"))
        print("\nAddition")    
        for i in range(0,n):
            arr3[i]=arr1[i]+arr2[i]
            print(("arr3[i]="),arr3[i])
        print("Multiplication")    
        for i in range(0,n):
            arr4[i]=arr1[i]*arr2[i]
            print(("arr4[i]="),(arr4[i]))
        print("Subtraction")
        for i in range(0,n):
            arr5[i]=arr1[i]-arr2[i]
            print(("arr5[i]"),(arr5[i]))
    
