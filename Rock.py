from tkinter import *
import random
import tkinter as tk
window =tk.Tk()
window.geometry("2000x1000")
window.configure(background='red')
window.title("Rock Paper Scissors Game")
USER_SCORE=0
COMP_SCORE=0
USER_CHOICE=""
COMP_CHOICE=""
def choice_to_number(choice):
   rps={'rock':0,'paper':1,'scissor':2}
   return rps[choice]
def number_to_choice(number):
   rps={0:'rock',1:'paper',2:'scissor'}
   return rps[number]
def random_computer_choice():
   return random.choice(['rock','paper','scissor'])

def result(human_choice,comp_choice):
    global USER_SCORE
    global COMP_SCORE
    user=choice_to_number(human_choice)
    comp=choice_to_number(comp_choice)
    if(user==comp):
        print("Tie")
    elif((user-comp)%3==1):
        print("You wins")
        USER_SCORE+=1
    else:
        print("Comp wins")
        COMP_SCORE+=1
    text_area=tk.Text(master=window,height=14,width=50,bg="#FFFF99")
    text_area.grid(column=1,row=2)
    answer="Your Choice:{uc} \n Computer Choice:{cc} \n Your Score:{u} \n comp score:{c}".format(
                                                                    uc=USER_CHOICE,cc=COMP_CHOICE,u=USER_SCORE,c=COMP_SCORE)
    text_area.insert(tk.END,answer)


def rock():
    global USER_CHOICE
    global USER_CHOICE
    USER_CHOICE='rock'
    COMP_CHOICE=random_computer_choice()
    result(USER_CHOICE,COMP_CHOICE)
def paper():
    global USER_CHOICE
    global USER_CHOICE
    USER_CHOICE='paper'
    COMP_CHOICE=random_computer_choice()
    result(USER_CHOICE,COMP_CHOICE)
def scissor():
    global USER_CHOICE
    global USER_CHOICE
    USER_CHOICE='scissor'
    COMP_CHOICE=random_computer_choice()
    result(USER_CHOICE,COMP_CHOICE)
button1=tk.Button(window,text="    Rock     ",bg="skyblue",command=rock)
button1.pack()
mi=PhotoImage(file='C:\\Users\\rohit\\OneDrive\\Documents\\Python\\rock.png')
button1.config(image=mi,compound=TOP)
button1.grid(column=0,row=1)
button2=tk.Button(text="    Paper    ",bg="pink",command=paper)
mi1=PhotoImage(file='C:\\Users\\rohit\\OneDrive\\Documents\\Python\\paper.png')
button2.config(image=mi1,compound=TOP)
button2.grid(column=1,row=1)
button3=tk.Button(text="    Scissor  ",bg="lightgreen",command=scissor)
mi2=PhotoImage(file='C:\\Users\\rohit\\OneDrive\\Documents\\Python\\scissor.png')
button3.config(image=mi2,compound=TOP)
button3.grid(column=2,row=1)

window.mainloop()
