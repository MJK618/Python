#Summation of first n terms using loop
#By Jatin Kamboj
while(1):
    print("Press 0 To Exit")
    Sum=0
    i=1
    n=int(input("Enter Number Of Terms"))
    if n==0:
        exit()
    else:    
        for i in range(1,n+1):
            Sum=Sum+i
            print(("Sum="),(Sum))
    print("Total Sum=",Sum)                                                                                            
