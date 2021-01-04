#Length of the last word
 
str_x = input("Enter your string")

def lengthOfLastWord(str):
    count = 0
    i = 0
    len_str_x = len(str_x)
    while (i<len_str_x):
        if str_x[i] != " ":
            count += 1
            i +=1
            
        else:
            while(str_x[i] == " "):
                count = 0
                i += 1
    return count


print("The length of the last word in the string \""+str_x+"\" is " +str(lengthOfLastWord(str_x)))



