
#Stack
#By Jatin Kamboj
class Stack(object):
    def __init__(self):
       self.Stack=[]
    def push(self,value):
       self.Stack.append(value)
    def pop(self):
      return (self.Stack.pop())    
    def display(self):    
      return self.Stack
    def  isempty(self):
      return len(self.Stack)
S1=Stack()
while(1):
    print("1-Push a Value")
    print("2-Pop")
    print("3-Display")
    print("4-Exit")
    ch=int(input("Enter Your Choice"))
    if ch==1:
        v=int(input("Enter Value"))
        S1.push(v)
    elif ch==2:\
        print(S1.pop())
    elif ch==3:
       print(S1.display())
    elif ch==4:
        exit()
    else:
        print("Invalid Input")
       
                   


