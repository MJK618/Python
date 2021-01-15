#Program To Count Vowels
#By Jatin Kamboj
str=input("Enter Your Statement")

for ch in str:
    if ch in 'aeiou':
        print((ch),("=Vowel"))
    else:
        print("No Vowel")

