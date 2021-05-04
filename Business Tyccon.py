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


### variables

money = 60000
income = 0
popularity = 0
name = 'company'  ### MAX 13
income_show = str(income) + '/Day'
money_show = money
money_list = []


### functions

def money_counter():
    global money, money_show, money_list

    if money >= 1000 and money <= 999999:
        money_list = list(map(int, str(money)))
        
        try:
            money_list.pop(5)
            money_show = str(money_list[0])
            money_show = money_show + str(money_list[1])
            money_show = money_show + str(money_list[2])
            money_show = money_show + 'K'
            print('m')
        except:
            try:
                money_list.pop(4)
                money_show = str(money_list[0])
                money_show = money_show + str(money_list[1])
                money_show = money_show + 'K'
                print('g')
            except:
                money_show = str(money_list[0])
                money_show = money_show + 'K'
                print('d')

    elif money >= 1000000 and money <= 999999999:
        money_list = list(map(int, str(money)))
        
        try:
            money_list.pop(8)
            money_show = str(money_list[0])
            money_show = money_show + str(money_list[1])
            money_show = money_show + str(money_list[2])
            money_show = money_show + 'M'

        except:
            try:
                money_list.pop(7)
                money_show = str(money_list[0])
                money_show = money_show + str(money_list[1])
                money_show = money_show + 'M'

            except:
                money_show = str(money_list[0])
                money_show = money_show + 'M'
        
    elif money >= 100000000 and money <= 999999999999:
        money_list = list(map(int, str(money)))
        
        try:
            money_list.pop(11)
            money_show = str(money_list[0])
            money_show = money_show + str(money_list[1])
            money_show = money_show + str(money_list[2])
            money_show = money_show + 'B'

        except:
            try:
                money_list.pop(10)
                money_show = str(money_list[0])
                money_show = money_show + str(money_list[1])
                money_show = money_show + 'B'

            except:
                money_show = str(money_list[0])
                money_show = money_show + 'B'

    elif money >= 1000000000000 and money <= 999999999999999:
        money_list = list(map(int, str(money)))
        
        try:
            money_list.pop(14)
            money_show = str(money_list[0])
            money_show = money_show + str(money_list[1])
            money_show = money_show + str(money_list[2])
            money_show = money_show + 'T'
            print('m')
        except:
            try:
                money_list.pop(13)
                money_show = str(money_list[0])
                money_show = money_show + str(money_list[1])
                money_show = money_show + 'T'
                print('g')
            except:
                money_show = str(money_list[0])
                money_show = money_show + 'T'
                print('d')
    
    money_lbl.configure(text=money_show)

    print(len(money_list))
    print(money_list)
    



root = Tk()

root.title("Business Tyccon v0.1")
root.geometry('1920x1080')



### loading assets

bg_img = PhotoImage(file='assets\\bg.png')
tab_img = PhotoImage(file='assets\\tab.png')
inc_img = PhotoImage(file='assets\\income.png')
prob_img = PhotoImage(file='assets\\problem_.png')
loss_img = PhotoImage(file='assets\\loss.png')
loss_income_img = PhotoImage(file='assets\\loss_income.png')
medium_income_img = PhotoImage(file='assets\\medium_income.png')
high_income_img = PhotoImage(file='assets\\high_income.png')
settings_img = PhotoImage(file='assets\\settings.png')
company_img = PhotoImage(file='assets\\comp_name.png')
popularity_img = PhotoImage(file='assets\\popularity.png')
time_img = PhotoImage(file='assets\\time.png')

### creating widgets

bg_lbl = tk.Label(root, image=bg_img)
bg_lbl.place(x=-2,y=-2)

tab_lbl = tk.Label(root, image=tab_img)
tab_lbl.place(x=-2,y=-2)

income = tk.Label(root, image=inc_img, borderwidth=0, highlightthickness=0)
income.place(x=100,y=40)

money_lbl = tk.Label(root, text=money_show, bg='#3399cc', font=('AcmeFont',30), fg='white')
money_lbl.place(x=150,y=35)

income_lbl = tk.Label(root, image=high_income_img, borderwidth=0, highlightthickness=0)
income_lbl.place(x=290,y=40)

income_lbl_show = tk.Label(root, text=income_show, bg='#3399cc', font=('AcmeFont',20), fg='white')
income_lbl_show.place(x=340,y=48)

settings_button = tk.Button(root, image=settings_img, borderwidth=0, highlightthickness=0, activebackground='#3399cc')
settings_button.place(x=20,y=40)

company_lbl = tk.Label(root, image=company_img, borderwidth=0, highlightthickness=0)
company_lbl.place(x=810,y=40)

company_name_lbl = tk.Label(root, text=name, bg='#3366cc', font=('AcmeFont',20), fg='white')
company_name_lbl.place(x=860,y=45)

popularity_lbl = tk.Label(root, image=popularity_img, borderwidth=0, highlightthickness=0)
popularity_lbl.place(x=550,y=40)

popularity_num_lbl = tk.Label(root, text=popularity, bg='#3399cc', font=('AcmeFont',20), fg='white')
popularity_num_lbl.place(x=600,y=45)

money_counter()

root.mainloop()
