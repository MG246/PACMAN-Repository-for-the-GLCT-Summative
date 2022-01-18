from app_class import *
from pygame.locals import *

if __name__ == '__main__':
    app = App()
    app.run()

app.run = True
while app.run==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            app.run = False