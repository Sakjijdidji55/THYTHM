import pygame
from Source import *

# 初始化Pygame
pygame.display.init()

WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h

return_img = pygame.transform.scale(pygame.image.load('./image/return.png'),(small_setting_length,small_setting_length))

class MUSICSETTING:

    def __init__(self):
        self.x = WIDTH//8
        self.y = HEIGHT//8
        self.choice = False
        self.font = pygame.font.Font("./font/SanJiLuRongTi/SanJiLuRongTi-2.ttf", int(50/1536*WIDTH))
        self.long = pygame.transform.scale(pygame.image.load('./image/setVolume.png'),(600/1536*WIDTH,40/1536*WIDTH))
        self.small = pygame.transform.scale(pygame.image.load('./image/small.png'),(40/1536*WIDTH,40/1536*WIDTH))
        self.v_img = pygame.transform.scale(pygame.image.load('./image/set_v.png'),(60/1536*WIDTH,40/1536*WIDTH))
        self.ve_img = pygame.transform.scale(pygame.image.load('./image/set_ve.png'),(50/1536*WIDTH,50/1536*WIDTH))
        self.small_x = self.x + 760/1536*WIDTH
        self.max = self.x + 760/1536*WIDTH
        self.small_state = False
        self.effect_state = True
        self.inc = 25/1536*WIDTH
        self.FPS = FPS
        
    def draw_set(self,window):
        rect_surface = pygame.Surface((WIDTH//2+WIDTH//4, HEIGHT//2+HEIGHT//4))
        rect_surface.fill((0,0,0))
        rect_surface.set_alpha(225)
        
        window.blit(rect_surface,(self.x,self.y))

        window.blit(return_img,(self.x + self.inc,self.y+self.inc))
    
    def draw(self,window):
        self.draw_set(window)
        
        voulme = self.font.render("音量: ", True, (255, 255, 255))
        voulme_value = self.font.render(str(int((self.small_x - self.x - 200/1536*WIDTH) / (560/1536*WIDTH) * 100)) + "%", True, (255, 255, 255))
        
        window.blit(voulme,(self.x + 50/1536*WIDTH,self.y + 175/1536*WIDTH))
        pygame.draw.rect(window, (0, 0, 0), (self.max + 90/1536*WIDTH,self.y + 175/1536*WIDTH, 150/1536*WIDTH, 50/1536*WIDTH))
        window.blit(voulme_value,(self.max + 90/1536*WIDTH,self.y + 175/1536*WIDTH))
        window.blit(self.long,(self.x + 200/1536*WIDTH,self.y + 180/1536*WIDTH))
        window.blit(self.small,(self.small_x,self.y + 180/1536*WIDTH))
        
        volumn_effect = self.font.render("音效: ", True, (255, 255, 255))
        
        window.blit(volumn_effect,(self.x + 50/1536*WIDTH,self.y + 375/1536*WIDTH))
        
        volumn_effect_up = self.font.render("开: ", True, (255, 255, 255))
        volumn_effect_down = self.font.render("关: ", True, (255, 255, 255))

        window.blit(volumn_effect_up,(self.x + 250/1536*WIDTH,self.y + 375/1536*WIDTH))
        pygame.draw.rect(window, (0, 0, 0), (self.x + 345/1536*WIDTH,self.y + 380/1536*WIDTH, 60/1536*WIDTH, 40/1536*WIDTH))
        window.blit(self.ve_img,(self.x + 350/1536*WIDTH,self.y + 375/1536*WIDTH))
        window.blit(volumn_effect_down,(self.x + 600/1536*WIDTH,self.y + 375/1536*WIDTH))
        pygame.draw.rect(window, (0, 0, 0), (self.x + 695/1536*WIDTH,self.y + 380/1536*WIDTH, 60/1536*WIDTH, 40/1536*WIDTH))
        window.blit(self.ve_img,(self.x + 700/1536*WIDTH,self.y + 375/1536*WIDTH))
        if self.effect_state == True:
            window.blit(self.v_img,(self.x + 345/1536*WIDTH,self.y + 380/1536*WIDTH))
        else:
            window.blit(self.v_img,(self.x + 695/1536*WIDTH,self.y + 380/1536*WIDTH))
        # x,y = pygame.mouse.get_pos()
        # window.blit(mouse,(x,y))
        
        
        FPS_text = self.font.render("FPS: ", True, (255, 255, 255))
        window.blit(FPS_text,(self.x + 50/1536*WIDTH,self.y + 575/1536*WIDTH))
        
        _30 = self.font.render("30: ", True, (255, 255, 255))
        _45 = self.font.render("45: ", True, (255, 255, 255))
        _60 = self.font.render("60: ", True, (255, 255, 255))
        
        window.blit(_30,(self.x + 200/1536*WIDTH,self.y + 575/1536*WIDTH))
        pygame.draw.rect(window, (0, 0, 0), (self.x + 300/1536*WIDTH,self.y + 575/1536*WIDTH, 60/1536*WIDTH, 40/1536*WIDTH))
        window.blit(self.ve_img,(self.x + 305/1536*WIDTH,self.y + 575/1536*WIDTH))
        
        window.blit(_45,(self.x + 450/1536*WIDTH,self.y + 575/1536*WIDTH))
        pygame.draw.rect(window, (0, 0, 0), (self.x + 550/1536*WIDTH,self.y + 575/1536*WIDTH, 60/1536*WIDTH, 40/1536*WIDTH))
        window.blit(self.ve_img,(self.x + 555/1536*WIDTH,self.y + 575/1536*WIDTH))
        
        window.blit(_60,(self.x + 700/1536*WIDTH,self.y + 575/1536*WIDTH))
        pygame.draw.rect(window, (0, 0, 0), (self.x + 800/1536*WIDTH,self.y + 575/1536*WIDTH, 60/1536*WIDTH, 40/1536*WIDTH))
        window.blit(self.ve_img,(self.x + 805/1536*WIDTH,self.y + 575/1536*WIDTH))
        
        if self.FPS == 30:
            window.blit(self.v_img,(self.x + 300/1536*WIDTH,self.y + 575/1536*WIDTH))
        elif self.FPS == 45:
            window.blit(self.v_img,(self.x + 550/1536*WIDTH,self.y + 575/1536*WIDTH))
        elif self.FPS == 60:
            window.blit(self.v_img,(self.x + 800/1536*WIDTH,self.y + 575/1536*WIDTH))
        
    def is_check_set(self,event):
        volumn = (self.small_x - self.x - 200/1536*WIDTH) / (560/1536*WIDTH)
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if pos[0] > self.x + self.inc and pos[0] < self.x + self.inc + small_setting_length and pos[1] > self.y + self.inc and pos[1] < self.y + self.inc + small_setting_length:
                self.choice = False
            elif pos[0] > self.small_x and pos[0] < self.small_x + 40/1536*WIDTH and pos[1] > self.y + 180/1536*WIDTH and pos[1] < self.y + 230/1536*WIDTH:
                self.small_state = not self.small_state
            elif pos[0] > self.x + 350/1536*WIDTH and pos[0] < self.x + 400/1536*WIDTH and pos[1] > self.y + 375/1536*WIDTH and pos[1] < self.y + 425/1536*WIDTH:
                self.effect_state = True
            elif pos[0] > self.x + 700/1536*WIDTH and pos[0] < self.x + 750/1536*WIDTH and pos[1] > self.y + 375/1536*WIDTH and pos[1] < self.y + 425/1536*WIDTH:
                self.effect_state = False
            elif pos[0] > self.x + 300/1536*WIDTH and pos[0] < self.x + 360/1536*WIDTH and pos[1] > self.y + 575/1536*WIDTH and pos[1] < self.y + 625/1536*WIDTH:
                self.FPS = 30
            elif pos[0] > self.x + 550/1536*WIDTH and pos[0] < self.x + 610/1536*WIDTH and pos[1] > self.y + 575/1536*WIDTH and pos[1] < self.y + 625/1536*WIDTH:
                self.FPS = 45
            elif pos[0] > self.x + 800/1536*WIDTH and pos[0] < self.x + 860/1536*WIDTH and pos[1] > self.y + 575/1536*WIDTH and pos[1] < self.y + 625/1536*WIDTH:
                self.FPS = 60
        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            if self.small_state == True:
                small_x = self.small_x + (pos[0] - self.small_x)
                volumn = (small_x - self.x - 200/1536*WIDTH) / (560/1536*WIDTH)
                if small_x > self.max:
                    small_x = self.max
                    volumn = 1
                elif small_x < self.x + 200/1536*WIDTH:
                    small_x = self.x + 200/1536*WIDTH
                    volumn = 0
                self.small_x = small_x
        if event.type == pygame.MOUSEBUTTONUP:
            self.small_state = False
        return volumn,self.effect_state
    