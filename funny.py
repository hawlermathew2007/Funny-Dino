from tkinter import *
from PIL import Image, ImageTk
import keyboard
import random
import threading
import os
import time
from data import *

window = Tk()
window.title("Funny Dino")

dino_mode = 'Devi' # Cute or Devi # Cute mode may distribute to cute wanderer or cute with actions

# Child Window
childWindow_width_limitation = window.winfo_screenwidth()/4
trolling_windows = [ # mostly meme :)) # This actually in the dict with title in a list
	{
		"title": 'DARE DEVILLL',
		"image_path": f'{imagesMeme_path}/threat.jpg'
	},
	{
		"title": 'Uhmm... Terrorist Jutsu',
		"image_path": f'{imagesMeme_path}/holy_damn.png'
	},
	{
		"title": 'MEOW MEOW, THE CAT CAN MEWWW',
		"image_path": f'{imagesMeme_path}/mewing_cat.jpeg'
	},
	{
		"title": 'GYATT Trump Lecture',
		"image_path": f'{imagesMeme_path}/trump_mewing.jpg'
	},
	{
		"title": 'Your Bro\'s Face when hEAr YoUr jOkes',
		"image_path": f'{imagesMeme_path}/funny_dog.png'
	}
	# 'Your mom', 'CDs... CEE DEEZ NUT', 'The diffence between you and the door', 'You monkey'
]

# Value for Dino Size and Screen Resolution
sample = PhotoImage(file=dino_path)
desire_size = 50
scale = desire_size/sample.width()
img_width = int(sample.width() * scale)
img_height = int(sample.height() * scale)

x = -img_width
y = 100

initial_destination = [int(window.winfo_screenwidth()/2 - img_width - 200), int(window.winfo_screenheight()/2 - img_height - 100)]


# Configure Main Window (The Dino duh)
window.geometry(f"{img_width}x{img_height}+{x}+{y}")
window.resizable(False, False)
window.attributes('-transparentcolor', 'black')
window.wm_attributes("-topmost", True)
window.configure(background='black')
window.overrideredirect(True)


def check_close_signal():
	while True:
		if os.path.exists("close_signal.txt"):
			os.remove("close_signal.txt")
			window.destroy()
			break
		time.sleep(0.5)  # Check every second


def destroy_window():
	window.destroy()


def address_deletedWindow(title, troll_window):
	print(f'This \'{title}\' window is closed')
	print('And the Dino gonna chase you!')
	troll_window.destroy()# What if the user close too many times?


def launch_trolling_window(title, image, x, y):

	child_window = Toplevel(window)

	# will be working with the child window position and there will randomly be a big window in the mid LOL
	child_window.title(title)
	child_window.resizable(False, False)
	child_window.wm_attributes("-topmost", True)

	# Create a label to display the image
	label = Label(child_window, image=image)
	label.image = image  # Keep a reference to avoid garbage collection
	label.pack()  # Pack the label to add it to the window
	
	child_window.geometry(f"+{int(x)}+{int(y)}")

	child_window.protocol("WM_DELETE_WINDOW", 
		lambda: address_deletedWindow(title, child_window)
	)

	return child_window


def resizing_image_for_dino(path):

	global dino

	image = Image.open(path)

	if dino_is_flipped:
		image = image.transpose(Image.FLIP_LEFT_RIGHT)

	resize_image = image.resize((img_width, img_height))

	dino = ImageTk.PhotoImage(resize_image)

	return dino


def generate_destination():
	return [random.randint(window_gap, window.winfo_screenwidth() - img_width - window_gap), random.randint(window_gap, window.winfo_screenheight() - img_height - window_gap)]


