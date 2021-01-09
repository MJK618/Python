#Age Calculation
#By Jatin Kamboj
while(1):
    print("\t\t\tAge Calculation")
    x=int(input("Enter your year of Birth"))
    y=int(input("Enter Current Year"))
    a=y-x
    print ("Your Age Is",a)
    if ((x%4==0)&(x%100!=0))|(x%400==0):
        print("Hurray! You were born in a leap year")
    else:
        print("Oh Damn! You were not born in a leap year")
    if a>=18:
        print("Hurray! You are eligible for voting")
    elif a==0:
        print("You Have Just Born")
    else:
        print("Oh Damn! You not eligible for voting")
        
