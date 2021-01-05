#Decimal to binary and hexadecimal converter program

#Introduction about program
print("Hello there! I am a decimal to binary & hexadecimal converter app")
user_name = input("What's your name? : ")
print("\n Hey " + user_name.title() + " let's move ahead.")


#Taking inputs for calculation
nums = int(input("Enter the number till where you want to list all the values : "))
print("Decimal\t---------\tBinary\t----------\tHexadecimal")
for num in range(nums):
    print(" "+str(num)+ "\t--------------\t" +str(bin(num) + "\t----------------\t"+ str(oct(num))))
bol = bool(input("enter"))
