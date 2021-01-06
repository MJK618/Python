#Fibonacci Series
#By Jatin Kamboj
n=int(input("Enter Number Of Terms"))
fib1=0
fib2=1
print (fib1)
print (fib2)
for i in range(3,n+1):
    fib3=fib1+fib2
    print (fib3)
    fib1=fib2
    fib2=fib3
            
