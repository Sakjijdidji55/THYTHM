import pygame
from pynput.keyboard import Key, Controller
import random
import threading
import os
from userData import *
import sys
import pickle

pygame.init()
WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
clock = pygame.time.Clock()
pygame.font.init()
FPS = 60
speed = (5/1536*WIDTH)/FPS*60
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music")


normal_font = pygame.font.Font("./font/SanJiLuRongTi/SanJiLuRongTi-2.ttf", int(50/1536*WIDTH))
enter_music = pygame.mixer.Sound("./music/enter.mp3")
enter_music_effect = pygame.mixer.Sound("./music/enter_effect.MP3")
gameover_music = pygame.mixer.Sound("./music/gameover.MP3")

start_video = []

enter_video = []

for i in range(0,420):
    path = "./start/frame_"+str(i).zfill(4)+".jpg"
    start_video.append(pygame.transform.scale(pygame.image.load(path), (WIDTH, HEIGHT)))

for i in range(0,450):
    path = "./newenter/frame_"+str(i).zfill(4)+".jpg"
    enter_video.append(pygame.transform.scale(pygame.image.load(path), (WIDTH, HEIGHT)))

music_names = []

# 歌曲：序章

xuzhang_sources = []
theme_xuzhang_bg = pygame.transform.scale(pygame.image.load("./themebg/序章.png"),(WIDTH,HEIGHT))
theme_xuzhang_img = pygame.transform.scale(pygame.image.load("./themecover/序章.png"),(WIDTH//2,HEIGHT//2))

# 歌曲：故事

gushi_sources = []
theme_gushi_img = pygame.transform.scale(pygame.image.load("./themecover/故事.png"),(WIDTH//2,HEIGHT//2))
theme_gushi_bg = pygame.transform.scale(pygame.image.load("./themebg/故事.png"),(WIDTH,HEIGHT))            

# 歌曲：回忆

huiyi_sources = []
theme_huiyi_img = pygame.transform.scale(pygame.image.load("./themecover/回忆.png"),(WIDTH//2,HEIGHT//2))
theme_huiyi_bg = pygame.transform.scale(pygame.image.load("./themebg/回忆.png"),(WIDTH,HEIGHT))


# 歌曲：雨天

yutian_sources = []
theme_yutian_img = pygame.transform.scale(pygame.image.load("./themecover/雨天.png"),(WIDTH//2,HEIGHT//2))  
theme_yutian_bg = pygame.transform.scale(pygame.image.load("./themebg/雨天.png"),(WIDTH,HEIGHT))

# 歌曲：古风

gufeng_sources = []
theme_gufeng_img = pygame.transform.scale(pygame.image.load("./themecover/古风.png"),(WIDTH//2,HEIGHT//2))
theme_gufeng_bg = pygame.transform.scale(pygame.image.load("./themebg/古风.png"),(WIDTH,HEIGHT))

# 歌曲：寻常

xunchang_sources = []
theme_xunchang_img = pygame.transform.scale(pygame.image.load("./themecover/寻常.png"),(WIDTH//2,HEIGHT//2))
theme_xunchang_bg = pygame.transform.scale(pygame.image.load("./themebg/寻常.png"),(WIDTH,HEIGHT)) 

# 歌曲：悦耳

yueer_sources = []
theme_yueer_img = pygame.transform.scale(pygame.image.load("./themecover/悦耳.png"),(WIDTH//2,HEIGHT//2))
theme_yueer_bg = pygame.transform.scale(pygame.image.load("./themebg/悦耳.png"),(WIDTH,HEIGHT))


# 歌曲：单曲

danqu_sources = []
theme_danqu_img = pygame.transform.scale(pygame.image.load("./themecover/单曲.png"),(WIDTH//2,HEIGHT//2))
theme_danqu_bg = pygame.transform.scale(pygame.image.load("./themebg/单曲.png"),(WIDTH,HEIGHT))

# load_music_inform
for root, dirs, files in os.walk("./gamemusic/序章"):
    for file in files:
        if file.endswith(".mp3"):
            writer,name = file.split("-")
            writer = writer[:-1]
            name = name[1:-4]
            name = name.split("-")[-1]
            music_inform = [writer,name,"./gamemusic/序章/"+file,"./gameimage/序章/"+file[:-4]+".png","./gamecover/序章/"+file[:-4]+".png"]
            xuzhang_sources.append(music_inform)
            music_names.append(name)

for root, dirs, files in os.walk("./gamemusic/故事"):
    for file in files:
        if file.endswith(".mp3"):
            writer,name = file.split("-")
            writer = writer[:-1]
            name = name[1:-4]
            name = name.split("-")[-1]
            music_inform = [writer,name,"./gamemusic/故事/"+file,"./gameimage/故事/"+file[:-4]+".png","./gamecover/故事/"+file[:-4]+".png"]
            gushi_sources.append(music_inform)
            music_names.append(name)
            
for root, dirs, files in os.walk("./gamemusic/回忆"):
    for file in files:
        if file.endswith(".mp3"):
            writer,name = file.split("-",1)
            writer = writer[:-1]
            name = name[1:-4]
            name = name.split("-")[-1]
            music_inform = [writer,name,"./gamemusic/回忆/"+file,"./gameimage/回忆/"+file[:-4]+".png","./gamecover/回忆/"+file[:-4]+".png"]
            huiyi_sources.append(music_inform)
            music_names.append(name)
        
        
for root, dirs, files in os.walk("./gamemusic/雨天"):
    for file in files:
        if file.endswith(".mp3"):
            writer,name = file.split("-",1)
            writer = writer[:-1]
            name = name[1:-4]
            name = name.split("-")[-1]
            music_inform = [writer,name,"./gamemusic/雨天/"+file,"./gameimage/雨天/"+file[:-4]+".png","./gamecover/雨天/"+file[:-4]+".png"]
            yutian_sources.append(music_inform)
            music_names.append(name)  
                
for root, dirs, files in os.walk("./gamemusic/古风"):
    for file in files:
        if file.endswith(".mp3"):
            writer,name = file.split("-",1)
            writer = writer[:-1]
            name = name[1:-4]
            name = name.split("-")[-1]
            music_inform = [writer,name,"./gamemusic/古风/"+file,"./gameimage/古风/"+file[:-4]+".png","./gamecover/古风/"+file[:-4]+".png"]
            gufeng_sources.append(music_inform)
            music_names.append(name)   
            
for root, dirs, files in os.walk("./gamemusic/寻常"):
    for file in files:
        if file.endswith(".mp3"):
            writer,name = file.split("-",1)
            writer = writer[:-1]
            name = name[1:-4]
            name = name.split("-")[-1]
            music_inform = [writer,name,"./gamemusic/寻常/"+file,"./gameimage/寻常/"+file[:-4]+".png","./gamecover/寻常/"+file[:-4]+".png"]
            xunchang_sources.append(music_inform)
            music_names.append(name)      

for root, dirs, files in os.walk("./gamemusic/悦耳"):
    for file in files:
        if file.endswith(".mp3"):
            writer,name = file.split("-",1)
            writer = writer[:-1]
            name = name[1:-4]
            name = name.split("-")[-1]
            music_inform = [writer,name,"./gamemusic/悦耳/"+file,"./gameimage/悦耳/"+file[:-4]+".png","./gamecover/悦耳/"+file[:-4]+".png"]
            yueer_sources.append(music_inform)
            music_names.append(name)
            
for root, dirs, files in os.walk("./gamemusic/单曲"):
    for file in files:
        if file.endswith(".mp3"):
            writer,name = file.split("-",1)
            writer = writer[:-1]
            name = name[1:-4]
            name = name.split("-")[-1]
            music_inform = [writer,name,"./gamemusic/单曲/"+file,"./gameimage/单曲/"+file[:-4]+".png","./gamecover/单曲/"+file[:-4]+".png"]
            danqu_sources.append(music_inform)
            music_names.append(name)

music_note = {}
music_note = get_music_inform(music_note,music_notes_path)

class Raindrop:
    # 初始化雨滴的属性
    def __init__(self):
        """
        初始化雨滴对象。

        Args:
            无

        Returns:
            无

        Raises:
            无

        """
        # 随机生成雨滴的初始位置
        self.x = random.randint(0, WIDTH)
        self.y = 0
        # 随机生成雨滴的速度
        self.speed = random.randint(5, 15)
        # 随机生成雨滴的长度
        self.length = random.randint(10, 20)

    # 雨滴下落的方法
    def fall(self):
        # 雨滴的y坐标增加速度
        self.y += self.speed

    # 绘制雨滴的方法
    def draw(self,window):
        """
        在窗口上绘制雨滴。

        Args:
            window (pygame.Surface): 窗口对象，用于绘制雨滴。

        Returns:
            None

        """
        # 在窗口上绘制雨滴
        pygame.draw.line(window, (211, 211, 211), (self.x, self.y), (self.x, self.y + self.length), 2)

    # 判断雨滴是否超出屏幕的方法
    def off_screen(self):
        """
        判断雨滴是否已移出屏幕。

        Args:
            无

        Returns:
            bool: 如果雨滴的y坐标大于屏幕的高度，则返回True，否则返回False。

        """
        # 如果雨滴的y坐标大于屏幕的高度，则返回True
        return self.y > HEIGHT

raindrops = []

# pygame.mouse.set_visible(False)

black = pygame.image.load("./image/black.png").convert_alpha()
black.set_alpha(128)
black = pygame.transform.scale(black, (WIDTH, HEIGHT))
small_setting_length = 72
volumn = 1
pygame.mixer.music.set_volume(volumn)

# 创建一个键盘控制器, 直接切换成英文
keyboard = Controller()
# 按下shift键
keyboard.press(Key.shift)
# 释放shift键
keyboard.release(Key.shift)

def begin(user):
    """
    开始游戏的主要逻辑函数。

    Args:
        无参数。

    Returns:
        无返回值。

    """
    # 遍历start_video中的每一帧图像
    for img in start_video:
        for event in pygame.event.get():
            # 如果事件类型为退出
            if event.type == pygame.QUIT:
                # 退出pygame
                pygame.quit()
                # 退出程序
                sys.exit()
        # 设置帧率为FPS
        clock.tick(60)
        # 将当前帧图像绘制到窗口中
        window.blit(img, (0, 0))
        # 更新窗口显示
        pygame.display.update()
    # 播放进入音乐
    enter_music.play()
    # 创建一个线程，用于播放进入音乐效果
    t=threading.Thread(target=lambda : enter_music_effect.play())
    # 创建一个文本对象，显示“轻触开始”
    text = normal_font.render("轻触开始", True, (255, 255, 255))
    # 设置游戏运行标志为True
    is_running = True
    # 当游戏运行时
    while is_running:
        # 遍历pygame事件
        for event in pygame.event.get():
            # 如果事件类型为退出
            if event.type == pygame.QUIT:
                # 退出pygame
                pygame.quit()
                # 退出程序
                sys.exit()
            # 如果事件类型为鼠标按下
            if event.type == pygame.MOUSEBUTTONDOWN:
               #  print("鼠标按下")
                # 设置游戏运行标志为False
                is_running = False
                # 启动线程
                t.start()
                # 跳出循环
                break
        # 如果游戏运行标志为False
        if is_running == False:
            # 跳出循环
            break
        # 遍历enter_video中的每一帧图像
        for img in enter_video:
            # 遍历pygame事件
            for event in pygame.event.get():
                # 如果事件类型为退出
                if event.type == pygame.QUIT:
                    # 退出程序
                    sys.exit()
                # 如果事件类型为鼠标按下
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # print("鼠标按下")
                    # 设置游戏运行标志为False
                    pos = pygame.mouse.get_pos()
                    if pos[0] > 0 and pos[0] < WIDTH - 0.6*HEIGHT and pos[1] > 0 and pos[1] < HEIGHT:
                        is_running = False
                        # 启动线程
                        t.start()
                        # 跳出循环
                        break
                if user.check(event) == "User":
                    user.show = not user.show
            # 如果游戏运行标志为False
            if is_running == False:
                # 跳出循环
                break
                    
            # 设置帧率为FPS
            clock.tick(60)
            # 将当前帧图像绘制到窗口中
            window.blit(img, (0, 0))
            user.draw(window)
            # x,y = pygame.mouse.get_pos()
            # window.blit(mouse,(x,y))
            
            # 有10%的概率生成一个雨滴
            if random.random() < 0.1:
                raindrops.append(Raindrop())
                
            # 遍历雨滴列表
            for raindrop in raindrops[:]:
                # 雨滴下落
                raindrop.fall()
                # 绘制雨滴
                raindrop.draw(window)
                # 如果雨滴超出屏幕
                if raindrop.off_screen():
                    # 从雨滴列表中移除
                    raindrops.remove(raindrop)
            
            # 将文本绘制到窗口中
            window.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT - 100))
            # 更新窗口显示
            pygame.display.update()
            
    # 停止进入音乐
    enter_music.stop()
    pygame.display.update()

def wait_to_load(music,window):
    """
    在窗口上等待音乐加载并显示相关信息。

    Args:
        music (Music): 包含音乐信息的对象。
        window (pygame.Surface): 用于绘制图像的Surface对象。

    Returns:
        None

    """
    window.blit(music.bg, (0, 0))
    window.blit(black, (0, 0))
    
    window.blit(music.cover,(WIDTH // 2 - music.cover.get_size()[0] // 2 , HEIGHT // 3 - music.cover.get_size()[1] // 2))
    
    w = music.writer
    n = music.name
    
    w_text = normal_font.render("作者: "+w, True, (255, 255, 255))
    n_text = normal_font.render("歌曲名: "+n, True, (255, 255, 255))
    
    window.blit(w_text, (WIDTH // 2 - w_text.get_width() // 2, HEIGHT // 2 + w_text.get_height() * 3))
    window.blit(n_text, (WIDTH // 2 - n_text.get_width() // 2, HEIGHT // 2 + n_text.get_height() * 5))

    # x,y = pygame.mouse.get_pos()
    # window.blit(mouse,(x,y))

    pygame.display.update()
      
switch_audio = []

for i in range(1,110):
    path = "./switch_pickle/"+str(i).zfill(4)+".pickle"
    with open(path, 'rb') as f:
        data = pickle.load(f)
        img = pygame.image.fromstring(data["image_bytes"], data["size"], 'RGBA')
        img = pygame.transform.scale(img, (WIDTH, HEIGHT))
        switch_audio.append(img)         


    
def switch(cur,window):
    """
    切换当前视图。

    Args:
        cur (pygame.Surface): 当前绘制的Surface对象。
        key (int): 切换键。1表示淡入效果，2表示淡出效果。
        window (pygame.Surface): 主窗口Surface对象。

    Returns:
        None

    """
    for audio_farme in switch_audio:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        clock.tick(60)
        cur.draw(window)
        window.blit(audio_farme, (0, 0))
        pygame.display.update()
        # window.fill((0, 0, 0))      
