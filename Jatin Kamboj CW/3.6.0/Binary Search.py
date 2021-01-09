#Binary Search
#By Jatin Kamboj
print("\t\t\tBinary Search")
def bsearch(A,val,n):
    low=0
    high=n
    found=0
    while(low<=high)and(not found):
        mid=int((low+high)/2)
        if val<A[mid]:
            high=mid-1
        elif val>A[mid]:
            low=mid+1
        else:
            found=1
    if found:
        return mid
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
    pos=bsearch(A,val,n)
    if pos==-1:
        print("Not Present In The List")
    else:
        print ("Value Present At",pos+1)
