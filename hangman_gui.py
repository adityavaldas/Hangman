import tkinter
import random
import os
score=0
def destroy():
    exit()
#Reading from words.txt and storing in list
filein=open("words.txt","r")
lines1=filein.readlines()
lines2=[]
lines=[]
for i in lines1:
    lines2.append(i.rstrip())

for i in lines2:
    lines.append(i.lower())
guesses_left=8

while(1):
    index=random.randint(1,len(lines)-1)
    curr_word=lines[index]
    hide_word="*"*len(curr_word)
    entered_char_list=[]

    entered_char=""

    def start_game(event):
        
        global curr_word
        global entered_char_list
        global guesses_left
        
        global score
        global got
        entered_char=entry_field.get()
        entered_char_list.append(entered_char)
        count_stars=0
        disp_label=""
        if(entered_char not in curr_word):
            guesses_left-=1
            output_label.config(text="Bad choice")
        else:
            output_label.config(text="Good choice")
        for i in range(len(curr_word)):
            if(curr_word[i] in entered_char_list):
                disp_label=disp_label+curr_word[i]
            else:
                disp_label=disp_label+"*"
                count_stars+=1
        word_label.config(text=disp_label)

        if(count_stars==0):
            score+=1
            index=random.randint(1,len(lines)-1)
            curr_word=lines[index]
            hide_word="*"*len(curr_word)
            entered_char_list=[]
            word_label.config(text=hide_word)
            output_label.config(text="Guessed correctly! Congratulations")
            guesses_left=8
        if(guesses_left==0):
            index=random.randint(1,len(lines)-1)
            output_label.config(text="The correct word was "+curr_word.upper())
            curr_word=lines[index]
            hide_word="*"*len(curr_word)
            entered_char_list=[]
            word_label.config(text=hide_word)
            
            guesses_left=8
        
        # curr_word_label.config(text=curr_word)
        guesses_label.config(text="Guesses left: "+str(guesses_left))
        score_label.config(text = "Score: "+str(score))
        entry_field.delete(0, tkinter.END)

    #Creating a window
    root = tkinter.Tk() 
    root.attributes("-fullscreen", True)
    # root.configure(background='#fffeeefff')
    score=0
    root.title("Hangman Game")
    root.geometry("800x500")
    heading=tkinter.Label(root, text='HANGMAN\n',font = ('Calibri', 120))
    heading.configure(fg='#111666fff')
    heading.pack()
    score_label = tkinter.Label(root, text = "Score: "+str(score),font = ('Calibri', 60))
    score_label.pack()
    # curr_word_label = tkinter.Label(root, text = "Current word: ")
    # curr_word_label.pack()
    # curr_word_label.config(text="Current word: "+curr_word)
    guesses_label = tkinter.Label(root, text = "Guesses left: "+str(guesses_left),font = ('Calibri', 40))
    guesses_label.pack()
    word_label = tkinter.Label(root, text = hide_word,font = ('Calibri', 50))
    word_label.pack()
    output_label = tkinter.Label(root, text = "All the best",font = ('Calibri', 60))
    output_label.pack()
    entry_field = tkinter.Entry(root,font = ('Calibri', 20))
    root.bind('<Return>', start_game)
    entry_field.pack()
    exit_button = tkinter.Button(root, text='Exit', width=25, command=destroy,font = ('Calibri', 20)) 
    exit_button.configure(background='#fff000333',fg='#fffffffff')
    exit_button.pack()
    
    entry_field.focus_set()

    root.mainloop()
    