# importing the library
import pygame
import file_seeker as fs


# setup
main_window_size = fs.get_window_size()
main_window_title = fs.get_window_title()

# initialising the display
pygame.init()
screen = pygame.display.set_mode(main_window_size)
pygame.display.set_caption(main_window_title)

# icons to the title window can be added
window_icon = pygame.image.load('assets/bitmap.png')
pygame.display.set_icon(window_icon)

# background
bg = pygame.image.load('assets/bg.png')
bg = pygame.transform.scale(bg, main_window_size)

# fonts
font_show = pygame.font.Font('freesansbold.ttf', 32)
font_coord_x = 0
font_coord_y = 0

# player attributes
player_x = 100
player_y = 100
player_delta_x = 0
player_delta_y = 0
player_img = pygame.image.load('assets/player.png')


def show_font(x, y):
	font_display = font_show.render('X: ' + str(player_x) + ' Y: ' + str(player_y), True, (255, 255,255))
	screen.blit(font_display, (0,0))

def background_update():
	screen.blit(bg, (1,0))

def player_update(x, y):
	screen.blit(player_img, (x, y))

# while loop key
run_status = True

# game loop
while run_status == True:
	background_update()
	player_update(player_x, player_y)
	show_font(player_x, player_y)
	# will monitor all the events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run_status = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				print('left arrow pressed')
				player_delta_x = -1
			if event.key == pygame.K_RIGHT:
				print('right arrow pressed')
				player_delta_x = 1
			if event.key == pygame.K_UP:
				print('up arrow pressed')
				player_delta_y = -1
			if event.key == pygame.K_DOWN:
				print('down arrow pressed')
				player_delta_y = 1

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				print('left arrow released')
				player_delta_x = 0
			if event.key == pygame.K_RIGHT:
				print('right arrow released')
				player_delta_x = 0
			if event.key == pygame.K_UP:
				print('up arrow released')
				player_delta_y = 0
			if event.key == pygame.K_DOWN:
				print('down arrow released')
				player_delta_y = 0

	if 0>player_x:
		player_x = 0
	elif 645<player_x:
		player_x = 645
	else:
		player_x += player_delta_x
	if 0>player_y:
		player_y = 0
	elif 295<player_y:
		player_y = 295
	else:
		player_y += player_delta_y
	# display.fill((255,255,255))
	# background()
	pygame.display.update()