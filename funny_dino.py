from data import *

# There might be a new window for adjusting the dino size and adjust the sound that the dino cause
# Also I might need to add the shadow for dino lmao

current_after = None

with open("signal_activated.txt", "w") as f:
	f.write("Dino is activated")

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
desire_size = 55
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
window.iconphoto(True, PhotoImage(file='sprites/Blue/dino.png'))
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


def play_sound(file):
	pygame.mixer.music.load(f'{sound_path}/{file}')
	pygame.mixer.music.play(loops=0)
	pygame.mixer.music.set_volume(0.04)


def update_current_after(element):
	global current_after
	global startOf_idleDuplication
	global idle_sprites
	global idle_index
	global duplicated_sprites
	global running_index
	global running_destination_queue
	global dino_is_dragging
	global walking_index
	global haveJust_done

	if ouch_one or haveJust_done: # if the dino is hurt, reset all
		haveJust_done = False
		startOf_idleDuplication = True
		idle_sprites = [f'{idle_path}/idle1.png',f'{idle_path}/idle2.png',f'{idle_path}/idle3.png',f'{idle_path}/idle4.png']
		idle_index = 0
		duplicated_sprites = []
		running_index = 0
		running_destination_queue = 0
		dino_is_dragging = False
		walking_index = 0

	current_after = element


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


def move_cursor(x, y):
	pyautogui.moveTo(x, y)


def address_deletedWindow(title, troll_window):

	global current_numsOf_childWindow

	if not dino_is_dragging:
		# print(f'This \'{title}\' window is closed')
		# print('The Dino gonna chase and Kick yah!')
		current_chase_step = 0 # reset the current step to 0 when the user close another window
		current_numsOf_childWindow -= 1
		# create after_cancel(here)
		if str(troll_window) in choosed_trolling_windowsWithGif.keys():
			troll_window.after_cancel(choosed_trolling_windowsWithGif[str(troll_window)]['loop'])
			choosed_trolling_windowsWithGif.pop(str(troll_window))
		# print('Current:', current_numsOf_childWindow)
		findObj_via_title(title, 'subtract')
		coordination = [x, y]
		destination = list(pyautogui.position())
		window.after_cancel(current_after)
		update_current_after(window.after(running_speed, running, coordination, destination, None, "CHASE"))
		troll_window.destroy()# What if the user close too many times?
		return
		# make the Dino chase here


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

	choosed_trolling_windowsWithGif[str(gif_window)]['loop'] = gif_window.after(gif_fps, lambda: animation_gif(gif_window, gif_label, gif_frame, current_frame, nums_frames))


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


def ouch_response():
	window.after_cancel(current_after)
	if dino_mode == "Cute":
		# print("You hurt the Dino. How dare!")
		update_current_after(window.after(hurt_delay, hurt))

	if dino_mode == "Devi":
		# print('The Dino gonna punish u!')
		update_current_after(window.after(kick_delay, kick))


def hurt():
	# in the hurt mode play the hurt animation make the dino, then go to idle mode
	global hurt_index
	global ouch_one
	global label
	global destination

	# Problems occurs the dino is laggy and not switch to idle mode (Solution may be cancel the current "after")
	ouch_one = True
	hurt_image = resizing_image_for_dino(hurt_sprites[hurt_index])

	label.config(image=hurt_image)

	hurt_index += 1

	if hurt_index > len(hurt_sprites) - 1:
		hurt_index = 0
		ouch_one = False
		destination = generate_destination()
		update_current_after(window.after(idle_time, idle, [x, y], destination))
		return

	update_current_after(window.after(hurt_speed, hurt))


def kick(): # display kick animation here
	coordination = [x, y]
	destination = list(pyautogui.position())
	update_current_after(window.after(running_speed, running, coordination, destination, None, 'KICK'))


