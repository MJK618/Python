#Age Calculation
#By Jatin Kamboj
x=int(input("Enter your year of Birth"))
a=2018-x
print ("Your Age Is"),a
if ((x%4==0)&(x%100!=0))|(x%400==0):
    print("Hurray! You were born in a leap year")
else:
    print("Oh Damn! You were not born in a leap year")
