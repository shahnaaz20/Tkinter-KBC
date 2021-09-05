from tkinter import PhotoImage, Tk, Frame, Label, Button
from time import sleep
from tkinter.constants import BOTTOM, LEFT, RIGHT, TOP
from tkinter.font import BOLD

window = Tk()
window.geometry("1000x800")
window.title("KAUN BANEGA COROREPATI")
bg = PhotoImage(file = "kbclogo.png")
label1 = Label(height=1500,width=1500)
label1.place(x = 0,y = 2)
label2 = Label( text = "Welcome To KBC",image=bg )
label2.pack(pady = 100)
class Question:
    def __init__(self, question, answers, correctLetter):
        self.question = question
        self.answers = answers
        self.correctLetter = correctLetter

    

    def check(self, letter, view):
        global right

        if(letter == self.correctLetter):
            label = Label(view, text="Right!",fg="green",font=("Georgia",30,"bold"))
            right += 1
    
        else:
            # print("YOU LOSE THE GAME!!!!")
            
            # label = Label(view, text="Wrong!",font=("Georgia",30,"bold"))
            quit("YOU LOSE THE GAME!!!!")
            # exit()
        label.pack()
        view.after(1000, lambda *args: self.unpackView(view))


    def getView(self, window):
        view = Frame(window)
        Label(view,font=("Times New Roman",30,BOLD),text=self.question).pack()
        Button(view, text=self.answers[0], width=20,bg="navy blue",fg="yellow",font=("Times",16,"bold"), command=lambda *args: self.check("A", view)).pack()
        Button(view, text=self.answers[1], width=20,bg="navy blue",fg="yellow",font=("Times",16,"bold"),command=lambda *args: self.check("B", view)).pack()
        Button(view, text=self.answers[2], width=20,bg="navy blue",fg="yellow",font=("Times",16,"bold"),command=lambda *args: self.check("C", view)).pack()
        Button(view, text=self.answers[3], width=20,bg="navy blue",fg="yellow",font=("Times",16,"bold"),command=lambda *args: self.check("D", view)).pack()
        
        return view


    def unpackView(self, view):
        view.pack_forget()
        askQuestion()

def askQuestion():
    global questions, window, index, button, right, number_of_questions 
    
    if(len(questions) == index + 1):
        Label(window ,font=("Georgia",30,BOLD),text="YOU WON 10000000!!!!").pack()
        return
    button.pack_forget()
    index += 1
    questions[index].getView(window).pack()
questions = []
file = open("questions.txt", "r")
line = file.readline()
while(line != ""):
    questionString = line
    answers = []
    for i in range (4):
        answers.append(file.readline())
    correctLetter = file.readline()
    correctLetter = correctLetter[:-1]
    questions.append(Question(questionString, answers, correctLetter))
    line = file.readline()
file.close()
index = -1
right = 0
number_of_questions = len(questions)

button = Button(window, text="Start",bg="navy blue",fg="white",width=10,height=2,font=("ComicSansMS",40,"bold"), command=askQuestion)
button.pack()
window.mainloop()