#Queue
#By Jatin Kamboj
class queue (object):
    def __init__(self):
        self.q=[]
    def insert(self,v):
        self.q.append(v)
    def delete(self):
        return self.q.pop(0)
    def isempty(self):
        return (len(self.q))==0
    def display(self):
        return self.q

q1=queue()
while(1):
    print("Press 1 To Insert")
    print("Press 2 To Delete")
    print("Press 3 To Display")
    print("Press 4 To Exit")
    ch=int(input("Enter Your Choice"))
    if ch==1:
           v=int(input("Enter Value"))
           q1.insert(v)
        
    elif ch==2:
        if q1.isempty():
            print("Empty Queue")
        else:
            print(q1.delete())
    elif ch==3:
        if q1.isempty():
           print("Empty Queue")
        else:
           print(q1.display())
           
    else:
        exit()
           
