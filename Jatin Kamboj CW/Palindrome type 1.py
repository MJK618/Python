#Palindrome
#By Jatin Kamboj
str=input("Enter The Word")
l=len(str)
mid=l/2
rev=-1
for i in range (mid):
    if str[i]==str[rev]:
        i=i+1
        rev=rev-1
    else:
         print("It Is Not A Palindrome")
         break
else:
    print("It Is A Palindrome")
    

