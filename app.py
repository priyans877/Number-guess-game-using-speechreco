import tkinter as tk
from tkinter import *
from PIL import ImageTk , Image
import random
import speech_recognition as sr


windows=tk.Tk()
app_width=1000
app_height=600
windows.geometry(f'{app_width}x{app_height}')
windows.config(bg="#065569")
windows.resizable(width=False,height=False)
windows.title('Number Guessing Game')
title =tk.Label(windows,text="Number Guessing Game",font=("Arial",24),fg="#3ECD21",bg="#D13F1F")
title.place(x="315",y="10")

global numberd


#making global entries for retries and target
TARGET = random.randint(0, 100)
RETRIES = 0
start_game="Hii , Buddy \n\n Click On PlayGame Button \n\n To Start The Game"
image1=Image.open("mic.png")
image1 = image1.resize((100,100), Image.ANTIALIAS)
test=ImageTk.PhotoImage(image1)
result=tk.Button(windows,font=("Arial",18,"normal","bold"),fg="White",bg="#065569")  
tryag=tk.Button(windows,text="Try Again",font=("Arial",18,"normal","bold"),fg="White",bg="#065569",command=lambda:[voice_inp()]) 
pint=tk.Button(windows,font=("Arial",13,"normal","bold"),fg="White",bg="#065569")
#talk,thanks, output button

talk=tk.Button(windows,text="Talk ....",font=("Arial",18,"normal","bold"),fg="White",bg="#065569")
thko=tk.Button(windows,text="Thanks You Intput is",font=("Arial",18,"bold"))
out=tk.Button(windows,font=("Arial",18,"normal","bold"),fg="white",bg="#065569")
def removebutton():
    global result,talk,out,thk,tryag,pint
    tryag.place_forget()
    result.place_forget()
    talk.place_forget()
    thko.place_forget()
    out.place_forget()
    pint.place_forget()



def voice_inp():
    global numberd,TARGET,talk,thko,out
    play_game.config(state=DISABLED)
    r=sr.Recognizer()
    talk.place(x=200,y=80)
    b=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89,90, 91, 92, 93, 94, 95, 96, 97,98, 99, 100] 
    try:
        with sr.Microphone() as source:
            print("talk....")
            audio_text=r.listen(source)
            ter=r.recognize_google(audio_text)
            print("thanks to give input")
        if int(ter) in b:
            i=b.index(int(ter))
        numberd=b[i]
        print(numberd)
        
        playgame()
        out.config(text=numberd)
        thko.place(x=380,y=170)
        out.place(x=480,y=260)
        return numberd
    except:
        ValueError="recall it"
    
        RequestError="request"
    
        UnknownValueError="value error"
    


def playgame():
    global RETRIES,TARGET,numberd,result,tryag
    #b=[]
    #b.append(numberd)
    choice = numberd
    '''pint.config(text=b)
    pint.place(s=0,y=350)'''
    def updateresult(hey):
        result.configure(text=hey)
    if choice != TARGET:
        RETRIES += 1
        if TARGET < choice:
            hint = f"   The required number lies between 0 and {choice}"
            updateresult(hint)
            tryag.place(x=440,y=440)
            result.place(x=230,y=350)

        else:
            hint =f"The required number lies between {choice} and 100"
            updateresult(hint)
            tryag.place(x=440,y=440)
            result.place(x=230,y=350)
    else:
        head=f"  You guessed the correct number after {RETRIES} retries\n Press PlayGame to Restart"
        tryag.place_forget()
        play_game.configure(state=NORMAL)
        updateresult(head) 
        result.place(x=230,y=350)
        


def micintpo():
    #global test
    start_ga.place_forget()
    spee=tk.Button(windows,text="To Start Speech Input \n Press Mic Icon \n\n   🎙️🎙️",font=("Arial",18,"normal","bold"),fg="#3ECD21",bg="#065569")
    hind=tk.Button(windows,text="speech number between 1 to 100",font=("Arial",13,"normal"),fg="White",bg="#065569")
    label1=tk.Button(windows,image=test,command=lambda: [voice_inp(),spee.place_forget(),hind.place_forget(),label1.place_forget()])
    #placing in this function
    spee.place(x=360,y=150)
    hind.place(x=373,y=300)
    label1.place(x=450,y=350)




#button creating
play_game=tk.Button(windows,text="PLAY GAME",font=("Arial",18,"normal","italic"),fg="White", bg="#065569",command=lambda:[micintpo(),removebutton()])
start_ga=tk.Button(windows, text=start_game,font=("Arial",15,"bold"),fg="white",bg="#000000")
exitbutton=tk.Button(windows,text="EXIT GAME",font=("Arial",18,"normal","italic"),fg="White",bg="#065569",command=exit)



#buttonn placing
start_ga.place(x=360,y=220)
play_game.place(x=180,y=530)
exitbutton.place(x=660,y=530)




windows.mainloop()