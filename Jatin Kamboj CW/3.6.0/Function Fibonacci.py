#Function For Fibonacci Series
#By Jatin Kamboj
while(1):
    n=int(input("Enter the number"))
    def rfibo(n):
        if n<=0:return-1
        if n<=1:return 0
        if n<=2:return 1
        return (rfibo(n-2)+rfibo(n-1))
    print(rfibo(n))
      
