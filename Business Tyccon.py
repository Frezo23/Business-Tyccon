import tkinter as tk 
from tkinter import *
from tkinter.ttk import *
from tkinter import PhotoImage
import tkinter.ttk as ttk
import random
import time
import datetime
from PIL import ImageTk, Image
import pygame
import os


root = Tk()

root.title("Business Tyccon v0.1")
root.geometry('1920x1080')



### loading assets

bg_img = PhotoImage(file='assets\\bg.png')
info_img = PhotoImage(file='assets\\buying.png')


### creating widgets

bg_lbl = tk.Label(root, image=bg_img)
bg_lbl.place(x=-2,y=-2)

task_lbl = tk.Button(root, image=info_img, borderwidth=0,highlightthickness=0)
task_lbl.place(x=747,y=300)

root.mainloop()
