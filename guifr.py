import tkinter as tk
from PIL import ImageTk, Image
from tkinter import Message, Text, Canvas
import tkinter.ttk as ttk
import tkinter.font as font
import facedetection as fd
import facetraining as ft
import facerecognition as fr

def d():
    name=nv.get()
    uid=idv.get()
    print("The name is : " + name)
    #print("The id is : " + uid)
    fd.detect(uid)
    
def t():
    ft.train()
    
def tst():
    fr.test(nv.get(),idv.get())
    
window = tk.Tk()
# setting the windows size
window.geometry("800x600")
window.title("Face_Recogniser")
window.configure(background ='white')
window.grid_rowconfigure(0, weight = 1)
window.grid_columnconfigure(0, weight = 1)

my_canvas = Canvas(window,width=800,height=600)
my_canvas.pack(fill="both", expand=True)

img= Image.open(r"D:\ximpro\FaceRecognitionProject\fc.jpg")
img = img.resize((800, 600), Image.ANTIALIAS)
bg = ImageTk.PhotoImage(img)

#Set image in canvas
my_canvas.create_image(0,0,anchor="nw",image=bg)

message = tk.Label(window, text ="Face Recognition System", bg="#FF8C00", fg="white", width=31,
                   height = 1, font = ('times', 30, 'bold'))      
message.place(x = 28, y = 20)

nv=tk.StringVar()
idv=tk.IntVar() 
  
lbl = tk.Label(window, text = "ID", width = 20, height = 1, fg ="#1C3D52", bg = "white",
               font = ('times', 15, ' bold ') ) 
lbl.place(x = 5, y = 215)
  
txt = tk.Entry(window,textvariable=idv, width = 20, bg ="white", fg ="#FB8500", font = ('times', 15, 'bold'))
txt.place(x = 205, y = 215)
  
lbl2 = tk.Label(window, text ="Name", width = 20, fg ="#1C3D52", bg ="white", height = 1, font =('times', 15, 'bold')) 
lbl2.place(x = 5, y = 315)
  
txt2 = tk.Entry(window, textvariable=nv, width = 20, bg ="white", fg ="#FB8500", font = ('times', 15, 'bold'))
txt2.place(x = 205, y = 315)

takeImg = tk.Button(window, text ="Take samples", command = d, fg ="white", bg ="#1C3D52", 
width = 11, height = 1, activebackground = "#FB8500", font =('times', 15, ' bold '))
takeImg.place(x = 30, y = 520)

trainImg = tk.Button(window, text ="Train model", command = t, fg ="white", bg ="#1C3D52", 
width = 11, height = 1, activebackground = "#FB8500", font =('times', 15, ' bold '))
trainImg.place(x = 230, y = 520)

trackImg = tk.Button(window, text ="Click to test", command = tst, fg ="white", bg ="#1C3D52", 
width = 11, height = 1, activebackground = "#FB8500", font =('times', 15, ' bold '))
trackImg.place(x = 430, y = 520)

quitWindow = tk.Button(window, text ="Quit", command = window.destroy, fg ="white", bg ="#1C3D52", 
width = 11, height = 1, activebackground = "#FB8500", font =('times', 15, ' bold '))
quitWindow.place(x = 630, y = 520)
  
