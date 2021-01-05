#Linear search
lst=[1,2,3,4,5,6,7,8,9]
n=9
def lsearch(a,v,n):

    i=0
    found=0

    while i<n and not found:
        if lst[i]==a:
            found=1
        else:
            i+=1
    if found==1:
        return i
    else:
        return -1

a=lst
v=int(input())

pos=lsearch(a,v,n)

print(pos)
