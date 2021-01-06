
#Program To Make List
#By Jatin Kamboj
L=[]
n=int(input("Enter Number Of Terms To Be Input"))
for i in range(0,n):
    x=int(input("Enter Terms"))
    L.append(x)
print (L)
print("\t\t\t\tExtend Function On List\t\t\t\t")
L1=[]
y=int(input("Enter Numbers Of Terms To Be Input"))
for i in range (0,y):
    z=int(input("Enter Terms"))
    L1.append(z)
    print(("L1="),L1)
L.extend(L1)
print (L)

print("\t\t\t\tSorted List\t\t\t\t")
L.sort()
print (L)

print("\t\t\t\tPopping\t\t\t\t")
z=int(input("Enter The Index Of The Term To Be Popped"))
L.pop(z)
print(L)

print("\t\t\t\tCount\t\t\t\tt")
k=int(input("Enter The Element To Be Counted"))
c=L.count(k)

print(k,"occured",c,"times")

print("\t\t\t\tInsert\t\t\t\t")
d=int(input("Enter Index Where The Number Is To Be Inserted"))
s=input("Enter The Term To Be Inserted")
L.insert(d,s)
print(L)


print("\t\t\t\tReversing\t\t\t\t")
L.reverse()

print(L)


      





    
