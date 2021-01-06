#Program To Make List
#By Jatin Kamboj
L=[]
n=input("Enter Number Of Terms To Be Input")
for i in range(0,n):
    x=raw_input("Enter Terms")
    L.append(x)
print L
print"***************Extend Function On List***************"
L1=[]
y=input("Enter Numbers Of Terms To Be Input")
for i in range (0,y):
    z=raw_input("Enter Terms")
    L1.append(z)
    print("L1="),L1
L.extend(L1)
print L

L.sort()
print L








    
