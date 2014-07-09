#!/usr/bin/env python
"""
Ping - Tennis game one player
with score
For the Raspberry Pi
"""
import time                     # for delays
import os, pygame, sys
import random

pygame.init()                   # initilise graphics interface
pygame.mixer.quit()
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
bounceSound = pygame.mixer.Sound("/home/pi/Mikel/sounds/beep3.ogg")
os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'
pygame.display.set_caption("Ping 1 player")
screenWidth = 500
screenHeight =300
screen = pygame.display.set_mode([screenWidth,screenHeight],0,32)
background = pygame.Surface((screenWidth,screenHeight))
textSize = 36
scoreSurface = pygame.Surface((textSize,textSize))
font = pygame.font.Font(None, textSize)

# define the colours to use for the user interface
cBackground =(255,255,255)
cBall = (0,0,0)
background.fill(cBackground) # make background colour
cText = (0,0,0)
box = [screenWidth-10,screenHeight-10]
deltaChoice = [ [15,1], [14,1], [13,1], [12,1], [11,1], [10,1], [15,2], [14,2], [13,2], [12,2], [11,2], [10,2] ]
maxDelta = 11
delta = deltaChoice[random.randint(0,maxDelta)]
hw = screenWidth / 2
hh = screenHeight /2
ballPosition = [-hw,hh] # position of the ball  off screen
batMargin = 30 # how far in from the wall is the bat
batHeight = 24
batThick = 6
batInc = 20 # bat / key movement
batX = [batMargin, screenWidth - batMargin]
batY = [hh, hh] # initial bat position
limit = [0, 0, 0, 0, 0, 0] #wall limits & bat limits
ballRad = 8 # size of the ball
rally = True
pause = True
score = 0
best = 0  # high score
balls = 3 # number of balls in a turn
ballsLeft = balls

def main():
   global ballPosition, rally, balls, pause, score, best   
   updateBox(0,0) # set up wall limits
   updateScore()
   screen.blit(background,[0,0])
   while True :
     ballsLeft = balls
     if score > best:
        best = score
     score = 0
     updateScore()
     while ballsLeft > 0:
      ballPosition = waitForServe(ballPosition)
      while rally :
            checkForEvent()
            time.sleep(0.05)
            drawScreen(ballPosition)
            ballPosition = moveBall(ballPosition)
      ballsLeft -= 1
     print "press space for",balls,"more balls"
     pause = True
     while pause :
       checkForEvent()
     
      
def waitForServe(p) :
     global batY, rally, delta
     computerBatDelta = 2
     serveTime = time.time() + 2.0 #automatically serve again
     while time.time() < serveTime :
            checkForEvent()
            drawScreen(p)
            batY[0] += computerBatDelta # move bat up and down when waiting
            if batY[0] > limit[3] or batY[0] < limit[2]:
               computerBatDelta = -computerBatDelta
     p[0] = batX[0]
     p[1] = batY[0]
     delta = deltaChoice[random.randint(0,maxDelta)]
     rally = True
     return p

def moveBall(p):
    global delta, batY, rally, score, batThick
    p[0] += delta[0]
    p[1] += delta[1]
    # now test to any interaction
    if p[1] <= limit[2] : # test top
       bounceSound.play()
       delta[1] = - delta[1]
       p[1] = limit[2]
    elif p[1] >= limit[3] : # test bottom
       bounceSound.play()
       delta[1] = - delta[1] 
       p[1] = limit[3]
    elif p[0] <= limit[0] : # test missed ball player 1
       p[0] = limit[0]
       rally = False
       print " missed ball"
    elif p[0] >= limit[1] : # test missed ball player 2
       p[0] = limit[1]
       rally = False
       print " missed ball"
    # now test left bat limit
    elif p[0] <= limit[4] and p[1] >= batY[0] - ballRad and p[1] <= batY[0] + ballRad + batHeight:
       bounceSound.play()
       p[0] = limit[4]
       delta[0] = random.randint(5,15)
       if random.randint(1,4) > 2 : # random change in y direction 
          delta[1] = 16 - delta[0]
       else :
          delta[1] = -(16 - delta[0])
    # Test right bat collision      
    elif p[0] >= limit[5] and p[1] >= batY[1] - ballRad and p[1] <= batY[1] + ballRad + batHeight:
       bounceSound.play()
       delta[0] = - delta[0]
       p[0] = limit[5]
       score+= 1
       updateScore()
    batY[0] = p[1] - ballRad # make auto opponent follow bat
    #batY[1] = p[1]- ballRad # temporary test for auto player
    return p
   
