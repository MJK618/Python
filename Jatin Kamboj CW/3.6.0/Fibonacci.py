#Fibonacci Series
#By Jatin Kamboj
while(1):
    print("\t\t\t\tFibonacci Series")
    n=int(input("Enter Number Of Terms"))
    if n==-1:
        exit()
    else:    
       fib1=0
       fib2=1
       print(fib1)
       print(fib2)
       for i in range(3,n+1):
           fib3=fib1+fib2
           print(fib3)
           fib1=fib2
           fib2=fib3
            
