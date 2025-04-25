import pygame
from chocieSongs import *
from Source import *

# 初始化Pygame
pygame.display.init()
pygame.font.init()
WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h

# print(WIDTH, HEIGHT)

left = pygame.transform.scale(pygame.image.load('./image/left.png'),(100/1536*WIDTH,100/1536*WIDTH))
right = pygame.transform.scale(pygame.image.load('./image/right.png'),(100/1536*WIDTH,100/1536*WIDTH))
theme_img = pygame.transform.scale(pygame.image.load('./image/themeTop.png'),(400/1536*WIDTH,100/1536*WIDTH))
return_img = pygame.transform.scale(pygame.image.load('./image/return.png'),(small_setting_length,small_setting_length))
set_img = pygame.transform.scale(pygame.image.load('./image/set.png'),(small_setting_length,small_setting_length))


class theme():
    def __init__(self,name,img,bg,music_list,father):
        '''
        name: 主题名称
        img: 主题图片
        bg: 主题背景图片
        music_list: 主题音乐列表
        father: 父类
        '''
        self.name = name
        self.img = img
        self.bg = bg
        self.MusicChoice = MusicChoicer(music_list, self,father)
        self.MusicChoice.set_music_father()
        self.text_size = pygame.font.Font("./font/SanJiLuRongTi/SanJiLuRongTi-2.ttf", int(50/1536*WIDTH))
        
    def draw(self,window):
        window.blit(self.bg, (0, 0))
        window.blit(black, (0, 0))
        
        window.blit(return_img,(25/1536*WIDTH,40/1536*WIDTH))
        window.blit(set_img,(150/1536*WIDTH,40/1536*WIDTH))
        
        window.blit(theme_img,(WIDTH//2 - 200/1536*WIDTH,HEIGHT//8))
        name = self.text_size.render(self.name, True, (0, 0, 0))
        window.blit(name, (WIDTH//2 - name.get_width()//2, HEIGHT//8 + 25/1536*WIDTH ))
        
        window.blit(self.img,(WIDTH//4,HEIGHT//4 + HEIGHT // 8))

class ThemeManager():
    def __init__(self,theme_list):
        '''
        theme_list: 主题列表
        '''
        self.theme_sources = theme_list
        self.current_theme_index = 0
        self.sound=pygame.mixer.Sound('./gamemusic/pianocd - 星河.mp3')

    def init_themes(self):
        self.theme_list = []
        for source in self.theme_sources:
            self.theme_list.append(theme(source[0],source[1],source[2],source[3],self))

    def get_current_theme(self):
        return self.theme_list[self.current_theme_index]

    def draw(self,window):
        current_theme = self.get_current_theme()
        current_theme.draw(window)
        window.blit(left,(100/1536*WIDTH,HEIGHT//2+HEIGHT//8 - 50/1536*WIDTH))
        window.blit(right,(WIDTH-200/1536*WIDTH,HEIGHT//2+HEIGHT//8 - 50/1536*WIDTH))

    def switch(self,key,window):
        """
        切换当前视图。

        Args:
            cur (pygame.Surface): 当前绘制的Surface对象。
            key (int): 切换键。1表示淡入效果，2表示淡出效果。
            window (pygame.Surface): 主窗口Surface对象。

        Returns:
            None

        """
        # print("switch")
        if key == 1:
            
            surface = pygame.Surface((WIDTH, HEIGHT))
            self.draw(surface)
            for i in range(255,-1,-32):
                window.fill((0, 0, 0))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                clock.tick(30)
                surface.set_alpha(i)
                window.blit(surface, (0, 0))
                pygame.display.update()
        elif key == 2:
            # window.fill((0, 0, 0))
            surface = pygame.Surface((WIDTH, HEIGHT))
            self.draw(surface)
            for i in range(0,256,16):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                clock.tick(60)
                surface.set_alpha(i)
                window.blit(surface, (0, 0))
                pygame.display.update()

    def change_theme(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.current_theme_index = (self.current_theme_index - 1) % len(self.theme_list)
            elif event.key == pygame.K_RIGHT:
                self.current_theme_index = (self.current_theme_index + 1) % len(self.theme_list)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if event.button == 1:
                if pos[0] > 100/1536*WIDTH and pos[0] < 200/1536*WIDTH and pos[1] > HEIGHT//2+HEIGHT//8 - 50/1536*WIDTH and pos[1] < HEIGHT//2+HEIGHT//8 + 50/1536*WIDTH:
                    self.switch(1,window)
                    self.current_theme_index = (self.current_theme_index - 1) % len(self.theme_list)
                    self.switch(2,window)
                elif pos[0] > WIDTH - 200/1536*WIDTH and pos[0] < WIDTH - 100/1536*WIDTH and pos[1] > HEIGHT//2+HEIGHT//8 - 50/1536*WIDTH and pos[1] < HEIGHT//2+HEIGHT//8 + 50/1536*WIDTH:
                    self.switch(1,window)
                    self.current_theme_index = (self.current_theme_index + 1) % len(self.theme_list)
                    self.switch(2,window)
                if pos[0] > WIDTH // 4 and pos[0] < WIDTH // 4 +  WIDTH // 2 and pos[1] > HEIGHT // 4 + HEIGHT // 8 and pos[1] < HEIGHT // 4 + HEIGHT // 8 + HEIGHT // 2:
                    threading.Thread(target=lambda : enter_music_effect.play()).start()
                    self.sound.stop()
                    return self.get_current_theme().MusicChoice
                if pos[0] > 25/1536*WIDTH and pos[0] < 97/1536*WIDTH and pos[1] > 40/1536*WIDTH and pos[1] < 112/1536*WIDTH:
                    pygame.quit()
                    sys.exit()
                if pos[0] > 150/1536*WIDTH and pos[0] < 222/1536*WIDTH and pos[1] > 40/1536*WIDTH and pos[1] < 112/1536*WIDTH:
                    return 'set'
        return None
                
    def change_sound_volumn(self,v):
        # print("change")
        self.sound.set_volume(v)
        