import random
import os

#Read from text file words.txt, remove \n and convert all words to lower case
filein=open("words.txt","r")
lines1=filein.readlines()
lines2=[]
lines=[]
for i in lines1:
    lines2.append(i.rstrip())

for i in lines2:
    lines.append(i.lower())
global guesses_left
global score
score=0
while(1):
    os.system("cls")
    print("Score is:",score)
    #Select a random word from the words.txt file
    index=random.randint(1,len(lines)-1)
    curr_word=lines[index]
    
    guesses_left=8
    hide_word="*"*len(curr_word)
    entered_char_list=[]
    print("\n\n   ",hide_word,"\n\n")
    while(guesses_left>0):
        
        entered_char=input("\nGuess a letter: ")
        if(entered_char not in curr_word):
            guesses_left-=1
        os.system("cls")
        print("\nGuesses left: ",guesses_left)
        entered_char_list.append(entered_char)
        count_stars=0
        print("\n\n   ",end="")
        for i in range(len(curr_word)):
            if(curr_word[i] in entered_char_list):
                print(curr_word[i],end="")
            else:
                print(hide_word[i],end="")
                count_stars+=1
        print("\n\n")
        
        if(count_stars==0):
            print("\n\nYou have guessed the word correctly!")
            print("You get a point")
            score+=1
            
            break
    if(guesses_left==0):
        os.system("cls")
        print("\n\n  The correct word was:",curr_word)
        print("\n\nSadly you have lost the game")
        print("You get no point")    
    inp=input("Press e to exit or anything else to continue: ")
    if(inp=="e"):
        os.system("cls")
        print("\n\nYour total score is:",score)
        break