def idle(coordination, destination):
	# change the image of the dino with sprite with the walking_speed of 50 maybe
	# the duration of the idle should be random
	# at the end of the last image, the idle_time should randomly be extend to last longer.
	global idle_index
	global idle_sprites
	global label
	global duplicated_sprites
	global startOf_idleDuplication

	# animation
	if startOf_idleDuplication:
		duplicated_sprites = idle_sprites * random.randint(3, 6)
		startOf_idleDuplication = False

	idle_image = resizing_image_for_dino(duplicated_sprites[idle_index])

	label.config(image=idle_image)

	idle_index += 1
	
	# choose check if the animation is finished and decide to do devi action or continue wandering
	if idle_index >= len(duplicated_sprites):
		startOf_idleDuplication = True
		idle_sprites = [f'{idle_path}/idle1.png',f'{idle_path}/idle2.png',f'{idle_path}/idle3.png',f'{idle_path}/idle4.png']
		idle_index = 0
		duplicated_sprites = []
		choosing_action = random.randint(1,3)

		print(choosing_action)

		if choosing_action == 1 and dino_mode == 'Devi': # Only be activated in Devi mode

			random_trollingWindow = random.choice(trolling_windows)
			print('The choosed Image: ', random_trollingWindow)
			
			meme_img = Image.open(random_trollingWindow['image_path'])  # Update with your image path
			print('Meme image Size: ', meme_img.size)

			child_window_width, child_window_height = meme_img.size

			# check image size
			print('Compare height and Limit:', child_window_height, childWindow_width_limitation)
			if child_window_height > childWindow_width_limitation:
				print('Window is resizing')
				child_window_scale = childWindow_width_limitation/child_window_width
				child_window_width = childWindow_width_limitation
				child_window_height = child_window_height*child_window_scale
				meme_img = meme_img.resize((int(child_window_width), int(child_window_height)))

			memeFR = ImageTk.PhotoImage(meme_img)

			child_window_x = random.choice([-child_window_width + 300, window.winfo_screenwidth() - 300])
			child_window_y = random.choice([window_gap, window.winfo_screenheight() - child_window_height - window_gap])

			drag_destination = [child_window_x, child_window_y + child_window_height/2 - img_height/2]
			troll_window = launch_trolling_window(random_trollingWindow['title'], memeFR, child_window_x, child_window_y)

			# window.after(running_speed, drag_window, coordination, drag_destination, troll_window)
			window.after(walking_speed, move, coordination, destination)

		else:
			window.after(walking_speed, move, coordination, destination)

		return

	# continue idle if havent done animation
	window.after(idle_time, idle, coordination, destination)


def drag_window(coordination, destination):
	# will have first destination with normal running
	# and second destination with reverse running
	# if second destination reached move to idle
	pass


def move(coordination, destination): #coordination, destination

	global x
	global y
	global walking_index
	global label
	global dino_is_flipped

	# is created to know what the dino's direction
	x_relate = coordination[0] - destination[0]
	y_relate = coordination[1] - destination[1]

	# print("Destination: ", destination)
	# print("---------------------------")
	# print("Coordination: ", coordination)
	# print("---------------------------")

	# animation and walking
	walking_image = resizing_image_for_dino(walking_sprites[walking_index])

	if x_relate > 0:
		dino_is_flipped = True
		x -= walking_step
	else:
		dino_is_flipped = False
		x += walking_step

	if y_relate > 0:
		y -= int(walking_step * (random.random() + 1))
	else:
		y += int(walking_step * (random.random() + 1))

	label.config(image=walking_image)

	walking_index += 1

	# check if walking cycle is finished then set it to be repeated
	if walking_index >= len(walking_sprites):
		walking_index = 0

	# Let the Dino not to move out of destination
	if (x >= destination[0] and x_relate <= 0) or (x <= destination[0] and x_relate > 0):
		x = destination[0]
	if (y >= destination[1] and y_relate <= 0) or (y <= destination[1] and y_relate > 0):
		y = destination[1]

	window.geometry(f"+{x}+{y}")

	coordination = [x, y]

	# move to idle if destination is reached
	if coordination == destination:
		walking_index = 0
		x = destination[0]
		y = destination[1]
		destination = generate_destination()
		idle(coordination, destination)
		return

	# continue walking
	window.after(walking_speed, move, coordination, destination)


threading.Thread(target=check_close_signal, daemon=True).start()

dino = resizing_image_for_dino(dino_path)

keyboard.add_hotkey("shift+6", destroy_window)

label = Label(window, bg='black', width=img_width, height=img_height, image= dino)
label.place(x=0, y=0, width=img_width, height=img_height)


move([x, y], initial_destination) # should del initial_destination to generate_destination

window.mainloop()
 
# # Show the window
# def show():
# second.deiconify()
 
# # Hide the window
# def hide():
#     second.withdraw()
 
# def drag_window(event):
#     window.geometry(f"+{int(event.x_root - img_width/2)}+{int(event.y_root - img_height/2)}")

# label.bind('<Button-1>', drag_window)
# label.bind("<B1-Motion>", drag_window)

# cute dino: has angry mode (when user approach the close dino button or close the tab), get hurt version
# smirking[evil] version (occurs when it poop or drag a sarcastic note) and falling baby
# cute dino must have sound lol
# must have random idle

# Note: must 4 directions, separate to 2 groups: West & East and South & North || Create Destination (!= current dino coordination); 
# Must Reckon Limitation First (with the prerequisite: 300 pixels away dino and 500 pixels move maximum 
# -> Must go to situation that have to determine the directions first bcuz
# the dino may be close to the computer screen side)
# Stage 1: Must Locate the Dino first -> Decide the direction || random the direction via Limitation and Minimum Distance
# Stage 2: From the nums of Direction decide Destination
# Stage 3: Modify the Dino walking_speed and Create movement
# Add Cute mode and Devi mode (the dino will randomly drag the user cursor or drag sarcastic window LOL)

# There should be a random here to decide to use the big window in the mid or small window # kinda time consuming so yeah

# Future problems
# when the user close the window while dino dragging, will the program crash?
# or when the user close the window will the dino crash when even in idle mode or walking? Cuz it might interrupt the window.after func
