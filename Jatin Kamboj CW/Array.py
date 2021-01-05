#Arithematic Operators Applied In Array
#By Jatin Kamboj
arr1=[0]*5
arr2=[0]*5
arr3=[0]*5
arr4=[0]*5
arr5=[0]*5

for i in range(0,5):
    arr1[i]=int(input("Enter Values In First Array"))
for i in range(0,5):
    arr2[i]=int(input("Enter Values In Second Array"))
print("Addition")    
for i in range(0,5):
    arr3[i]=arr1[i]+arr2[i]
    print(("arr3[i]="),arr3[i])
print("Multiplication")    
for i in range(0,5):
    arr4[i]=arr1[i]*arr2[i]
    print(("arr4[i]="),(arr4[i]))
print("Subtraction")
for i in range(0,5):
    arr5[i]=arr1[i]-arr2[i]
    print(("arr5[i]"),(arr5[i]))
    
