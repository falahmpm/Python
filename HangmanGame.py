import random

Hangman=["+-----+\n|  |  |\n|  O  |\n|     |\n|     |\n+-----+","+-----+\n|  |  |\n|  O  |\n| /   |\n|     |\n+-----+","+-----+\n|  |  |\n|  O  |\n| /|  |\n|     |\n+-----+","+-----+\n|  |  |\n|  O  |\n| /|\\ |\n|     |\n+-----+","+-----+\n|  |  |\n|  O  |\n| /|\\ |\n| /   |\n+-----+","+-----+\n|  |  |\n|  O  |\n| /|\\ |\n| /|\\ |\n+-----+"]


print("Hangman Game!!!")
print("---------------")
print("Lets play Hangman!!\n")
print("You have only 6 lives so try to guess the word within 6 attempts. Good luck!!\n")



words_list=["apple","banana","porsche","panamera","benz","swift"]

selected_word=random.choice(words_list)
#print(selected_word)

len=len(selected_word)

blank_word="_"*len

blank_word_list=[]

selected_word_list=[]

for i in blank_word:
    blank_word_list.append(i)

for i in selected_word:
    selected_word_list.append(i)


#print(selected_word_list)

print("The word to guess is:\n")
print(blank_word_list)

count=0
limit=6
while limit>0 and "_" in blank_word_list:
    letter=input("\nGuess the letter:").lower()
    if letter in selected_word_list:
        
        for j in range(len):
            if selected_word_list[j]==letter:
                blank_word_list[j]=letter
        print(blank_word_list)
        
    else:
        limit=limit-1
        print("wrong letter!!")
        print(Hangman[5-limit])

if selected_word_list==blank_word_list:
    print("Congratulations you guessed the word!!\n")
    print("The word is :",blank_word_list)
else:
    print("Then you are out of guesses and you are hanged")
    print("The word was:\n",selected_word_list)
    
    print("You guessed until",blank_word_list)
        
        
             

   














#Hangman0="+-----+\n|     |\n|     |\n|     |\n|     |\n+-----+"
