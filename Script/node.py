import pygame
import random
import math
from Source import WIDTH,speed

circle_img = pygame.image.load('./image/ball.png')
rains_img = pygame.image.load('./image/raintap.png')
long_ball_img = pygame.image.load('./image/long.png')
long_ball_up = pygame.image.load('./image/longup.png')
long_ball_down = pygame.image.load('./image/longdown.png')
Fifty = 50/1536*WIDTH
Thirty = 30/1536*WIDTH

class Ball:
    def __init__(self,x, y,color,test_y):
        self.x = x
        self.y = y
        self.speed = speed
        self.color = color
        self.length = 10/1536*WIDTH
        self.test_y = test_y
        self.img = pygame.transform.scale(circle_img, (Fifty, Fifty))


    def draw(self,window):

        window.blit(self.img,(self.x,self.y))

        # position = self.test_y//10
        
        # for i in range(10):
        #     pygame.draw.line(window,(255,255,255),(self.x+25, i*position),(self.x + 25, (i+1)*position-10), 2)
    
        # 画框
        pygame.draw.circle(window,(255,255,255),(self.x+Fifty/2, self.test_y+Fifty/2), Fifty/2, 4)

    def update(self):
        self.y += self.speed

    def test(self):
        if abs(self.y-self.test_y)<=20:
            return 1
        elif abs(self.y-self.test_y)<=40:
            return 2
        else:
            return 0
        
class LONGBALL:
    def __init__(self,x, y,color,length,test_y):
        self.x = x
        self.y = y
        self.speed = speed
        self.color = color
        self.length = length
        self.test_y = test_y
        self.win = False
        self.img = pygame.transform.scale(long_ball_img, (Fifty, self.length))
        self.img_up = pygame.transform.scale(long_ball_up, (Fifty, Fifty/2))
        self.img_down = pygame.transform.scale(long_ball_down, (Fifty, Fifty/2))
        self.start = False
        self.isdie = False
        self.count = 0 
        
    def draw(self,window):
        window.blit(self.img_up,(self.x,self.y-Fifty/2))
        window.blit(self.img,(self.x,self.y))
        window.blit(self.img_down,(self.x,self.y+self.length))
        pygame.draw.circle(window,(255,255,255),(self.x+Fifty/2, self.test_y+Fifty/2), Fifty/2, 4)
    

    def update(self):
        self.y += self.speed
        if self.y + self.length >= self.test_y + Fifty/2:
            if self.test_y - self.y + Fifty/2> 0:
                self.img = pygame.transform.scale(long_ball_img, (Fifty, self.test_y - self.y + Fifty/2))
                self.length = self.test_y - self.y + Fifty/2
        
    def test(self):
        if abs(self.y+self.length-self.test_y)<=20:
            return 1
        elif abs(self.y+self.length-self.test_y)<=40:
            return 2
        else:
            return 0

class RaindropBall:
    def __init__(self,x, y, color,radius, test_y):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.color = color
        self.test_y = test_y
        self.img = pygame.transform.scale(rains_img, (Thirty, Thirty/2+Thirty/2*math.sqrt(3)))

        
    def draw(self,window):
        window.blit(self.img,(self.x+Fifty/5,self.y))
        pygame.draw.circle(window, (255, 255, 255), (self.x + Fifty/2, self.test_y + Fifty/2), Fifty/2, 4)


    def update(self):
        self.y += self.speed
        
    def test(self):
        if abs(self.y-self.test_y) <= 5:
            return 1
        else:
            return 0

# 定义粒子类
class Particle:
    def __init__(self,x, y, color):
        self.x = x
        self.y = y
        self.vx = (random.random() - 0.5) * 10
        self.vy = (random.random() - 0.5) * 10
        self.size = random.random() * 15 + 2
        self.color = color
    

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.size *= 0.95

    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.size)
