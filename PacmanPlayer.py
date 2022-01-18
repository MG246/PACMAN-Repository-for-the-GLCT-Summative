# Go back to the settings file too make a change in the player settings
import pygame
from settings import *
vec = pygame.math.Vector2 


class Player:
    def __init__(self,app,pos):
        self.grid_pos = pos
        self.app = app 
        self.starting_pos = [pos.x, pos.y]
        self. pix_pos = self.get_pix_pos()
        self.direction = vec(1,0)
        self.stored_direction = None
        self.able_to_move = True
        self.current_score = 0
        self.speed = 2
        self.lives = 1

    def update(self): #my update function
        if self.able_to_move:
            self.pix_pos += self.direction*self.speed
        if self.time_to_move():
            if self.stored_direction != None:
                self.direction = self.stored_direction
            self.able_to_move = self.can_move()
        # Setting grid position in reference to pix pos
        self.grid_pos[0] = (self.pix_pos[0]-Top_Bottom_Buffer +
                            self.app.cell_width//2)//self.app.cell_width+1
        self.grid_pos[1] = (self.pix_pos[1]-Top_Bottom_Buffer +
                            self.app.cell_height//2)//self.app.cell_height+1
        if self.on_coin():
            self.eat_coin()
            
        

    def draw(self): 
        # my pacman circle function
        pygame.draw.circle(self.app.screen, PLAYER_COLOUR, (int(self.pix_pos.x),
                                                            int(self.pix_pos.y)), self.app.cell_width//2-2)
        # drawing the grid position rectangle
        #pygame.draw.rect(self.app.screen, Red, (self.grid_pos[0]*self.app.cell_width - Top_Bottom_Buffer//2, self.grid_pos[1] * self.app.cell_height - Top_Bottom_Buffer//2, self.app.cell.width, self.app.cell_height), 1)
        for x in range(self.lives):
            pygame.draw.circle(self.app.screen, PLAYER_COLOUR, (30 + 20*x, HEIGHT - 15), 7)

    def on_coin(self):
        if self.grid_pos in self.app.coins:
            if int(self.pix_pos.x+Top_Bottom_Buffer//2) % self.app.cell_width == 0:
                if self.direction == vec(1, 0) or self.direction == vec(-1, 0) or self.direction == vec(0, 0):
                    return True
            if int(self.pix_pos.y+Top_Bottom_Buffer//2) % self.app.cell_height == 0:
                if self.direction == vec(0, 1) or self.direction == vec(0, -1) or self.direction == vec(0, 0):
                    return True
            return False
                  
    def eat_coin(self):
         self.app.coins.remove(self.gid_pos)
         self.current_score += 1
    def move(self,direction):#my move function
        self.stored_direction = direction

    def get_pix_pos(self):
        return vec((self.grid_pos[0]*self.app.cell_width)+Top_Bottom_Buffer//2+self.app.cell_width//2,
                   (self.grid_pos[1]*self.app.cell_height) +
                   Top_Bottom_Buffer//2+self.app.cell_height//2)

        print(self.grid_pos, self.pix_pos)
        
    def time_to_move(self):
        if int(self.pix_pos.x+Top_Bottom_Buffer//2) % self.app.cell_width == 0:
            if self.direction == vec(1, 0) or self.direction == vec(-1, 0) or self.direction == vec(0, 0):
                return True
        if int(self.pix_pos.y+Top_Bottom_Buffer//2) % self.app.cell_height == 0:
            if self.direction == vec(0, 1) or self.direction == vec(0, -1) or self.direction == vec(0, 0):
                return True

    def can_move(self):
        for wall in self.app.walls:
            if vec(self.grid_pos+self.direction) == wall:
                return False
        return True
