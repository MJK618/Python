#Sum Of A Series
#By Jatin Kamboj
#8647
print("Our Series Is 1+(2/2!)+(3/3!)+........(n/n!)")
while(1):
    n=int(input("Enter Your Number"))

    def rfact(n):
        if n<=0:return-1
        if n==1:return(1)


        return n*rfact(n-1)

    sum=1
    for i in range(2,n+1):
        sum=sum+(i/rfact(i))
    

    print("Sum Of the Series=",(sum))

