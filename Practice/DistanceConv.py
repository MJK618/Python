#Miles To Km COnverter
#By MJK618

#Telling about the program
print("Hello and Welcome to distance converter program ")
print("I can convert entities for you...")

#Taking input
user_name = input("\nWhat's your name? : ")

print(user_name.title() + ", thats a nice name \n Choose from the below menu options")


#Functioning under the loop
while True:
    #Menu
    print("Press 1 for miles to Km conversion")
    print("Press 2 for Km to miles conversion")
    chosen = int(input("Press the key : "))

    if (chosen == 1):
        distance_miles = float(input("Enter the value in miles : "))
        result = round(1.60934*distance_miles, 6)
        #Presenting the results
        print(str(distance_miles) + " miles = " + str(result) + " Km")

    elif (chosen == 2):
        distance_km = float(input("Enter the value in Km : "))
        result = round(0.621371*distance_km,6)
        #Presenting the results
        print(str(distance_km) + " Km = " + str(result) + " miles")
    else:
        print("Wrong/Invalid input.\n Try again ")

    
    
