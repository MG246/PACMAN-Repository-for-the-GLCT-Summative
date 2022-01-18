
from pygame.math import Vector2 as vec


# our screen settings
WIDTH, HEIGHT = 448, 596
FPS = 60
Top_Bottom_Buffer = 50
Maze_width,Maze_height = WIDTH - Top_Bottom_Buffer, HEIGHT - Top_Bottom_Buffer

ROWS = 30
COLS = 28

# our colour settings
BLACK = (0,0,0)
RED = (208, 22, 22)
WHITE = (107, 107, 107)
GREY = (255, 255, 255)
PLAYER_COLOUR = (190, 194, 15)
# font settings

START_TEXT_SIZE = 16
START_FONT = 'arial black'
Player_colour = (190, 194, 15) # colour of pacman check if correct
#player settings
Player_Starting_POS = vec(1,1)
# enemy settings
#font settings