def kicking(coordination, destination, cursor_destination):
	# in the hurt mode play the hurt animation make the dino, then go to idle mode
	global kick_index
	global ouch_one
	global label

	# Problems occurs the dino is laggy and not switch to idle mode (Solution may be cancel the current "after")
	ouch_one = True
	dino_is_flipped = True
	kick_image = resizing_image_for_dino(kick_sprites[kick_index])

	label.config(image=kick_image)

	kick_index += 1

	cursor_coordination = list(pyautogui.position())
	cursor_x = cursor_coordination[0]
	cursor_x -= cursor_step

	move_cursor_thread = threading.Thread(target=move_cursor, args=(cursor_x, cursor_destination[1]), daemon=True)
	move_cursor_thread.start()

	if kick_index > len(kick_sprites) - 1:
		kick_index = len(kick_sprites) - 1
		# print(cursor_coordination)
		# print('Destination:', cursor_destination)
		if cursor_coordination == cursor_destination:
			kick_index = 0
			ouch_one = False
			destination = generate_destination()
			update_current_after(window.after(idle_time, idle, [x, y], destination))
			return
		update_current_after(window.after(cursor_speed, kicking, coordination, destination, cursor_destination))
		return

	update_current_after(window.after(kick_speed, kicking, coordination, destination, cursor_destination))


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
		duplicated_sprites = idle_sprites * random.randint(4, 6)
		startOf_idleDuplication = False

	idle_image = resizing_image_for_dino(duplicated_sprites[idle_index])

	label.config(image=idle_image)

	idle_index += 1
	# print(idle_index)
	
	# choose check if the animation is finished and decide to do devi action or continue wandering
	if idle_index >= len(duplicated_sprites):
		startOf_idleDuplication = True
		idle_sprites = [f'{idle_path}/idle1.png',f'{idle_path}/idle2.png',f'{idle_path}/idle3.png',f'{idle_path}/idle4.png']
		idle_index = 0
		duplicated_sprites = []
		choosing_action = random.randint(1,3)

		# print(choosing_action)

		if choosing_action == 1 and dino_mode == 'Devi' and current_numsOf_childWindow < max_numsOf_childWindow: # Only be activated in Devi mode #  

			filtered_window = list(filter(lambda window: window['replica'] < max_replica, trolling_windows))
			if len(filtered_window) == 0: # if all of the window alr reached max replica then just randomly choose all of them
				filtered_window = trolling_windows
			random_trollingWindow = random.choice(filtered_window) # use filter to filter out the duplicated meme
			random_trollingWindow_path = random_trollingWindow['path']
			
			meme = Image.open(random_trollingWindow_path)  # Update with your image path

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

			# print('Child Size: ', child_window_width, child_window_height)
			# print('Child Coordination: ', child_window_x, child_window_y)

			dino_is_dragging = True

			drag_x = child_window_x
			drag_y = child_window_y + child_window_height/2 - img_height/2
			
			if child_window_x < window.winfo_screenwidth()/2:
				drag_x += child_window_width

			drag_destination = [drag_x, drag_y]
			troll_window = launch_trolling_window(random_trollingWindow['title'], memeFR, child_window_x, child_window_y, photoimage_gifs, frames)
			current_numsOf_childWindow += 1
			# print('Current:', current_numsOf_childWindow)
			# print('Troll Window ID:', troll_window)

			# window.after(running_speed, add_shadow, running_speed)
			update_current_after(window.after(running_speed, running, coordination, drag_destination, troll_window, "DRAG"))

		else: # for Cute mode, but also for Devi if choosing action isn't 1
			# window.after(walking_speed, add_shadow, walking_speed)
			update_current_after(window.after(walking_speed, walking, coordination, destination))

		return

	# continue idle if havent done animation
	update_current_after(window.after(idle_time, idle, coordination, destination))


