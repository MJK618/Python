#Student Database
#By Jatin Kamboj
print("\t\t\t\tStudent Database")

n=input("Student Name")

M=int(input("Enter your marks in Mathematics"))

P=int(input("Enter your marks in Physics"))

C=int(input("Enter your marks in Chemistry"))

x=(M+P+C)/3

print ("*********************REPORT CARD***********************")

print(("Student name-"),(n))

print(("\nYour percentage is-"),(x),("%"))
if (x>=90):
    print("\nGrade Obtained A")
elif (x>=80 and x<90):
    print("\nGrade Obtained B")
elif (x>=70 and x<80):
    print("\nGrade Obtained C")
elif (x<70 and x>=60):
    print("\nGrade Obtained D")
elif (x>60 and x<=50):
    print("\nGrade Obtained E")
else:
    print("\nYou failed")
    
    
