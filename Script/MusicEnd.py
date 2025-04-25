import pygame
from Source import *

# 初始化Pygame
pygame.display.init()
pygame.font.init()
WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h

left = pygame.transform.scale(pygame.image.load('./image/left.png'),(100/1536*WIDTH,100/1536*WIDTH))
right = pygame.transform.scale(pygame.image.load('./image/right.png'),(100/1536*WIDTH,100/1536*WIDTH))
name_img = pygame.transform.scale(pygame.image.load('./image/EndTop.png'),(600/1536*WIDTH,100/1536*WIDTH))
perfect_img = pygame.transform.scale(pygame.image.load('./image/perfect.png'),(400/1536*WIDTH,100/1536*WIDTH))
good_img = pygame.transform.scale(pygame.image.load('./image/good.png'),(400/1536*WIDTH,100/1536*WIDTH))
miss_img = pygame.transform.scale(pygame.image.load('./image/miss.png'),(400/1536*WIDTH,100/1536*WIDTH))
return_img = pygame.transform.scale(pygame.image.load('./image/return.png'),(small_setting_length,small_setting_length))
set_img = pygame.transform.scale(pygame.image.load('./image/set.png'),(small_setting_length,small_setting_length))
continue_img = pygame.transform.scale(pygame.image.load('./image/continue.png'),(100/1536*WIDTH,100/1536*WIDTH))


class MusicEnd():
    def __init__(self,song,name,img,bg,score,total,perfect,miss,good):
        '''
        :param name: 歌曲名
        :param img: 歌曲封面(圆角)
        :param bg: 背景图片
        :param score: 得分
        :param total: 总分
        :param perfect: 完美数
        :param miss: 漏掉数
        :param good: 好数
        '''
        self.song = song
        self.name = name
        self.img = img
        self.bg = bg
        self.rank_size = pygame.font.Font("./font/SanJiLuRongTi/SanJiLuRongTi-2.ttf", int(120/1536*WIDTH))
        self.score_size = pygame.font.Font("./font/SanJiLuRongTi/SanJiLuRongTi-2.ttf", int(80/1536*WIDTH))
        self.text_size = pygame.font.Font("./font/SanJiLuRongTi/SanJiLuRongTi-2.ttf", int(50/1536*WIDTH))
        self.score = int(score)
        self.perfect = perfect
        self.miss = max(miss,0)
        self.good = good
        self.rank = self.get_rank(score,total)
        gameover_music.play()

    def get_rank(self,score,total):
        if score <= total and score > total * - 10:
            return "SSS"
        if score / total >= 0.97:
            return "SS"
        if score/total >= 0.95:
            return "S"
        if score >= total * 0.9:
            return "A"
        if score >= total * 0.8:
            return "B"
        else:
            return "C"

    def draw(self,window):
        window.blit(self.bg, (0, 0))
        window.blit(black, (0, 0))
        
        window.blit(return_img,(25,40))
        window.blit(set_img,(150,40))
        window.blit(continue_img,(WIDTH - 125/1536*WIDTH - WIDTH//24,HEIGHT - 125/1536*WIDTH))
        
        window.blit(name_img,(WIDTH//4 + WIDTH//16 - name_img.get_width()//2,HEIGHT//8))
        name = self.text_size.render(self.name, True, (0, 0, 0))
        window.blit(name, (WIDTH//4 + WIDTH//16 - name.get_width()//2, HEIGHT//8 + 25 ))
        
        score = self.score_size.render(str(self.score), True, (255, 255, 255))
        rank = self.rank_size.render(self.rank, True, (128,0, 255))
        perfect = self.text_size.render("Perfect: " + str(self.perfect), True, (0, 0, 0))
        miss = self.text_size.render("Miss: " + str(self.miss), True, (0, 0, 0))
        good = self.text_size.render("Good: " + str(self.good), True, (0, 0, 0))
        
        window.blit(score, (WIDTH//2 + WIDTH//7 - score.get_width()//2, HEIGHT//8 + 10/1536*WIDTH))

        window.blit(rank, (WIDTH - WIDTH//10 - rank.get_width()//2, HEIGHT//8 - 10/1536*WIDTH))

        window.blit(perfect_img,(WIDTH//2 + WIDTH//4 - perfect_img.get_width()//2, HEIGHT//2 - HEIGHT//8 ))
        
        window.blit(perfect, (WIDTH//2 + WIDTH//4 - perfect.get_width()//2, HEIGHT//2 - HEIGHT//8 + 25))

        window.blit(good_img,(WIDTH//2 + WIDTH//4 - good_img.get_width()//2, HEIGHT//2 + 140/1536*WIDTH - HEIGHT//8))

        window.blit(good, (WIDTH//2 + WIDTH//4 - good.get_width()//2, HEIGHT//2 + 165/1536*WIDTH - HEIGHT//8)) 
        
        window.blit(miss_img,(WIDTH//2 + WIDTH//4 - miss_img.get_width()//2, HEIGHT//2 + 280 - HEIGHT//8))
        
        window.blit(miss, (WIDTH//2 + WIDTH//4 - miss.get_width()//2, HEIGHT//2 + 305/1536*WIDTH - HEIGHT//8))
        
        window.blit(self.img,(WIDTH//16,HEIGHT//4 + HEIGHT // 8))


    def check_clicked(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if pos[0] >= 25/1536*WIDTH and pos[0] <= 112/1536*WIDTH and pos[1] >= 40/1536*WIDTH and pos[1] <= 112/1536*WIDTH:
                gameover_music.stop()
                return "return"

            if pos[0] >= 150/1536*WIDTH and pos[0] <= (150 + 72)/1536*WIDTH and pos[1] >= 40/1536*WIDTH and pos[1] <= 112/1536*WIDTH:
                return "set"

            if pos[0] >= WIDTH - 125/1536*WIDTH - WIDTH//24 and pos[0] <= WIDTH - 125/1536*WIDTH - WIDTH//24 + 100/1536*WIDTH and pos[1] >= HEIGHT - 125/1536*WIDTH and pos[1] <= HEIGHT - 125/1536*WIDTH + 100/1536*WIDTH:
                gameover_music.stop()
                return "continue"
        return None
