from tkinter import *
from PIL import Image, ImageTk
import keyboard
import random

# Note: must 4 directions, separate to 2 groups: West & East and South & North || Create Destination (!= current dino coordination); 
# Must Reckon Limitation First (with the prerequisite: 300 pixels away dino and 500 pixels move maximum 
# -> Must go to situation that have to determine the directions first bcuz
# the dino may be close to the computer screen side)
# Stage 1: Must Locate the Dino first -> Decide the direction || random the direction via Limitation and Minimum Distance
# Stage 2: From the nums of Direction decide Destination
# Stage 3: Modify the Dino speed and Create movement

window = Tk()
window.title("Funny Dino")

# Path

type_of_Dino = 'Blue'

dino_path = f'sprites/{type_of_Dino}/dino.png'
idle_path = f'sprites/{type_of_Dino}/Idle'
walking_path = f'sprites/{type_of_Dino}/Walking'

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

# Velocity of the Dino
speed = 50 # 100 millisecond
step = 2

# Value for Dino Size and Screen Resolution
sample = PhotoImage(file=dino_path)
desire_size = 50
scale = desire_size/sample.width()
img_width = int(sample.width() * scale)
img_height = int(sample.height() * scale)

initial_destination = [int(window.winfo_screenwidth()/2 - img_width - 150), int(window.winfo_screenheight()/2 - img_height - 100)]

x = -img_width
y = 100

window.geometry(f"{img_width}x{img_height}+{x}+{y}")
window.resizable(False, False)
window.attributes('-transparentcolor', 'black')
window.wm_attributes("-topmost", True)
window.configure(background='black')
window.overrideredirect(True)

class Protangonist():
	pass


class Object():
	def __init__(self, state):
		super.__init__()
		self.state = state # falling, staying

	def update(self):
		pass


class Window(): # created by thing funny thing it could be funny or sacrasm
	pass


def destroy_window():
	window.destroy()


def resizing_image(path):

	global dino

	image = Image.open(path)

	if dino_is_flipped:
		image = image.transpose(Image.FLIP_LEFT_RIGHT)

	resize_image = image.resize((img_width, img_height))

	dino = ImageTk.PhotoImage(resize_image)

	return dino


def generate_destination():
	return [random.randint(0, window.winfo_screenwidth() - img_width), random.randint(0, window.winfo_screenheight() - img_height)]


def idle(coordination, destination):
	# change the image of the dino with sprite with the speed of 50 maybe
	# the duration of the idle should be random
	# at the end of the last image, the idle_time should randomly be extend to last longer.
	global idle_index
	global idle_sprites
	global label
	global duplicated_sprites
	global startOf_idleDuplication

	if startOf_idleDuplication:
		duplicated_sprites = idle_sprites * random.randint(3, 6)
		startOf_idleDuplication = False

	idle_image = resizing_image(duplicated_sprites[idle_index])

	label.config(image=idle_image)

	idle_index += 1
	
	if idle_index >= len(duplicated_sprites):
		startOf_idleDuplication = True
		idle_sprites = [f'{idle_path}/idle1.png',f'{idle_path}/idle2.png',f'{idle_path}/idle3.png',f'{idle_path}/idle4.png']
		idle_index = 0
		duplicated_sprites = []
		window.after(speed, move, coordination, destination)
		return

	window.after(idle_time, idle, coordination, destination)


def move(coordination, destination): #coordination, destination

	global x
	global y
	global walking_index
	global label
	global dino_is_flipped

	x_relate = coordination[0] - destination[0]
	y_relate = coordination[1] - destination[1]

	# print("Relate: ", x_relate, y_relate)
	# print("Destination: ", destination)
	# print("---------------------------")
	# print("Coordination: ", coordination)
	# print("---------------------------")

	# the Dino when changing Direction much depend on x_relate only

	walking_image = resizing_image(walking_sprites[walking_index])

	if x_relate > 0:
		dino_is_flipped = True
		x -= step
	else:
		dino_is_flipped = False
		x += step

	if y_relate > 0:
		y -= int(step * (random.random() + 1))
	else:
		y += int(step * (random.random() + 1))

	label.config(image=walking_image)

	walking_index += 1

	if walking_index >= len(walking_sprites):
		walking_index = 0

	# Let the Dino not to move out of destination
	if (x >= destination[0] and x_relate <= 0) or (x <= destination[0] and x_relate > 0):
		x = destination[0]
	if (y >= destination[1] and y_relate <= 0) or (y <= destination[1] and y_relate > 0):
		y = destination[1]

	window.geometry(f"+{x}+{y}")

	coordination = [x, y]

	if coordination == destination:
		walking_index = 0
		x = destination[0]
		y = destination[1]
		destination = generate_destination()
		idle(coordination, destination)
		return

	window.after(speed, move, coordination, destination)


def drag_window(event):
    window.geometry(f"+{int(event.x_root - img_width/2)}+{int(event.y_root - img_height/2)}")

dino = resizing_image(dino_path)

keyboard.add_hotkey("shift+6", destroy_window)

label = Label(window, bg='black', width=img_width, height=img_height, image= dino)
label.place(x=0, y=0, width=img_width, height=img_height)
label.bind('<Button-1>', drag_window)
label.bind("<B1-Motion>", drag_window)

move([x, y], initial_destination) # should del initial_destination to generate_destination

window.mainloop()


# # Open New Window
# def launch():
#     global second
#     second = Toplevel()
#     second.title("Child Window")
#     second.geometry("400x400")
 
# # Show the window
# def show():
#     second.deiconify()
 
# # Hide the window
# def hide():
#     second.withdraw()
 
# # Add Buttons
# Button(window, text="launch Window", command=launch).pack(pady=10)
# Button(window, text="Show", command=show).pack(pady=10)
# Button(window, text="Hide", command=hide).pack(pady=10)
# cute dino: has angry mode (when user approach the close dino button or close the tab), get hurt version
# smirking[evil] version (occurs when it poop or drag a sarcastic note) and falling baby
# cute dino must have sound lol
# must have random idle