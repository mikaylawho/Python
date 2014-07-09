#!/usr/bin/env python
"""
Bounce with sound
A Raspberry Pi Test
"""

import time
import os, pygame, sys

pygame.init()
pygame.mixer.quit()
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
bounceSound = pygame.mixer.Sound('/home/pi/Mikel/sounds/beep3.ogg')
os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'
pygame.display.set_caption("Bounce2")
screenWidth = 400
screenHeight = 400
screen = pygame.display.set_mode([screenWidth, screenHeight],0,32)
background = pygame.Surface((screenWidth, screenHeight))

#define user interface colors
cBackground = (255,255,255)
cBlock = (0,0,0)
background.fill(cBackground)
box = [screenWidth - 80, screenHeight - 80]
delta = [5,10]
hw = screenWidth / 2
hh = screenHeight / 2
position = [hw,hh]
limit = [0,0,0,0]
ballRad = 8

def main():
    global position
    updateBox(0,0)
    screen.blit(background, [0,0])
    while True :
        checkForEvent()
        time.sleep(0.05)
        drawScreen(position)
        position = moveBall(position)

def drawScreen(p):
    screen.blit(background,[0,0])
    pygame.draw.rect(screen, (255,0,0), (hw - (box[0]/2), hh - (box[1]/2), box[0],
                                         box[1]), 2)
    pygame.draw.circle(screen, cBlock, (p[0], p[1]), ballRad, 2 )
    pygame.display.update()

def moveBall(p):
    global delta
    p[0] += delta[0]
    p[1] += delta[1]
    if p[0] <= limit[0]:
        bounceSound.play()
        delta[0] = -delta[0]
        p[0] = limit[0]
    if p[0] >= limit[1]:
        bounceSound.play()
        delta[0] = -delta[0]
        p[0] = limit[1]
    if p[1] <= limit[2]:
        bounceSound.play()
        delta[1] = -delta[1]
        p[1] = limit[2]
    if p[1] >= limit[3]:
        bounceSound.play()
        delta[1] = -delta[1]
        p[1] = limit[3]
    return p

def updateBox(d, amount):
    global box,limit
    box[d] += amount
    limit[0] = hw - (box[0]/2) + ballRad
    limit[1] = hw + (box[0]/2) - ballRad
    limit[2] = hh - (box[1]/2) + ballRad
    limit[3] = hh + (box[1]/2) - ballRad

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
    #expand / contract the box
    if event.type == pygame.K_DOWN:
        updateBox(1,-2)
    if event.type == pygame.K_UP:
        updateBox(1,2)
    if event.type == pygame.K_LEFT:
        updateBox(0,-2)
    if event.type == pygame.K_RIGHT:
        updateBox(0,2)

if __name__ == '__main__':
    main()
    
        
    
        
    
    
