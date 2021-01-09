#To Calculate Factorial (!)
#By Jatn Kamboj
while(1):
    print("\t\t\t\tCalculating Factorial (!)")
    print("Press -1 To Exit")
    n=int(input("Enter The Number"))
    if n==0:
        print ("0!=1")
    elif n==-1:
        exit()
    else:
        fact=1
    for i in range(1,n+1):
        fact=fact*i
    print((n),("!="),(fact))
