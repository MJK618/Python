#Factor Generator Program
#By MJK618

#Introduction
print("I am a Factor Generator Program \nGive me a number and I will list all the factors of that number")

#Main Loop
choice = 'y'
while choice == 'y':
    num = int(input("\nEnter your number : "))   #Input for the number
    factors = []
    print("Factors of " + str(num) + " are as follows :")
    for i in range(1,num+1):
        if num%i == 0:
            factors.append(i)
            print(i)
    print("\n\tSummary")        
    for i in range(int(len(factors)/2)):
        print("\t" + str(factors[i]) + " * " + str(factors[-i-1]) + " = " + str(num)) 
  
    choice = input("Do you want to run again? (y/n)").lower()    
    





