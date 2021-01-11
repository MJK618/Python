#Programe to check if the given year is leap year or not
#By Jatin Kamboj
while(1):
    print("\t\t\t\tTo Check If A Year Is Leap Year Or Not")
    print("\nPress 0 To Exit")
    y=int(input("Enter The Year"))
    if y==0:
        exit()
    else:
        if ((y%4==0)&(y%100!=0))|(y%400==0):
            print("This is a leap year")
        else:
            print("This is not a leap year") 
    
   
    
    

   
  
  
