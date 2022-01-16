from pygame.math import Vector2 as vec

#screen settings
WIDTH, HEIGHT = 600, 800
Top_Bottom_Buffer = 50
Maze_width,Maze_height = WIDTH - Top_Bottom_Buffer, HEIGHT - Top_Bottom_Buffer

FPS = 60

ROWS = 30
COLS = 28

#colour settings more are to be added
Red = (208, 22, 22)
Black = (0, 0, 0)
White = (8,9,8)
   
Player_colour = (190, 194, 15) # colour of pacman check if correct
#player settings
#Player_Starting_POS = vec(1,1)

#font settings
Start_font = 'arial black'
