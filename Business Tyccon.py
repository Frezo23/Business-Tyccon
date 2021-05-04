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
day = 10
month = 10
year = 2010
sound_on_off = True
date = str(day) + '/' + str(month) + '/' + str(year)
satisfaction = 6
satisfaction_show = str(satisfaction) + '/10' 



pygame.mixer.init()
pygame.mixer.music.load('assets/sound_track.mp3')
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(0.1)

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
        except:
            try:
                money_list.pop(4)
                money_show = str(money_list[0])
                money_show = money_show + str(money_list[1])
                money_show = money_show + 'K'
            except:
                money_show = str(money_list[0])
                money_show = money_show + 'K'

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
        except:
            try:
                money_list.pop(13)
                money_show = str(money_list[0])
                money_show = money_show + str(money_list[1])
                money_show = money_show + 'T'
            except:
                money_show = str(money_list[0])
                money_show = money_show + 'T'
    
    money_lbl.configure(text=money_show)


def update_all():
    global date

    money_counter()
    date = str(day) + '/' + str(month) + '/' + str(year)
    date_num_lbl.configure(text=date)

    
def next_day():
    global day, month, year, date

    day += 1

    if day == 31:
        month += 1
        day = 1

        if month == 13:
            month = 1
            year += 1
    
    date = str(day) + '/' + str(month) + '/' + str(year)
    date_num_lbl.configure(text=date)

    update_all()

def settings():

    def sound():
        global sound_on_off

        if sound_on_off == True:
            sound_on_off = False
            sound_button.configure(image=sound_off_img)
            pygame.mixer.music.stop()
        elif sound_on_off == False:
            sound_on_off = True
            sound_button.configure(image=sound_on_img)
            pygame.mixer.music.play(loops=-1)
            pygame.mixer.music.set_volume(0.1)

    settings_button = tk.Label(root, image=settings_screen_img, borderwidth=0, highlightthickness=0)
    settings_button.place(x=450,y=300)

    save_button = tk.Button(root, image=save_img, borderwidth=0, highlightthickness=0, activebackground='#656565')
    save_button.place(x=600,y=420)

    load_button = tk.Button(root, image=load_img, borderwidth=0, highlightthickness=0, activebackground='#656565')
    load_button.place(x=600,y=500)

    sound_button = tk.Button(root, image=sound_on_img, borderwidth=0, highlightthickness=0, activebackground='#656565', command=sound)
    sound_button.place(x=600,y=580)


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
next_day_img = PhotoImage(file='assets\\next_day.png')
satisfied_img = PhotoImage(file='assets\\satisfied.png')
partly_satisfied_img = PhotoImage(file='assets\\partly_satisfied.png')
unsatisfied_img = PhotoImage(file='assets\\unsatisfied.png')
locked_img = PhotoImage(file='assets\\locked.png')
tasks_img = PhotoImage(file='assets\\tasks.png')
settings_screen_img = PhotoImage(file='assets\\settings_screen.png')
save_img = PhotoImage(file='assets\\save_game.png')
load_img = PhotoImage(file='assets\\load.png')
sound_on_img = PhotoImage(file='assets\\sound_on.png')
sound_off_img = PhotoImage(file='assets\\sound_off.png')

### creating widgets

bg_lbl = tk.Label(root, image=bg_img)
bg_lbl.place(x=-2,y=-2)

tab_lbl = tk.Label(root, image=tab_img)
tab_lbl.place(x=-2,y=-2)

income = tk.Label(root, image=inc_img, borderwidth=0, highlightthickness=0)
income.place(x=100,y=40)

money_lbl = tk.Label(root, text=money_show, bg='#3399cc', font=('AcmeFont',20), fg='white')
money_lbl.place(x=150,y=45)

income_lbl = tk.Label(root, image=high_income_img, borderwidth=0, highlightthickness=0)
income_lbl.place(x=290,y=40)

income_lbl_show = tk.Label(root, text=income_show, bg='#3399cc', font=('AcmeFont',20), fg='white')
income_lbl_show.place(x=340,y=48)

settings_button = tk.Button(root, image=settings_img, borderwidth=0, highlightthickness=0, activebackground='#3399cc', command=settings)
settings_button.place(x=20,y=40)

company_lbl = tk.Label(root, image=company_img, borderwidth=0, highlightthickness=0)
company_lbl.place(x=810,y=40)

company_name_lbl = tk.Label(root, text=name, bg='#3366cc', font=('AcmeFont',20), fg='white')
company_name_lbl.place(x=860,y=45)

popularity_lbl = tk.Label(root, image=popularity_img, borderwidth=0, highlightthickness=0)
popularity_lbl.place(x=550,y=40)

popularity_num_lbl = tk.Label(root, text=popularity, bg='#3399cc', font=('AcmeFont',20), fg='white')
popularity_num_lbl.place(x=600,y=45)

date_lbl = tk.Label(root, image=time_img, borderwidth=0, highlightthickness=0)
date_lbl.place(x=1630,y=40)

date_num_lbl = tk.Label(root, text=date, bg='#3399cc', font=('AcmeFont',20), fg='white')
date_num_lbl.place(x=1680,y=45)

next_day_lbl = tk.Button(root, image=next_day_img, borderwidth=0, highlightthickness=0, activebackground='#3399cc',command=next_day)
next_day_lbl.place(x=1850,y=40)

customer_satisfaction_lbl = tk.Label(root, image=satisfied_img, borderwidth=0, highlightthickness=0)
customer_satisfaction_lbl.place(x=1460,y=40)

customer_satisfaction_num_lbl = tk.Label(root, text=satisfaction_show, bg='#3399cc', font=('AcmeFont',20), fg='white')
customer_satisfaction_num_lbl.place(x=1510,y=45)

locked_lbl = tk.Label(root, image=locked_img, borderwidth=0, highlightthickness=0)
locked_lbl.place(x=1250,y=40)

locked_text_lbl = tk.Label(root, text='coming soon', bg='#3399cc', font=('AcmeFont',15), fg='white')
locked_text_lbl.place(x=1300,y=50)

tasks_lbl = tk.Button(root, image=tasks_img, borderwidth=0, highlightthickness=0, activebackground='white')
tasks_lbl.place(x=0,y=900)

money_counter()

root.mainloop()