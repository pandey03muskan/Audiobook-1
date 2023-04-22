import pyttsx3
import PyPDF2
import keyboard
from tkinter import*
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog

#tkinter gui making
bg='#D8B5FF'
app=Tk()
app.geometry('400x500')
app.title('Audiobook')
app.configure(bg=bg)

#init the speaker
speaker=pyttsx3.init()
path=None
def click():
    global path
    path=filedialog.askopenfilename()
    print(path)

def talk():
   page_n = page_number_box.get()
   if path and page_n:
    #open book
    book = open(path,'rb')
    #read file
    read_file =PyPDF2.PdfFileReader(book)
    #choosing the page you want to read
    page=read_file.getPage(int(page_n))
    #extract text from the page 
    text=page.extractText()
    select()
    print(text)
    speaker.say(text)
    speaker.runAndWait()
def select():
    voices=speaker.getProperty("voices")
    collect=page_version_box.get()
    if collect=='male':
        speaker.setProperty('voice', voices[0].id)
    elif collect=='female':
        speaker.setProperty('voice', voices[1].id)
def pause():
    app.destroy()    


image = Image.open('new.png')
imageResized=image.resize((120,120),Image.Resampling.LANCZOS)
image1 =ImageTk.PhotoImage(imageResized)

logo = Label(app,image=image1,bg=bg)
logo.pack()

title=Label(app,text='"Lets begin to Listen"',bg=bg,font='none',fg='#4B0082')
title.pack()

page_number=Label(app,text='Please Enter the page number',bg=bg,)
page_number.pack(pady=(50,0))

page_number_box=Entry(app,bg=bg)
page_number_box.pack()

open_PDF=Button(app,text='Open',width=20,command=click)
open_PDF.pack(pady=(40,0))

page_version=Label(app,text='Enter Male/Female',bg=bg,)
page_version.pack(pady=(50,0))
page_version_box=Entry(app,bg=bg)
page_version_box.pack()

say_PDF = Button(app,text='Talk',width=20,command=talk)
say_PDF.pack(pady=(20,0))

pause_button = Button(app, text = "Pause" , command=pause)
pause_button.pack()
app.mainloop()

