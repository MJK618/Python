#Programe to convert temprature from Farhneit to Celsius
#By Jatin Kamboj

t=int(input("Enter Temprature"))
print ("\n Enter 1 for F to C")
print("\n Enter 2 for C to F")
choice=int(input("Enter Choice"))
if choice==1:
    C=(t-32)*5.0/9.0
    print( C,("^C"))
else:
    F=(t*9.0/5.0)+32
    print (F,("^F"))
