import pygame
from Source import *

# 初始化pygame.display
pygame.display.init()
pygame.font.init()

WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h

songlist_img = pygame.image.load("./image/songlist.png")
songlist_img = pygame.transform.scale(songlist_img, (560/1536*WIDTH,160/1536*WIDTH))
return_img = pygame.transform.scale(pygame.image.load('./image/return.png'),(small_setting_length,small_setting_length))
set_img = pygame.transform.scale(pygame.image.load('./image/set.png'),(small_setting_length,small_setting_length))
theme_image = pygame.transform.scale(pygame.image.load('./image/themeTop.png'),(400/1536*WIDTH,100/1536*WIDTH))

class MusicChoicer:
    def __init__(self,songs_list,theme,father):
        '''
        :param songs_list: 歌曲列表
        :param theme: 主题
        :param father: 主题父类
        '''
        self.positions = (72/1536*WIDTH,376/1536*WIDTH)
        self.line_pos = (912/1536*WIDTH,96/1536*WIDTH),(552/1536*WIDTH,456/1536*WIDTH),(992/1536*WIDTH,896/1536*WIDTH)
        self.bk_pos = (700/1536*WIDTH,216/1536*WIDTH)
        self.text_positions = [[(192/1536*WIDTH,256/1536*WIDTH),(312/1536*WIDTH,236/1536*WIDTH),(312/1536*WIDTH,316/1536*WIDTH)],[(112/1536*WIDTH,416/1536*WIDTH),(232/1536*WIDTH,396/1536*WIDTH),(232/1536*WIDTH,476/1536*WIDTH)],[(192/1536*WIDTH,576/1536*WIDTH),(312/1536*WIDTH,556/1536*WIDTH),(312/1536*WIDTH,636/1536*WIDTH)],[(272/1536*WIDTH,736/1536*WIDTH),(392/1536*WIDTH,716/1536*WIDTH),(392/1536*WIDTH,796/1536*WIDTH)]]
        self.index_font = pygame.font.Font("./font/SanJiLuRongTi/SanJiLuRongTi-2.ttf", int(80/1536*WIDTH))
        self.rank_font = pygame.font.Font("./font/SanJiLuRongTi/SanJiLuRongTi-2.ttf", int(60/1536*WIDTH))
        self.text_size = pygame.font.Font("./font/SanJiLuRongTi/SanJiLuRongTi-2.ttf", int(40/1536*WIDTH))
        self.text_color = (255, 255, 255)
        self.line_color = (255, 255, 255, 64)
        self.songs_list = songs_list
        self.song_spacing = 160/1536*WIDTH
        self.index = [len(self.songs_list)-1,0,1,2]
        self.father = theme
        self.father_father = father
    
    def set_music_father(self):
        for song in self.songs_list:
            song.set_father(self)
    
    def start_music(self):
        self.songs_list[self.index[1]].play_sound()
    
    def draw(self, window):
        window.blit(self.songs_list[self.index[1]].bg, (0, 0))
        window.blit(black, (0, 0))
        
        window.blit(return_img,(25/1536*WIDTH,40/1536*WIDTH))
        window.blit(set_img,(150/1536*WIDTH,40/1536*WIDTH))
        
        window.blit(songlist_img, self.positions)
        pygame.draw.line(window, self.line_color, self.line_pos[0], self.line_pos[1], 4)
        pygame.draw.line(window, self.line_color, self.line_pos[1], self.line_pos[2], 4)
        
        theme_name = self.text_size.render(self.father.name, True, (128, 128, 128))
        window.blit(theme_image,(WIDTH//2 - 200/1536*WIDTH,HEIGHT//8 - 65/1536*WIDTH))
        window.blit(theme_name, (WIDTH//2 - theme_name.get_width()//2, HEIGHT//8 - 30/1536*WIDTH ))
        
        window.blit(self.songs_list[self.index[1]].cover, self.bk_pos)
        best_rank = self.rank_font.render("Best Rank:"+self.songs_list[self.index[1]].best_rank,True, (255, 255, 255))
        window.blit(best_rank, (self.bk_pos[0] + WIDTH//2 - best_rank.get_width() , self.bk_pos[1] - 80/1536*WIDTH))
        
        for i in range(4):
            name = self.songs_list[self.index[i]].name
            writer = self.songs_list[self.index[i]].writer
            index_surface = self.index_font.render(str(self.index[i]+1), True, self.text_color)
            name_surface = self.text_size.render(name, True, self.text_color)
            writer_surface = self.text_size.render(writer, True, self.text_color)
            window.blit(index_surface, self.text_positions[i][0])
            window.blit(name_surface, self.text_positions[i][1])
            window.blit(writer_surface, self.text_positions[i][2]) 
            # print(self.text_positions[i][0], self.text_positions[i][1], self.text_positions[i][2])     
        
    def switch(self,key,window):
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
                clock.tick(60)
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
        
    def scroll(self,event):
        """
        滚动音乐列表并播放对应音乐。

        Args:
            event (pygame.event.Event): 事件对象，包含事件类型和信息。

        Returns:
            str or None: 根据点击的位置返回对应的字符串标识或返回None。

        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 5:
                self.switch(1,window)
                self.songs_list[self.index[1]].stop_sound()
                self.index.append((self.index[-1]+1)%len(self.songs_list))
                self.index.pop(0)
                self.switch(2,window)
                self.songs_list[self.index[1]].play_sound()
            elif event.button == 4:
                self.switch(1,window)
                self.songs_list[self.index[1]].stop_sound()
                self.index.insert(0,(self.index[0]-1+len(self.songs_list))%len(self.songs_list))
                self.index.pop()
                self.switch(2,window)
                self.songs_list[self.index[1]].play_sound()
            elif event.button == 1:
                pos = pygame.mouse.get_pos()
                if (pos[0] > WIDTH//2 - 200 and pos[0] < WIDTH//2 + 200 and pos[1] > HEIGHT//8 - 65 and pos[1] < HEIGHT//8 + 35) or (pos[0] > 25 and pos[0] < 97 and pos[1] > 40 and pos[1] < 112) :
                    self.songs_list[self.index[1]].stop_sound()
                    return "theme"
                if pos[0] > self.bk_pos[0] and pos[1] > self.bk_pos[1] and pos[1] < self.bk_pos[1] + HEIGHT//2 + HEIGHT// 8:
                    self.songs_list[self.index[1]].stop_sound()
                    threading.Thread(target=lambda : enter_music_effect.play()).start()
                    return 'music'
                if pos[0] > 150/1536*WIDTH and pos[0] < 222/1536*WIDTH and pos[1] > 40/1536*WIDTH and pos[1] < 112/1536*WIDTH:
                    # self.songs_list[self.index[1]].stop_sound()
                    return 'set'
        return None
    