def running(coordination, destination, target_window, _type): # could need a type parameter like "chase" or "drag_meme"

	# have to work on the child window about "how to drag itself"

	global x
	global y
	global running_index
	global running_destination_queue
	global label
	global dino_is_flipped
	global dino_is_dragging
	global current_chase_step
	global on_dumping_trash

	# is created to know what the dino's direction
	x_relate = coordination[0] - destination[0]
	y_relate = coordination[1] - destination[1]

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

	play_sound('step.mp3')
	window.geometry(f"+{int(x)}+{int(y)}")

	coordination = [x, y]

	# The Dino Drag the Window
	# may need to fix the gap here
	if _type == "DRAG":
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
				update_current_after(window.after(10, idle, coordination, destination))
				return


	# should add a bool to prevent user clicking the dino and eventually collapse
	if _type == "CHASE": # Will trigger when the user close the window

		touch_mouth_range = 10 # this just simply let the cursor close to the dino mouth not the topleft or top right
		# chase the cursor here
		if not on_dumping_trash: # remember to adjust on_dumping_trash at the end
			current_chase_step += 1
			cursor_destination = list(pyautogui.position())
			actual_destination = [cursor_destination[0] + img_width, cursor_destination[1] - touch_mouth_range]
			hasReach = coordination == actual_destination

			# this 'if' is just make the program more rational (reach correctly)
			if not dino_is_flipped:
				actual_destination = [cursor_destination[0], cursor_destination[1] - touch_mouth_range]
				hasReach = coordination == actual_destination

			# decide continue to chase or not
			if hasReach:
				play_sound('bite.mp3')
				current_chase_step = 0
				trash_coordination = [0, window.winfo_screenheight()/2]
				on_dumping_trash = True
				update_current_after(window.after(chase_speed, running, coordination, trash_coordination, target_window, _type))
				return

			if current_chase_step > max_chase_steps:
				# print('Run out Step')
				current_chase_step = 0
				destination = generate_destination()
				update_current_after(window.after(idle_time, idle, coordination, destination))
				return

		# dragging the cursor to trash location here
		else:
			global haveJust_done
			move_cursor_thread = threading.Thread(target=move_cursor, args=(coordination[0], coordination[1] + touch_mouth_range), daemon=True)
			move_cursor_thread.start()
			# when the dino done dragging the cursor to trash
			if coordination == destination:
				haveJust_done = True
				on_dumping_trash = False
				new_destination = [80, destination[1]]
				update_current_after(window.after(walking_speed, walking, coordination, new_destination))
				return
			update_current_after(window.after(chase_speed, running, coordination, destination, None, _type))
			return
			
		update_current_after(window.after(chase_speed, running, coordination, actual_destination, None, _type))
		return


	if _type == "KICK": # Will trigger when the user double click the dino

		touch_mouth_range = 10 # this just simply let the cursor close to the dino mouth not the topleft or top right
		# chase the cursor here
		if not on_dumping_trash: # remember to adjust on_dumping_trash at the end
			current_chase_step += 1
			cursor_destination = list(pyautogui.position())
			actual_destination = [cursor_destination[0] + img_width, cursor_destination[1] - touch_mouth_range]
			hasReach = coordination == actual_destination

			# this 'if' is just make the program more rational (reach correctly)
			if not dino_is_flipped:
				actual_destination = [cursor_destination[0], cursor_destination[1] - touch_mouth_range]
				hasReach = coordination == actual_destination

			# decide continue to chase or not
			if hasReach:
				play_sound('bite.mp3')
				current_chase_step = 0
				trash_coordination = [window.winfo_screenwidth()/2 - img_width/2, window.winfo_screenheight()/2 - img_height/2]
				on_dumping_trash = True
				update_current_after(window.after(chase_speed, running, coordination, trash_coordination, target_window, _type))
				return

			if current_chase_step > max_chase_steps:
				# print('Run out Step')
				current_chase_step = 0
				destination = generate_destination()
				update_current_after(window.after(idle_time, idle, coordination, destination))
				return

		# dragging the cursor to trash location here
		else:
			move_cursor_thread = threading.Thread(target=move_cursor, args=(coordination[0], coordination[1] + touch_mouth_range), daemon=True)
			move_cursor_thread.start()
			# when the dino done dragging the cursor to trash
			if coordination == destination:
				haveJust_done = True
				on_dumping_trash = False
				cursor_trash_destination = [0, window.winfo_screenheight()/2]
				update_current_after(window.after(kick_delay, kicking, coordination, destination, cursor_trash_destination))
				return
			update_current_after(window.after(chase_speed, running, coordination, destination, None, _type))
			return
			
		update_current_after(window.after(chase_speed, running, coordination, actual_destination, None, _type))
		return


	# continue running
	update_current_after(window.after(running_speed, running, coordination, destination, target_window, _type))


def walking(coordination, destination): #coordination, destination

	global x
	global y
	global walking_index
	global label
	global dino_is_flipped

	# is created to know what the dino's direction
	x_relate = coordination[0] - destination[0]
	y_relate = coordination[1] - destination[1]

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

	play_sound('step.mp3')
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
	update_current_after(window.after(walking_speed, walking, coordination, destination))


thread_check_close_signal = threading.Thread(target=check_close_signal, daemon=True)
thread_check_close_signal.start()

dino = resizing_image_for_dino(dino_path)
# shadow = resizing_image(shadow_path, shadow_width, shadow_height)

keyboard.add_hotkey("shift+6", destroy_window)

window.bind('<Double-1>', lambda e: ouch_response() if not ouch_one or not dino_is_dragging else None)

# sub_label = Label(window, bg='black', width=shadow_width, height=shadow_height, image= shadow)
# sub_label.image = shadow
# sub_label.place(x=100, y=100, width=shadow_width, height=shadow_height)

label = Label(window, bg='black', width=img_width, height=img_height, image= dino)
label.place(x=0, y=0, width=img_width, height=img_height)

walking([x, y], initial_destination) # should del initial_destination to generate_destination
# add_shadow(walking_speed)

window.mainloop()

os.remove('signal_activated.txt')

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