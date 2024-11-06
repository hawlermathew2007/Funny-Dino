from tkinter import *
from PIL import Image, ImageTk
import pyautogui
import keyboard
import random
import threading
import os
import time

# decide to run dino or not
run_dino = False

# Cute or Devi # Cute mode may distribute to cute wanderer or cute with actions
dino_mode = 'Devi'

#Type of Dino
type_of_Dino = 'Blue'

# Types of Dino
types_of_dino = ['Blue', 'Yellow', 'Red', 'Green']
indexOf_typesDino = 0

# -----------! Window for the user choose the mode and dino type !-----------
opt_window = Tk()
opt_window.title("Funny Dino's \"Menu\"")
opt_window.iconphoto(True, PhotoImage(file='sprites/Blue/dino.png'))
opt_window.configure(background='#FAEDCB')
opt_window.resizable(False, False)

# Create Image here
current_dino_path = f'sprites/{type_of_Dino}/dino.png'
sample = PhotoImage(file=current_dino_path)
desire_size = 70
scale = desire_size/sample.width()
img_width = int(sample.width() * scale)
img_height = int(sample.height() * scale)

image = Image.open(current_dino_path)
resize_image = image.resize((img_width, img_height))
current_dino = ImageTk.PhotoImage(resize_image)

def switch_image(_type):

	# global type_of_Dino # will uncomment it until all types of dino is done with designing
	global current_dino
	global current_dino_path
	global indexOf_typesDino

	if _type == 'back':
		indexOf_typesDino -= 1
	if _type == 'forward':
		indexOf_typesDino += 1

	if indexOf_typesDino > len(types_of_dino) - 1:
		indexOf_typesDino = 0
	if indexOf_typesDino < 0:
		indexOf_typesDino = len(types_of_dino) - 1

	type_of_Dino = types_of_dino[indexOf_typesDino]
	current_dino_path = f'sprites/{type_of_Dino}/dino.png'

	switched_image = Image.open(current_dino_path)
	resize_switchedImage = switched_image.resize((img_width, img_height))
	current_dino = ImageTk.PhotoImage(resize_switchedImage)

	dino_type.config(image=current_dino)
	dino_type.config(text=type_of_Dino.upper())


def select_one(_type):

	global dino_mode
	global first_check

	if cute.get() == 1 and _type=='devi':
		cute.set(0)
		devi.set(1)
		dino_mode = 'Devi'

	if devi.get() == 1 and _type=='cute':
		cute.set(1)
		devi.set(0)
		dino_mode = 'Cute'
		

def run_dino_func():
	global run_dino
	global type_of_Dino

	run_dino = True
	type_of_Dino = types_of_dino[indexOf_typesDino]
	opt_window.destroy()


cute = IntVar()
devi = IntVar()

title = Label(opt_window, text="FUNNY DINO", font=("Fixedsys", 28, "bold"), padx=50, pady=30, background='#FAEDCB', fg='#1352AB')
title.pack()

# Select Dino Here
selectDino_frame = Frame(opt_window, background='#FAEDCB')
selectDino_frame.pack()

back = Button(selectDino_frame, text="<", font=("Fixedsys", 22), background='#FAEDCB', activebackground='#FAEDCB', command=lambda: switch_image('back'), bd=0)
back.pack(side=LEFT)

dino_type = Label(selectDino_frame, text=type_of_Dino.upper(), padx=15, pady=10, font=("Fixedsys", 17), image=current_dino, background='#FAEDCB', compound='top')
dino_type.pack(side=LEFT)

forward = Button(selectDino_frame, text='>', font=("Fixedsys", 22), background='#FAEDCB', activebackground='#FAEDCB', command=lambda: switch_image('forward'), bd=0)
forward.pack(side=LEFT)

# Select Mode here
selectMode_frame = Frame(opt_window, background='#FAEDCB', pady=30)
selectMode_frame.pack()

cute_check = Checkbutton(selectMode_frame, text='Cute', font=("Fixedsys", 16), padx=5, variable=cute, onvalue=1, offvalue=0, background='#BFFCC6', activebackground="#BFFCC6", command=lambda: select_one('cute'))
cute_check.pack(side=LEFT)

or_text = Label(selectMode_frame, text='OR', font=("Fixedsys", 12), background='#FAEDCB', padx=12)
or_text.pack(side=LEFT)

devi_check = Checkbutton(selectMode_frame, text='Devi', font=("Fixedsys", 16), padx=5, variable=devi, onvalue=1, offvalue=0, background='#FFABAB', activebackground="#FFABAB", command=lambda: select_one('devi'))
devi_check.pack(side=LEFT)

devi.set(1)

# Submite or Cancel button
block = Label(opt_window, pady=1, background='#FAEDCB')
block.pack()

submit = Button(opt_window, font=("Fixedsys", 18), text="SUBMIT", background='#A4C8E1', padx=8, bd=0, command=run_dino_func)
submit.pack()

block = Label(opt_window, pady=15, background='#FAEDCB')
block.pack()

opt_window.mainloop()

# -----------! DONE window for the user choose the mode and dino type !-----------


# Just Simply the Gap between the dino and the window side to make it look natural
window_gap = 80

# About Dino Path
shadow_path = f'misc/shadow.png'
dino_path = f'sprites/{type_of_Dino}/dino.png'
idle_path = f'sprites/{type_of_Dino}/Idle'
walking_path = f'sprites/{type_of_Dino}/Walking'
running_path = f'sprites/{type_of_Dino}/Running'
hurt_path = f'sprites/{type_of_Dino}/Hurt'
kick_path = f'sprites/{type_of_Dino}/Kick'

# Meme path
imagesMeme_path = 'meme/images'
gifsMeme_path = 'meme/gifs'
gif_fps = 50

# Sprite
duplicated_sprites = []
dino_is_flipped = False

idle_index = 0
idle_time = 500
idle_sprites = [f'{idle_path}/idle1.png',f'{idle_path}/idle2.png',f'{idle_path}/idle3.png',f'{idle_path}/idle4.png']
startOf_idleDuplication = True

walking_index = 0
walking_sprites = [f'{walking_path}/walking1.png',f'{walking_path}/walking2.png',f'{walking_path}/walking3.png',f'{walking_path}/walking4.png',
					f'{walking_path}/walking5.png',f'{walking_path}/walking6.png']

running_index = 0
running_sprites = [f'{running_path}/running1.png',f'{running_path}/running2.png',f'{running_path}/running3.png',f'{running_path}/running4.png',
					f'{running_path}/running5.png',f'{running_path}/running6.png', f'{running_path}/running7.png']
running_destination_queue = 0

ouch_one = False

hurt_index = 0
hurt_delay = 10
hurt_speed = 250
hurt_sprites = [f'{hurt_path}/hurt1.png',f'{hurt_path}/hurt2.png',f'{hurt_path}/hurt3.png']

kick_index = 0
kick_delay = 10
kick_speed = 250
kick_sprites = [f'{kick_path}/kick1.png',f'{kick_path}/kick2.png',f'{kick_path}/hurt3.png']

# Drag
dino_is_dragging = False

# Chase
chase_speed = 10
on_dumping_trash = False
current_chase_step = 0
max_chase_steps = 1000

# Velocity of the Dino
walking_speed = 32 # in millisecond
running_speed = 18
walking_step = 2
running_step = 3