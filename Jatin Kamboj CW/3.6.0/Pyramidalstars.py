#Pyramid Stars(Right Angled Triangle
#By Jatin Kamboj
#8647
while(1):
    print("Press 0 To Exit")
    m=int(input("Enter Number Of Rows"))
    if m==0:
        exit()
    else:
        for i in range(0,m):
            for j in range(0, i+1):
                print("* ",end="")
            print()
