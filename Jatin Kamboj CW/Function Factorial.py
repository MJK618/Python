#To define a Function For Calculating Factorial
#By Jatin Kamboj
n=int(input("Enter the Number"))
def rfact(n):
    if n<=0:return-1
    if n==1:return(1)
    return n*rfact(n-1)
print (n,("!="),(rfact(n)))

