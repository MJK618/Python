#Encoding and Decoding A Message
#By MJK618
#Major code is from Frequence Analyser Program

from collections import Counter

#Elements to be removed
remove = ['1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','^','&',' ','\n','\t'
          '(',')','_','-',';',':','\"','\'',',','<','.','>','?','/','\\','*','=','+','~','`']

#Introduction
print("Hello there! I am a Frequency Analysis Program")
print("\nPass me the strings and I will order the alphabets present in it according to their frequency of occuring.\n")
print("I will create a secret message by making a string of most occuring letters.\nHope You Enjoy ;)")

#Took phrases garbage
string_input = ("""vfhdjgvfdhgjskdhfsahrioweajdabcdefghijklmnopqrstuvwxyzjasdfhjweoaiufsoadhfsfiweoiquihgftttdgahufgavcashbcxksanxkazbJKBZahjGSIAJHSOISJPOAkspoisdioeyfuisdgfudgjhzxgbahxahxnjsjhxolasj""").lower()

#Removing the endesired elements
for element in remove:
    string_input = string_input.replace(element,'')
print("After removing : "+string_input)
total_length = len(string_input)

occurence_count = Counter(string_input)

#Displaying the content
print("\nI have analysed your data input as follows")
print("\n\tLetter\t\t\tOccurence\t\tPercentage")
for letter,count in sorted(occurence_count.items()):
    percentage = round(100*count/total_length,2)
    print("\t  " + letter + " \t\t\t " + str(count) + " \t\t\t " + str(percentage) + "%")

print()
#Storing the most occuring letters as a list

most_occuring = occurence_count.most_common()  # returns a list of tuples with letter and its frequency
first_ord = []


print("The message formed from the most occuring letters : ",end='')
for pair in most_occuring:
       first_ord.append(pair[0])
for letter in first_ord:
    print(letter,end='')
    

#Doing the Same Above thing for the second string input
print("\n\n*****************************************************************")

#Took phrases as garbage
another_string_input = ("""Sakshi is going to mabcdefghijklmnopqrstuvwxyzarket and she is also a stupid girl watching at the computer screen like a noob.fnhdsdgfcsdadgsydftweaytgdfyutgfwqetgyufg""").lower()
#Removing the endesired elements
for element in remove:
    another_string_input = another_string_input.replace(element,'')
print("After removing : "+ another_string_input)
total_length = len(another_string_input)

occurence_count = Counter(another_string_input)

#Displaying the content
print("\nI have analysed your data input as follows")
print("\n\tLetter\t\t\tOccurence\t\tPercentage")
for letter,count in sorted(occurence_count.items()):
    percentage = round(100*count/total_length,2)
    print("\t  " + letter + " \t\t\t " + str(count) + " \t\t\t " + str(percentage) + "%")

print()
#Storing the most occuring letters as a list

most_occuring = occurence_count.most_common()  # returns a list of tuples with letter and its frequency
another_ord = []

print("The message formed from the most occuring letters : ",end='')
for pair in most_occuring:
       another_ord.append(pair[0])
for letter in another_ord:
    print(letter,end='')

       
#Encoding and Decoding
choice = input("\n\nPress 1 for Encoding and Press 2 for Decoding your message : ")
message = input("\nEnter your message : ")
for element in remove:
    message = message.replace(element,'')

if choice == '1':
    encoded_message = []
    for letter in message:
        index = first_ord.index(letter)
        letter = another_ord[index]
        encoded_message.append(letter)

    for letter in encoded_message:
        print(letter,end='')
elif choice == '2':
    decoded_message = []
    for letter in message:
        index = another_ord.index(letter)
        letter = first_ord[index]
        decoded_message.append(letter)

    for letter in decoded_message:
        print(letter,end='')
else:
    print("Please enter a valid input... ")
    










    
    