def updateScore():
    global score, best, scoreRect, scoreSurface
    scoreSurface = font.render(str(best)+" : "+str(score), True, cText, cBackground)
    scoreRect = scoreSurface.get_rect()
    scoreRect.centerx = hw
    scoreRect.centery = 24
    
def drawScreen(p) : # draw to the screen
    global rally
    screen.blit(background,[0,0]) # set background colour
    pygame.draw.rect(screen,(255,0,0), (hw - (box[0]/2),hh - (box[1]/2),box[0],box[1]), 4)
    pygame.draw.line(screen,(0,255,0), (batX[0], batY[0]),(batX[0], batY[0]+batHeight),batThick)
    pygame.draw.line(screen,(0,255,0), (batX[1], batY[1]),(batX[1], batY[1]+batHeight),batThick)
    screen.blit(scoreSurface, scoreRect)
    if rally :
        pygame.draw.circle(screen,cBall, (p[0], p[1]),ballRad, 2)
    pygame.display.update()

def updateBox(d,amount):
    global box, limit
    box[d] += amount    
    limit[0] = hw - (box[0]/2) +ballRad #leftLimit
    limit[1] = hw + (box[0]/2) -ballRad #rightLimit
    limit[2] = hh - (box[1]/2) + ballRad #topLimit
    limit[3] = (hh + (box[1]/2))-ballRad #bottomLimit
    limit[4] = batX[0] + ballRad + batThick/2 #x Limit ball approaching from the right
    limit[5] = batX[1] - ballRad - batThick/2  #x Limit ball approaching from the left
         
def terminate(): # close down the program
    print ("Closing down please wait")
    pygame.quit() # close pygame
    sys.exit()

batmoving = False
    
def checkForEvent(): # see if we need to quit
    global batY, rally, pause, batmoving
    event = pygame.event.poll()
    if event.type == pygame.QUIT :
           terminate()
    if event.type == pygame.KEYDOWN :            
       if event.key == pygame.K_ESCAPE :
           terminate()
       if event.key == pygame.K_DOWN : # expand / contract the box
            updateBox(1,-2)
       if event.key == pygame.K_UP :
            updateBox(1,2)
       if event.key == pygame.K_LEFT :
            updateBox(0,-2)
       if event.key == pygame.K_RIGHT :
            updateBox(0,2)
       if event.key == pygame.K_s :
            rally = True
       if event.key == pygame.K_SPACE :
            pause = False
       if event.key == pygame.K_PAGEDOWN :          
            batmoving = True #added
            while batmoving: #added
                time.sleep(0.1)
                if batY[1] < screenHeight - batInc:
                    batY[1] += batInc                
                checkForEvent()  #added               
       if event.key == pygame.K_PAGEUP :
            batmoving = True #added
            while batmoving: #added
               time.sleep(0.1)
               if batY[1] > batInc :
                  batY[1] -= batInc
               checkForEvent()#added                
    if event.type == pygame.KEYUP:
        #print "KEYUP event triggered!" #added
        batmoving = False
##        if event.key == pygame.K_PAGEDOWN :
##          if batmoving == True: #added
##             batmoving = False #added
##             #print "Pagedown key up"
##        if event.key == pygame.K_PAGEUP :
##          if batmoving == True: #added
##             batmoving = False #added
##             #print "Page UP key up"
            
if __name__ == '__main__':
    main()   
