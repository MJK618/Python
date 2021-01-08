#Program To Check Vowels
#By Jatin Kamboj
while(1):
    print("\t\t\tProgram To Check Vowels")
    str=input("\nEnter Your Statement")
    if str==0:
        exit()
    else:    
        for ch in str:
            if ch in 'aeiou':
                print((ch),("=Vowel"))
            elif ch in 'AEIOU':
                print((ch),("=Vowel"))
            else:    
                print("No Vowel")

