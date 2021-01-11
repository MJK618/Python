#Operators Of Strings
#Jatin Kamboj
str=input("Enter Your String")

print("\t\t\t\tCapitalizing First Word\t\t\t\t")
strc=str.capitalize()
print(strc)

print("\t\t\t\tCounting Number Of Element\t\t\t\t")
x=input("Enter The Element To be Counted ")
strC=str.count(x)
print("It Occured",strC,"times")

print("\t\t\t\tTo Find\t\t\t\t")
y=input("Enter The Letter To Find")
strf=str.find(y)
print("Index of",y,"is",strf)

print("\t\t\t\tConvertimg To Lowercase\t\t\t\t")
print(str.lower())

print("\t\t\t\tConverting to Uppercase\t\t\t\t")
print(str.upper())

print("\t\t\t\tSplitting\t\t\t\t")
print(str.split())

print("\t\t\t\tReplacing\t\t\t\t")
old=input("Enter Old Instance")
new=input("Enter New Instance")
print(str.replace(old,new))

print("\t\t\t\tStriping\t\t\t\t")
x=input("Enter The Stripping Element")
print(str.strip(x))

print("\t\t\t\tSwap Casing\t\t\t\t")
print(str.swapcase())




 
    


      
