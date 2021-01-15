#Programe to convert temprature from Fahrenheit to Celsius and vice versa
#By Jatin Kamboj
while(1):
    print("\t\t\t\tPrograme to convert temprature from Fahrenheit to Celsius and vice versa")
    
    print("\n Press 1 for Fahrenheit to Celsius")
    print("\n Press 2 for Celsius to Fahrenheit")
    print("\n Press 0 To Exit")
    choice=int(input("Enter Your Choice"))
    if choice==1:
        print("\t\tFor Fahrenheit To Celsius")
        t=int(input("Enter Temprature in Fahrenheit"))
        C=(t-32)*5.0/9.0
        print( C,("^C"))
    elif choice==2:
        print("\t\tFor Celsius To Fahrenheit")
        t=int(input("Enter Temprature in Celsius"))
        F=(t*9.0/5.0)+32
        print (F,("^F"))
    elif choice==0:
        exit()
    else:
        print("Invalid Input")
