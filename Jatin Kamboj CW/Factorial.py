#To Calculate Factorial (!)
#By Jatn kamboj
n=int(input("Enter The Number"))
if n==0:
    print ("0!=1")
else:
    fact=1
for i in range(1,n+1):
    fact=fact*i
    print((n),("!="),(fact))
