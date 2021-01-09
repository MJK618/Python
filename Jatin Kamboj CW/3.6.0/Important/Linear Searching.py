#Linear Searching
#By Jatin Kamboj
def Lsearch(A,val,n):
    i=0
    found=0
    while i<n and not(found):
        if A[i]==val:
            found=1
        else:
            i+=1
    if found:
        return i
    else:
        return -1

n=int(input("Enter The Number Of Terms To Be Entered"))
print("Enter The List")
A=[]
for i in range(0,n):
    v=int(input())
    A.append(v)
while(1):
    val=int(input("Enter Value To Be Searched"))
    pos=Lsearch(A,val,n)

    if pos==-1:
        print("Not Present In The List")
    else:
        print("Value Present At",pos+1)
