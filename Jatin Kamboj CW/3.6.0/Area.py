#Area Of Different 2D Shapes
#By Jatin Kamboj
while(1):
    print("\t\t\tCalculating Area Of Different 2D Shapes")
    print("Press 1 To Calculate Area Of Square")
    print("Press 2 To Calculate Area Of Rectangle")
    print("Press 3 To Calculate Area Of Triangle")
    print("Press 4 To Calculate Area Of Circle")
    print("Press 0 To Exit")
    import math
    ch=int(input("Enter Choice"))
    if (ch==1):
        a=int(input("Side Of Square"))
        Area=a*a
        print(("Area Of Square="),(Area),("Sq. Units"))
    elif (ch==2):
        l=int(input("Enter Length Of Rectangle"))
        b=int(input("Enter Breadth Of Rectangle"))
        Area=l*b
        print(("Area Of Rectangle="),(Area),("Sq. Units"))
    elif (ch==3):
        x=int(input("Enter First Side Of Triangle"))
        y=int(input("Enter Second Side Of Triangle"))
        z=int(input("Enter Third Side Of Triangle"))
        s=float(x+y+z)/2.00
        Area=math.sqrt(s*(s-x)*(s-y)*(s-z))
        print(("Area Of Triangle="),Area,("Sq. Units"))
    elif (ch==4):
        r=int(input("Enter Radius Of Circle"))
        Area=math.pi*(r*r)
        print(("Area Of Circle="),Area,("Sq. Units"))
    elif ch==0:
        exit()
