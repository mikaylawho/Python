#!/user/bin/env python
"""
Bounce
A Raspberry Pi test
"""

import time
import os, pygame, sys

pygame.init()
os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'
pygame.display.set_caption("Bounce")
screenWidth = 400
screenHeight = 400
screen = pygame.display.set_mode([screenWidth, screenHeight],0,32)
background = pygame.Surface((screenWidth, screenHeight))

#define user interface colors
cBackground = (255,255,255)
cBlock = (0,0,0)
background.fill(cBackground)
dx = 5
dy = 10

def main():
    X = screenWidth / 2
    Y = screenHeight / 2
    screen.blit(background,[0,0])
    while True:
        checkForEvent()
        time.sleep(0.1)
        drawScreen(X,Y)
        X += dx
        Y += dy
        checkBounds(X,Y)

def checkBounds(px,py):
    global dx,dy
    if px > screenWidth - 10 or px < 0:
        dx = -dx
    if py > screenHeight - 10 or py < 0:
        dy = -dy

def drawScreen(px,py):
    screen.blit(background,[0,0])
    #I *think* 10px is the highth and width of the block.
    #This is why there is "- 10" in calculations for "checkBounds"
    pygame.draw.rect(screen,cBlock,(px,py,10,10),0)
    pygame.display.update()

def terminate():
    print("Closing down, please wait.")
    pygame.quit()
    sys.exit()

def checkForEvent():
    event = pygame.event.poll()
    if event.type == pygame.QUIT :
        terminate()
    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        terminate()

if __name__ == '__main__':
    main()
    
        
