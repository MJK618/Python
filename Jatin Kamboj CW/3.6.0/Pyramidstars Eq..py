#Pyramid Of Stars(Equilateral) 
#By Jatin Kamboj
#8647
while(1):
        print("Press 0 To Exit")
        k = 0
        n=int(input("Enter Number Of Rows"))
        
        if n==0:
            exit()
        else:    
            for i in range(1, n+1):
                for space in range(1, (n-i)+1):
                    print(end="  ")
                while k != (2*i-1):
                    print("* ", end="")
                    k = k + 1
                k = 0
                print()

