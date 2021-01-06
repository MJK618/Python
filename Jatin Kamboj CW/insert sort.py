#Insertion Sort
#By Jatin Kamboj
def insertsort(a,n):
    for i in range(1,n):
        currentv=a[i]
        pos=i
        while pos>0 and a[pos-1]>currentv:
            a[pos]=a[pos-1]
            pos-=1
        a[pos]=currentv       
a=[]
n=int(input("Enter The Number Of Elements To Be Entered"))
a=[0]*n
for i in range (0,n):
    a[i]=int(input("Enter The Values In The Array"))
print(a)
insertsort(a,n)
print(a)