#Mathematical Table
#By Jatin Kamboj
while(1):
    print("\t\t\t\tMath Table")
    print("Press 0 To Exit")
    n=int(input("Enter The Number Of Which Table Is To Be Generated"))
    if n==0:
        exit()
    else:
        print("Mathematical Table")
        for i in range (1,11):
            print (n,"*",i,"=",n*i)
