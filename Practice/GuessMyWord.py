#Guess My Word Program
#By MJK618
import random
"""
import pandas as pd
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
pd.set_option('display.width',None)
pd.set_option('display.max_colwidth',-1)
"""

word_dict = {'sports':['ball','bat','football','cricket','basketball','skating','table tennis','hockey','badminton','baseball','rugby','kabaddi',],
             'programming':['code','compile','java','python','bugs'],
             'computer':['mouse','keyboard','monitor','cpu','speakers','printer','input','output','internet',],
             'fruits':['apple','mango','grapes','lichi','strawberry','watermelon','papaya','guava','orange','pomengranate',],
             'colours':['red','blue','yellow','green','blue','orange','pink','black','white','skin','purple','brown','mustard',],
             'body parts':['heart','lungs','eyes','nose','brain','tongue','ears','arms','legs','lips','mouth','stomach','feet','skin','liver','teeth','cheeks','chin','hairs',],
             'languages':['sanskrit','hindi','marathi','punjabi','english','german','french','urdu','bengali','russian','spanish','italian','portuguese']
             }

#df = pd.DataFrame(list(word_dict.items()),columns=['1','2'])
#print(df)

#Introduction
print("Hey there,I am a Word Guessing Program")
print("\nI'll take an input for the topic and would think of a random word related to it.")
print("Also I would reveal a random letter of the word I am thinking of after each wrong attempt made by you.\n\t\t\nHope You Will Enjoy!!!")
player_name = input("Enter your name : ")
print("WOW! " + player_name.title() + " is really cool name.\nLet's start the game...\n")

running = 'y'
while running != 'q':
    #Displaying topics
    print("\nI have the following topics : \n")
    topic_menu = ['']
    for key in word_dict:
        topic_menu.append(key)
    for topic_num in range(1,len(topic_menu)):
        print("\t"+str(topic_num) + " - " + topic_menu[topic_num].title())
        #print("\t-" + key.title())
    #Taking Input    
    topic_num = int(input("\nEnter the topic number : "))
    if topic_num <= len(topic_menu):
        topic = (topic_menu[topic_num]).lower()
        list_word = list(word_dict[topic])
        word = random.choice(list(list_word))

        
        #Working (Thinking of the word randomly)

        if topic in word_dict:
            
            temp_word = []
            for letter in word:
                temp_word.append('-')
            print("\n\t\tYou chose topic - " + topic.title())
            print("\nI have a "+str(len(word)) +" letter word in my mind related to topic - " + topic.title() + ".")
                
                
            guess = ''
            guess_count = 0
            while guess != word:
                guess = input("\nEnter your guess : ").lower()
                guess_count += 1

                #Checking for correct guess
                if guess == word:
                    print("\nGREAT " +player_name.title() +"!,you guessed the word \'" + word + "\' in " + str(guess_count) + " guesses.")


                else:
                    print("\nNO! This is not the correct guess.Let me reveal a alphabet for you. ")
                    #Updating temp_word
                    updating = True
                    while updating:
                        temp_index = random.randint(0,len(temp_word)-1)
                        if temp_word[temp_index] == "-":
                            temp_word[temp_index] = word[temp_index]
                            updating = False
                    print("".join(temp_word))        

    else:
        print("\nPlease enter a valid option.")
    running = input("\n\nPress enter to play again or press 'q' to quit : ").lower()
print("\nThank You so much for playing with me.\nHope you enjoyed Tee :)")
    
