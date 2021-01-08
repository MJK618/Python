#Functions On Tuple
#By Jatin Kamboj
T=('1','Jatin','Shekhar','45','Tuple')    
print("This is Your Predefined Tuple=",T)

print("\t\t\t\tCounting Elements\t\t\t\t")
x=input("Enter The Element To Be Counted")
print(x,"occured",T.count(x),"times")

print("\t\t\t\tTo Check Index\t\t\t\t")
y=input("Enter The Element Whose Index Is To Be Checked")
print("The Index Of",y,"is",T.index(y))

print("\t\t\t\tLength\t\t\t\t")
l=len(T)
print("Length of the Tuple is",l)


