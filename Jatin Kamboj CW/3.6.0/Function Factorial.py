#To define a Function For Calculating Factorial
#By Jatin Kamboj
while(1):
    print("\t\t\t\tTo Calculate Factorial ")
    n=int(input("Enter the Number"))
    if n==-1:
        exit()
    else:    
        def rfact(n):
            if n<=0:return-1
            if n==1:return(1)
            return n*rfact(n-1)
        print(n,("! ="),(rfact(n)))

