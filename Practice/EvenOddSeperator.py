#Seperating even and odd
#By MJK618

#Introduction
print("Hello there! I am a even-odd seperator.\nYou provide me a string of integers seperated by a ','.")


choice = 'y'
while choice:
    numbers = input("\nEnter the numbers [Seperate them by a comma (,)]")    
    numbers = numbers.replace(' ','')
    numbers_list = numbers.split(',')
    print("\n\t\tResults\n")
    for number in numbers_list:
        if int(number) % 2 == 0:
            print("\t" + str(number) + " is an even number")
        else:
            print("\t" + str(number) + "is an odd number")
    choice = input("\nWould you like to do it again? (y/n)").lower()
