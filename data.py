from tkinter import *
from PIL import Image, ImageTk
import pyautogui
import random
import threading
import os
import time
import pygame

# Initialize Sound
pygame.mixer.init()

#Type of Dino
type_of_Dino = 'Blue'

# Cute or Devi # Cute mode may distribute to cute wanderer or cute with actions
dino_mode = 'Devi'


if os.path.exists('your_option.txt'):
	with open("your_option.txt", "r") as f:
		dino_state = f.read().split()
	type_of_Dino = dino_state[0]
	dino_mode = dino_state[1]
else:
	with open("your_option.txt", "w") as f:
		f.write("Blue Devi")


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

# Sound Path
sound_path = 'sounds'

# Meme path
imagesMeme_path = 'meme/images'
gifsMeme_path = 'meme/gifs'
gif_fps = 80

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
kick_delay = 300
kick_speed = 250
kick_sprites = [f'{kick_path}/kick1.png',f'{kick_path}/kick2.png',f'{kick_path}/kick3.png']

# Drag
dino_is_dragging = False

# Chase
chase_speed = 10
on_dumping_trash = False
current_chase_step = 0
max_chase_steps = 1000
haveJust_done = False

# Velocity of the Dino
walking_speed = 32 # in millisecond
running_speed = 18
walking_step = 2
running_step = 3

# Cursor
cursor_x = 0
set_cursor_x = True

cursor_speed = 6
cursor_step = 2

# Trolling Windows Image and Gif
default_images = {
	'threat.png': 'DARE DEVILLL',
	'skibidi.png': 'Sit on my face ;)',
	'giga_dino.png': 'A CHAD NEVER SKIP',
	'cat-pointing-laughing.png': 'JOKESONYOU >:DD',
	'nuts.png': 'Forever the Nuts',
	'assignments.png': 'Dino sincere message :3',
}

default_gifs = {
	'among_us_twerking.gif': 'SMELL DA SUXY ASS',
	'rick_roll.gif': 'Old. but Gold meme :)',
	'rick_roll_cry.gif': 'YOU CAN\'T STOP THE DINO',
}

default_memes = list(default_gifs.keys()) + list(default_images.keys())

gifs = []
images = []
trolling_windows = []

for gif in os.listdir(gifsMeme_path):
	if gif in list(default_gifs.keys()):
		gifs.append({
			"title": default_gifs[gif],
			"path": f'{gifsMeme_path}/{gif}',
			"replica": 0
		})
	else:
		gifs.append({
			"title": os.path.splitext(gif)[0],
			"path": f'{gifsMeme_path}/{gif}',
			"replica": 0
		})

for image in os.listdir(imagesMeme_path):
	if image in list(default_images.keys()):
		images.append({
			"title": default_images[image],
			"path": f'{imagesMeme_path}/{image}',
			"replica": 0
		})
	else:
		images.append({
			"title": os.path.splitext(image)[0],
			"path": f'{imagesMeme_path}/{image}',
			"replica": 0
		})

trolling_windows = gifs + images
random.shuffle(trolling_windows)


max_replica = 2