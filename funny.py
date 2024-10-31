from data import *

# Problems: the dino not being at the topmost when the child window appear and the child window can be close and drag by user 
# while the dino is locating it -> make the window cannot be minimized, focused and close [not let the user minimize the program]
# should I make the Dino always be focused or always be lift?

# Problem: set limit of meme review in the user screen. BTW, why the fuck the Dino is so buggy

if run_dino:
	window = Tk()
	window.title("Funny Dino")

	# Child Window
	childWindow_width_limitation = window.winfo_screenwidth()/4
	trolling_windows = [ # mostly meme :)) # This actually in the dict with title in a list
		{
			"title": 'DARE DEVILLL',
			"path": f'{imagesMeme_path}/threat.jpg',
			"replica": 0
		},
		{
			"title": 'Uhmm... Terrorist Jutsu',
			"path": f'{imagesMeme_path}/holy_damn.png',
			"replica": 0
		},
		{
			"title": 'SMELL DA SUXY ASS',
			"path": f'{gifsMeme_path}/among_us_twerking.gif',
			"replica": 0
		},
		{
			"title": 'Old. but Gold meme :)',
			"path": f'{gifsMeme_path}/rick_roll.gif',
			"replica": 0
		},
		{
			"title": 'MEOW MEOW, THE CAT CAN MEWWW',
			"path": f'{imagesMeme_path}/mewing_cat.jpeg',
			"replica": 0
		},
		{
			"title": 'Hmmm, insanitary meow meow rizz :D',
			"path": f'{imagesMeme_path}/pee_rizz.jpg',
			"replica": 0
		},
		{
			"title": 'Roblox Cat :]',
			"path": f'{imagesMeme_path}/rizz_cat.jfif',
			"replica": 0
		},
		{
			"title": 'Cat can Romantic Rizz (O-o)',
			"path": f'{imagesMeme_path}/dirty_rizz.jfif',
			"replica": 0
		},
		{
			"title": 'JOKESONYOU >:DD',
			"path": f'{imagesMeme_path}/cat-pointing-laughing.png',
			"replica": 0
		},
		{
			"title": 'JUST LOOKKK!!!',
			"path": f'{imagesMeme_path}/deez_nuts.jpg',
			"replica": 0
		},
		{
			"title": 'GYATTT',
			"path": f'{imagesMeme_path}/rizz.png',
			"replica": 0
		},
		{
			"title": 'Dirty Dino SOmeTiMes',
			"path": f'{imagesMeme_path}/villain_rizz.png',
			"replica": 0
		},
		{
			"title": 'YOU CAN\'T STOP THE DINO',
			"path": f'{gifsMeme_path}/rick_roll_cry.gif',
			"replica": 0
		},
		{
			"title": 'GYATT Trump Lecture',
			"path": f'{imagesMeme_path}/trump_mewing.jpg',
			"replica": 0
		},
		{
			"title": 'Your Bro\'s Face when hEAr YoUr jOkes',
			"path": f'{imagesMeme_path}/funny_dog.png',
			"replica": 0
		}
		# 'Your mom', 'CDs... CEE DEEZ NUT', 'The diffence between you and the door', 'You monkey'
	]
	max_replica = 2

	# Contain the trolling window that on User screen
	choosed_trolling_windowsWithGif = {}

	# Set Limit for number of child window
	current_numsOf_childWindow = 0
	max_numsOf_childWindow = 6

	# Value for Dino Size and Screen Resolution
	sample = PhotoImage(file=dino_path)
	# sample_shadow = PhotoImage(file=shadow_path)
	desire_size = 50
	scale = desire_size/sample.width()
	img_width = int(sample.width() * scale)
	img_height = int(sample.height() * scale)
	# shadow_width = img_width
	# shadow_height = int(sample_shadow.height() * scale)
	# print(shadow_width, shadow_height)

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

	# def add_shadow(speed):
		
	# 	global x
	# 	global y
	# 	global sub_label

	# 	sub_label.place(x=x, y=y+img_height+100)

	# 	print(sub_label.winfo_x(), sub_label.winfo_y())
	# 	window.after(speed, add_shadow, speed)


	def check_close_signal():
		while True:
			if os.path.exists("close_signal.txt"):
				os.remove("close_signal.txt")
				window.destroy()
				break
			time.sleep(0.5)  # Check every second


	def destroy_window():
		window.destroy()


	def findObj_via_title(title, do):
		for trolling_window in trolling_windows: # modify the replica if the meme is added
			if trolling_window['title'] == title:
				if do == 'add':
					trolling_window['replica'] += 1
				if do == 'subtract':
					trolling_window['replica'] -= 1
				if trolling_window['replica'] > max_replica:
					trolling_window['replica'] = max_replica
				print(trolling_window)


	def address_deletedWindow(title, troll_window):

		global current_numsOf_childWindow

		if not dino_is_dragging:
			print(f'This \'{title}\' window is closed')
			print('And the Dino gonna chase you!')
			current_numsOf_childWindow -= 1
			# create after_cancel(here)
			if str(troll_window) in choosed_trolling_windowsWithGif.keys():
				troll_window.after_cancel(choosed_trolling_windowsWithGif[str(troll_window)]['loop'])
				choosed_trolling_windowsWithGif.pop(str(troll_window))
			print('Current:', current_numsOf_childWindow)
			findObj_via_title(title, 'subtract')
			troll_window.destroy()# What if the user close too many times?


	def launch_trolling_window(title, image, x, y, frames, nums_frames):

		child_window = Toplevel(window)

		# will be working with the child window position and there will randomly be a big window in the mid LOL
		child_window.title(title)
		child_window.resizable(False, False)
		child_window.wm_attributes("-topmost", True)
		child_window.attributes("-toolwindow", True)

		# Create a label to display the image
		label = Label(child_window, image=image)
		label.image = image  # Keep a reference to avoid garbage collection
		label.pack()  # Pack the label to add it to the window
		
		child_window.geometry(f"+{int(x)}+{int(y)}")

		child_window.bind("<Button-1>", lambda e: None)
		child_window.bind("<B1-Motion>", lambda e: None)

		child_window.protocol("WM_DELETE_WINDOW", 
			lambda: address_deletedWindow(title, child_window)
		)

		findObj_via_title(title, 'add')
		
		# if gif then handle gif here
		if len(frames) > 0:
			animate_loop = child_window.after(50, lambda: animation_gif(child_window, label, frames, 1, nums_frames))
			choosed_trolling_windowsWithGif[str(child_window)] = { 'loop': animate_loop }

		return child_window


	def animation_gif(gif_window, gif_label, gif_frame, current_frame, nums_frames): # animation gif

		global choosed_trolling_windowsWithGif
		
		image = gif_frame[current_frame]

		gif_label.configure(image = image)
		current_frame += 1

		if current_frame == nums_frames:
			current_frame = 0 # reset the current_frame to 0 when end is reached

		choosed_trolling_windowsWithGif[str(gif_window)]['loop'] = gif_window.after(50, lambda: animation_gif(gif_window, gif_label, gif_frame, current_frame, nums_frames))


	def resizing_image_for_dino(path):

		global dino

		image = Image.open(path)

		if dino_is_flipped:
			image = image.transpose(Image.FLIP_LEFT_RIGHT)

		resize_image = image.resize((img_width, img_height))

		dino = ImageTk.PhotoImage(resize_image)

		return dino


	def resizing_image(path, width, height):
		return ImageTk.PhotoImage(Image.open(path).resize((width, height)))


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
		global dino_is_dragging
		global current_numsOf_childWindow

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

			print(choosing_action, dino_mode)

			if choosing_action == 1 and dino_mode == 'Devi' and current_numsOf_childWindow < max_numsOf_childWindow: # Only be activated in Devi mode #  

				filtered_window = list(filter(lambda window: window['replica'] < max_replica, trolling_windows))
				if len(filtered_window) == 0: # if all of the window alr reached max replica then just randomly choose all of them
					filtered_window = trolling_windows
				random_trollingWindow = random.choice(filtered_window) # use filter to filter out the duplicated meme
				random_trollingWindow_path = random_trollingWindow['path']
				
				meme = Image.open(random_trollingWindow_path)  # Update with your image path
				print('Meme image Size: ', meme.size)

				child_window_width, child_window_height = meme.size

				# check image size
				if child_window_height > childWindow_width_limitation:
					child_window_scale = childWindow_width_limitation/child_window_width
					child_window_width = child_window_width*child_window_scale
					child_window_height = child_window_height*child_window_scale

				# handle gif here
				photoimage_gifs = []
				frames = 0
				if '.gif' in random_trollingWindow_path:
					frames = meme.n_frames # number of frames
					for i in range(frames):
						meme.seek(i)
						resize_meme = meme.resize((int(child_window_width), int(child_window_height)), Image.LANCZOS)
						photoimage_gifs.append(ImageTk.PhotoImage(resize_meme))
					memeFR = photoimage_gifs[0]

				else:
					meme = meme.resize((int(child_window_width), int(child_window_height)))
					memeFR = ImageTk.PhotoImage(meme)


				child_window_x = random.choice([-child_window_width-img_width, window.winfo_screenwidth()+img_width])
				child_window_y = random.choice([window_gap, window.winfo_screenheight() - child_window_height - window_gap])

				print('Child Size: ', child_window_width, child_window_height)
				print('Child Coordination: ', child_window_x, child_window_y)

				dino_is_dragging = True

				drag_x = child_window_x
				drag_y = child_window_y + child_window_height/2 - img_height/2
				
				if child_window_x < window.winfo_screenwidth()/2:
					drag_x += child_window_width

				drag_destination = [drag_x, drag_y]
				troll_window = launch_trolling_window(random_trollingWindow['title'], memeFR, child_window_x, child_window_y, photoimage_gifs, frames)
				current_numsOf_childWindow += 1
				print('Current:', current_numsOf_childWindow)
				print('Troll Window ID:', troll_window)

				# window.after(running_speed, add_shadow, running_speed)
				window.after(running_speed, running, coordination, drag_destination, troll_window)

			else: # for Cute mode, but also for Devi if choosing action isn't 1
				# window.after(walking_speed, add_shadow, walking_speed)
				window.after(walking_speed, walking, coordination, destination)

			return

		# continue idle if havent done animation
		window.after(idle_time, idle, coordination, destination)


	def running(coordination, destination, target_window): # could need a type parameter like "chase" or "drag_meme"

		# have to work on the child window about "how to drag itself"

		global x
		global y
		global running_index
		global running_destination_queue
		global label
		global dino_is_flipped
		global dino_is_dragging

		# is created to know what the dino's direction
		x_relate = coordination[0] - destination[0]
		y_relate = coordination[1] - destination[1]

		# print("Destination: ", destination)
		# print("---------------------------")
		# print("Coordination: ", coordination)
		# print("---------------------------")

		# animation and running
		running_image = resizing_image_for_dino(running_sprites[running_index])

		if x_relate > 0:
			dino_is_flipped = True
			x -= running_step
		else:
			dino_is_flipped = False
			x += running_step

		if running_destination_queue == 1:
			dino_is_flipped = not dino_is_flipped

		if y_relate > 0:
			y -= int(running_step * (random.random() + 1))
		else:
			y += int(running_step * (random.random() + 1))

		label.config(image=running_image)

		running_index += 1

		# check if running cycle is finished then set it to be repeated
		if running_index >= len(running_sprites):
			running_index = 0

		# Let the Dino not to running out of destination
		if (x >= destination[0] and x_relate <= 0) or (x <= destination[0] and x_relate > 0):
			x = destination[0]
		if (y >= destination[1] and y_relate <= 0) or (y <= destination[1] and y_relate > 0):
			y = destination[1]

		window.geometry(f"+{int(x)}+{int(y)}")

		coordination = [x, y]

		# make the child window move if the dino reached the first destinaion
		if running_destination_queue == 1:
			# there is a touch between dino and window so add 10 to keep lil distance
			target_window_width = 0 + img_width
			if x < window.winfo_screenwidth()/2:
				target_window_width = -(target_window.winfo_width() + 10)
			target_window.geometry(f"+{int(x + target_window_width)}+{int(target_window.winfo_y())}")

		# if dino reached first destination then change to second destination with sprites be reversed
		# print("Compare Coordination and Destination: ",coordination, destination)
		if coordination == destination:
			# there is a touch between dino and window so add 10 to keep lil distance
			x = destination[0]
			y = destination[1]
			running_index = 0
			if running_destination_queue == 0:
				running_sprites.reverse()
				running_destination_queue = 1
				random_window_gap = int(window_gap * (random.random() + 1))
				drag_length = target_window.winfo_width()*2 + random_window_gap + img_width + 10
				if target_window.winfo_x() > window.winfo_screenwidth()/2:
					drag_length = -(target_window.winfo_width() + random_window_gap + img_width + 10)
				destination = [target_window.winfo_x() + drag_length, target_window.winfo_y() + target_window.winfo_height()/2 - img_height/2] # 'New Second Destination'
			else:
				window.wm_attributes("-topmost", True)
				window.lift()
				window.focus_force()
				running_sprites.reverse()
				running_destination_queue = 0
				dino_is_dragging = False
				target_window.unbind("<Button-1>")
				target_window.unbind("<B1-Motion>")
				destination = generate_destination()
				idle(coordination, destination)
				return

		# continue running
		window.after(running_speed, running, coordination, destination, target_window)


	def walking(coordination, destination): #coordination, destination

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

		# Let the Dino not to walking out of destination
		if (x >= destination[0] and x_relate <= 0) or (x <= destination[0] and x_relate > 0):
			x = destination[0]
		if (y >= destination[1] and y_relate <= 0) or (y <= destination[1] and y_relate > 0):
			y = destination[1]

		window.geometry(f"+{int(x)}+{int(y)}")

		coordination = [x, y]

		# walking to idle if destination is reached
		if coordination == destination:
			walking_index = 0
			x = destination[0]
			y = destination[1]
			destination = generate_destination()
			idle(coordination, destination)
			return

		# continue walking
		window.after(walking_speed, walking, coordination, destination)


	threading.Thread(target=check_close_signal, daemon=True).start()

	dino = resizing_image_for_dino(dino_path)
	# shadow = resizing_image(shadow_path, shadow_width, shadow_height)

	keyboard.add_hotkey("shift+6", destroy_window)

	window.bind('<Double-1>', lambda e: print('- You double-clicked the Dino'))

	# sub_label = Label(window, bg='black', width=shadow_width, height=shadow_height, image= shadow)
	# sub_label.image = shadow
	# sub_label.place(x=100, y=100, width=shadow_width, height=shadow_height)

	label = Label(window, bg='black', width=img_width, height=img_height, image= dino)
	label.place(x=0, y=0, width=img_width, height=img_height)

	walking([x, y], initial_destination) # should del initial_destination to generate_destination
	# add_shadow(walking_speed)

	window.mainloop()
 
# # Show the window
# def show():
# second.deiconify()
 
# # Hide the window
# def hide():
#     second.withdraw()
 
# def running(event):
#     window.geometry(f"+{int(event.x_root - img_width/2)}+{int(event.y_root - img_height/2)}")

# label.bind('<Button-1>', running)
# label.bind("<B1-Motion>", running)

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
