# Just Simply the Gap between the dino and the window side to make it look natural
window_gap = 80

# About Dino Path
type_of_Dino = 'Blue'
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

