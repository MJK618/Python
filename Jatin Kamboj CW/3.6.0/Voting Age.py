#Age Calculation
#By Jatin Kamboj
x=int(input("Enter your year of Birth"))
n=int(input("Enter Current Year"))
a=n-x
print ("Your Age Is",a,"years")

if a>=18:
    print("Hurray! You are eligible for voting")
else:
    print("Oh Damn! You not eligible for voting")
