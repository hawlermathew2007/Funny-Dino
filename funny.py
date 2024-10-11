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

# Sprite
idle_index = 0
idle_time = 600
idle_sprite = ['image1','image2','image3','image4','image5']

speed = 8 # 100 millisecond
step = 2
sample = PhotoImage(file='dino.png')

desire_size = 45
scale = desire_size/sample.width()
img_width = int(sample.width() * scale)
img_height = int(sample.height() * scale)

initial_destination = [int(window.winfo_screenwidth()/2 - img_width - 150), int(window.winfo_screenheight()/2 - img_height - 100)]

image = Image.open("dino.png")
resize_image = image.resize((img_width, img_height))

dino = ImageTk.PhotoImage(resize_image)

x = -img_width
y = 100

window.geometry(f"{img_width}x{img_height}+{x}+{y}")
window.resizable(False, False)
window.attributes('-transparentcolor', 'gray')
window.wm_attributes("-topmost", True)
window.configure(background='gray')
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

def generate_destination():
	return [random.randint(0, window.winfo_screenwidth() - img_width), random.randint(0, window.winfo_screenheight() - img_height)]

def idle(coordination, destination):
	# change the image of the dino with sprite with the speed of 50 maybe
	# the duration of the idle should be random
	# at the end of the last image, the idle_time should randomly be extend to last longer.
	global idle_index

	print(idle_sprite[idle_index])
	print('The Dino is in Idle Mode')

	idle_index += 1
	
	if idle_index == len(idle_sprite):
		idle_index = 0
		window.after(speed, move, coordination, destination)
		return

	window.after(idle_time, idle, coordination, destination)


def move(coordination, destination): #coordination, destination

	global x
	global y
	
	x_relate = coordination[0] - destination[0]
	y_relate = coordination[1] - destination[1]

	# print("Relate: ", x_relate, y_relate)
	# print("Destination: ", destination)
	# print("---------------------------")
	# print("Coordination: ", coordination)
	# print("---------------------------")

	# the Dino when changing Direction much depend on x_relate only

	if x_relate > 0:
		x -= step
	else:
		x += step

	if y_relate > 0:
		y -= int(step * (random.random() + 1))
	else:
		y += int(step * (random.random() + 1))

	if (x >= destination[0] and x_relate <= 0) or (x <= destination[0] and x_relate > 0):
		x = destination[0]
	if (y >= destination[1] and y_relate <= 0) or (y <= destination[1] and y_relate > 0):
		y = destination[1]

	window.geometry(f"+{x}+{y}")

	coordination = [x, y]

	if coordination == destination:
		x = destination[0]
		y = destination[1]
		destination = generate_destination()
		idle(coordination, destination)
		return

	window.after(speed, move, coordination, destination)

def drag_window(event):
    window.geometry(f"+{int(event.x_root - img_width/2)}+{int(event.y_root - img_height/2)}")

keyboard.add_hotkey("shift+6", destroy_window)

label = Label(window, bg='gray', width=img_width, height=img_height, image= dino)
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