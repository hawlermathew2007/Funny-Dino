from tkinter import *
from PIL import Image, ImageTk
import keyboard
import random
import threading
import os
import time

# decide to run dino or not
run_dino = False

# Cute or Devi # Cute mode may distribute to cute wanderer or cute with actions
dino_mode = 'Cute'

#Type of Dino
type_of_Dino = 'Blue'

# Types of Dino
types_of_dino = ['Blue', 'Yellow', 'Red', 'Green']
indexOf_typesDino = 0

# Window for the user choose the mode and dino type
opt_window = Tk()
opt_window.title("Funny Dino")

first_check = True # simply prevent dino_mode = 'Cute' for the first check

x_optWindow = int(opt_window.winfo_screenwidth()/2 - opt_window.winfo_width()/2)
y_optWindow = int(opt_window.winfo_screenheight()/2 - opt_window.winfo_height()/2)

opt_window.geometry(f"+{x_optWindow}+{y_optWindow}")

# Create Image here
current_dino_path = f'sprites/{type_of_Dino}/dino.png'
sample = PhotoImage(file=current_dino_path)
desire_size = 50
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
		indexOf_typesDino = len(types_of_dino)

	type_of_Dino = types_of_dino[indexOf_typesDino]
	current_dino_path = f'sprites/{type_of_Dino}/dino.png'

	switched_image = Image.open(current_dino_path)
	resize_switchedImage = switched_image.resize((img_width, img_height))
	current_dino = ImageTk.PhotoImage(resize_switchedImage)

	dino_type_text.config(text=type_of_Dino)
	dino_type.config(image=current_dino)


def select_one(_type):

	global dino_mode
	global first_check

	if first_check:
		if _type == 'cute':
			dino_mode = "Cute"
		else:
			dino_mode = "Devi"
		first_check = False
		return

	if cute.get() == 1 and _type=='devi':
		cute.set(0)
		devi.set(1)
		dino_mode = 'Devi'

	if devi.get() == 1 and _type=='cute':
		cute.set(1)
		devi.set(0)
		dino_mode = 'Cute'
		
	print(dino_mode)

def run_dino_func():
	global run_dino
	run_dino = True
	opt_window.destroy()

cute = IntVar()
devi = IntVar()

back = Button(opt_window, text="<", command=lambda: switch_image('back'))
back.pack()

dino_type = Label(opt_window, image=current_dino)
dino_type.pack()

dino_type_text = Label(opt_window, text=type_of_Dino)
dino_type_text.pack()

forward = Button(opt_window, text='>', command=lambda: switch_image('forward'))
forward.pack()

cute_check = Checkbutton(opt_window, text='Cute',variable=cute, onvalue=1, offvalue=0, command=lambda: select_one('cute'))
cute_check.pack()

devi_check = Checkbutton(opt_window, text='Devi',variable=devi, onvalue=1, offvalue=0, command=lambda: select_one('devi'))
devi_check.pack()

submit = Button(opt_window, text="Submit", command=run_dino_func)
submit.pack()

cancel = Button(opt_window, text='Cancel', command=lambda: opt_window.destroy())
cancel.pack()

opt_window.mainloop()

# Just Simply the Gap between the dino and the window side to make it look natural
window_gap = 80

# About Dino Path
shadow_path = f'misc/shadow.png'
dino_path = f'sprites/{type_of_Dino}/dino.png'
idle_path = f'sprites/{type_of_Dino}/Idle'
walking_path = f'sprites/{type_of_Dino}/Walking'
running_path = f'sprites/{type_of_Dino}/Running'

# Meme path
imagesMeme_path = 'meme/images'
gifsMeme_path = 'meme/gifs'

# Sprite
duplicated_sprites = []
dino_is_flipped = False

idle_index = 0
idle_time = 600
idle_sprites = [f'{idle_path}/idle1.png',f'{idle_path}/idle2.png',f'{idle_path}/idle3.png',f'{idle_path}/idle4.png']
startOf_idleDuplication = True

walking_index = 0
walking_sprites = [f'{walking_path}/walking1.png',f'{walking_path}/walking2.png',f'{walking_path}/walking3.png',f'{walking_path}/walking4.png',
					f'{walking_path}/walking5.png',f'{walking_path}/walking6.png']

running_index = 0
running_sprites = [f'{running_path}/running1.png',f'{running_path}/running2.png',f'{running_path}/running3.png',f'{running_path}/running4.png',
					f'{running_path}/running5.png',f'{running_path}/running6.png', f'{running_path}/running7.png']
running_destination_queue = 0
dino_is_dragging = False

# Velocity of the Dino
walking_speed = 35 # in millisecond
running_speed = 25
walking_step = 2
running_step = 3

