import pygame
from Source import *
from everyMusic import *
from chocieSongs import *
from MusicEnd import *
from ThemeManage import *
from setting import *
from User import *

default_init_pos=[[WIDTH//6-15/1536*WIDTH,0],[WIDTH//2-15/1536*WIDTH,0],[WIDTH//6*5-15/1536*WIDTH,0],[WIDTH//3-15/1536*WIDTH,0],[WIDTH//3*2-15/1536*WIDTH,0]]
user = User(user_data[user_imform_keys[0]],user_data[user_imform_keys[1]],user_data[user_imform_keys[2]])

music_inform = {}
for name in music_names:
    music_inform[name] = "未开始"
music_inform = get_music_inform(music_inform)

xuzhang_music = []
gushi_music = []
huiyi_music = []
yutian_music = []
gufeng_music = []
xunchang_music = []
danqu_music = []
yueer_music = []

for mf in xuzhang_sources:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    writer = mf[0]
    name = mf[1]
    music_file = mf[2]
    music_image = mf[3]
    music_cover = mf[4]
    music = MUSIC(name=name,writer=writer,file_name=music_file,bg_images=music_image,cover=music_cover,init_pos=default_init_pos,test_y=650/1536*WIDTH,count=3,best_rank=music_inform[name])
    xuzhang_music.append(music)
    
for mf in gushi_sources:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    writer = mf[0]
    name = mf[1]
    music_file = mf[2]
    music_image = mf[3]
    music_cover = mf[4]
    music = MUSIC(name=name,writer=writer,file_name=music_file,bg_images=music_image,cover=music_cover,init_pos=default_init_pos,test_y=650/1536*WIDTH,count=4,best_rank=music_inform[name])
    gushi_music.append(music)
    
    

for mf in huiyi_sources:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    writer = mf[0]
    name = mf[1]
    music_file = mf[2]
    music_image = mf[3]
    music_cover = mf[4]
    music = MUSIC(name=name,writer=writer,file_name=music_file,bg_images=music_image,cover=music_cover,init_pos=default_init_pos,test_y=650/1536*WIDTH,count=2,best_rank=music_inform[name])
    huiyi_music.append(music)


for mf in yutian_sources:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    writer = mf[0]
    name = mf[1]
    music_file = mf[2]
    music_image = mf[3]
    music_cover = mf[4]
    music = MUSIC(name=name,writer=writer,file_name=music_file,bg_images=music_image,cover=music_cover,init_pos=default_init_pos,test_y=650/1536*WIDTH,count=2,best_rank=music_inform[name])
    yutian_music.append(music)

for mf in gufeng_sources:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    writer = mf[0]
    name = mf[1]
    music_file = mf[2]
    music_image = mf[3]
    music_cover = mf[4]
    music = MUSIC(name=name,writer=writer,file_name=music_file,bg_images=music_image,cover=music_cover,init_pos=default_init_pos,test_y=650/1536*WIDTH,count=2,best_rank=music_inform[name])
    gufeng_music.append(music)
    
    
for mf in xunchang_sources:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    writer = mf[0]
    name = mf[1]
    music_file = mf[2]
    music_image = mf[3]
    music_cover = mf[4]
    music = MUSIC(name=name,writer=writer,file_name=music_file,bg_images=music_image,cover=music_cover,init_pos=default_init_pos,test_y=650/1536*WIDTH,count=2,best_rank=music_inform[name])
    xunchang_music.append(music)

for mf in danqu_sources:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    writer = mf[0]
    name = mf[1]
    music_file = mf[2]
    music_image = mf[3]
    music_cover = mf[4]
    music = MUSIC(name=name,writer=writer,file_name=music_file,bg_images=music_image,cover=music_cover,init_pos=default_init_pos,test_y=650/1536*WIDTH,count=2,best_rank=music_inform[name])
    danqu_music.append(music)
    
for mf in yueer_sources:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    writer = mf[0]
    name = mf[1]
    music_file = mf[2]
    music_image = mf[3]
    music_cover = mf[4]
    music = MUSIC(name=name,writer=writer,file_name=music_file,bg_images=music_image,cover=music_cover,init_pos=default_init_pos,test_y=650/1536*WIDTH,count=2,best_rank=music_inform[name])
    yueer_music.append(music)

theme1 = ["序章",theme_xuzhang_img,theme_xuzhang_bg,xuzhang_music]
theme2 = ["故事",theme_gushi_img,theme_gushi_bg,gushi_music]
theme3 = ["回忆",theme_huiyi_img,theme_huiyi_bg,huiyi_music]
theme4 = ["雨天",theme_yutian_img,theme_yutian_bg,yutian_music]
theme5 = ["古风",theme_gufeng_img,theme_gufeng_bg,gufeng_music]
theme6 = ["寻常",theme_xunchang_img,theme_xunchang_bg,xunchang_music]
theme7 = ["悦耳",theme_yueer_img,theme_yueer_bg,yueer_music]
theme8 = ["单曲",theme_danqu_img,theme_danqu_bg,danqu_music]

themelist = [theme1,theme2,theme3,theme4,theme5,theme6,theme7,theme8]

manager = ThemeManager(themelist)
setting = MUSICSETTING()

manager.init_themes()
cur = manager

def load(cur):
    cur.get_notes()
    cur.is_load = True
begin(user=user)
switch(cur,window=window)
cur.sound.play()

theme_state = 1
music_choice_state = 2
music_play_state = 3
music_end_state = 4

state = theme_state
setting_state = 0
score = 0

cur_FPS = FPS
cur_FPS_count = 0
time_start = time.time()
text = font.render("FPS: "+str(cur_FPS), True, (255, 255, 255))

while True: #  无限循环
    # print("is_run")    
    
    if time.time() - time_start > 1:
        time_start = time.time()
        cur_FPS = cur_FPS_count
        text = font.render("FPS: "+str(cur_FPS), True, (255, 255, 255))
        cur_FPS_count = 0
    
    cur_FPS_count += 1
    
    clock.tick(FPS) #  设置帧率为60

    for event in pygame.event.get(): #  获取事件
        if event.type == pygame.QUIT: #  如果事件类型为退出
            pygame.quit() #  退出pygame
            sys.exit() #  退出程序
        if user.show:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                user.show = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if pos[0] > 0 and pos[0] < WIDTH - 0.6*HEIGHT and pos[1] > 0 and pos[1] < HEIGHT:
                    user.show = False
        if user.check(event) == "User" and state != music_play_state:
            user.show = not user.show
        if user.show and user.check(event) == "Set":
            setting.choice = True
        if setting.choice:
            v,s = setting.is_check_set(event)
            original_FPS = FPS
            FPS = setting.FPS
            speed = speed * original_FPS/FPS
            if v != None: 
                pygame.mixer.music.set_volume(v)
                if state == theme_state:
                    cur.change_sound_volumn(v)
                elif state == music_choice_state:
                    cur.songs_list[cur.index[1]].change_sound_volumn(v)
                elif state == music_end_state:
                    cur.song.change_sound_volumn(v) 
        elif state == theme_state: #  如果当前状态为主题状态
            new_state = cur.change_theme(event) #  改变主题
            if new_state == 'set': #  如果新状态为设置
                setting.choice = True
            elif new_state != None: #  如果新状态不为空
                state = music_choice_state #  将状态设置为音乐选择状态 
                cur = new_state
                switch(cur,window=window) #  切换到新状态
                cur.start_music()
        elif state == music_choice_state: #  播放音乐
            new_state = cur.scroll(event)
            if new_state == 'theme': #  滚动选择
                state = theme_state
                window.fill((0,0,0))
                time.sleep(0.1)
                cur = cur.father_father
                threading.Thread(target=lambda: enter_music_effect.play()).start()
                switch(cur,window=window) #  获取父级父级
                cur.sound.play()
            elif new_state == 'music': #  播放声音
                state = music_play_state
                cur = cur.songs_list[cur.index[1]]
                if cur.is_load == False:
                    _load=threading.Thread(target=lambda : load(cur))
                    _load.start()
                window.fill((0,0,0))
                time.sleep(0.1)
                threading.Thread(target=lambda : cur.again()).start()         
                wait_to_load(cur,window)
                _load.join()
                time.sleep(2)
                score = 0
                cur.effect = setting.effect_state
                cur.replay_music()
                cur.play_music()
            elif new_state == 'set':
                setting.choice = True
        #鼠标按下
        elif state == music_play_state:
            score=cur.check_collision(event)
            if cur.is_check_setting(event,window) == 'Return':   
                state = music_choice_state      
                cur = cur.father
                threading.Thread(target=lambda: enter_music_effect.play()).start()
                switch(cur,window=window)
                cur.start_music()
        elif state == music_end_state:  
            # 检查当前状态是否被点击
            new_state = cur.check_clicked(event)
            # 如果当前状态被点击，并且点击的是返回按钮
            if new_state == 'return':
                # 将状态设置为音乐播放状态
                state = music_play_state
                # 将当前状态设置为当前歌曲
                cur = cur.song 
                # 重新播放音乐
                cur.replay_music()
                # 重新开始游戏
                cur.again()
                cur.effect = setting.effect_state
                # 播放音乐
                cur.play_music()
                # 分数重置为0
                score = 0
            # 如果当前状态被点击，并且点击的是继续按钮
            elif new_state == 'continue':
                # print('continue')
                # 将状态设置为音乐选择状态
                state = music_choice_state
                # 将当前状态设置为当前歌曲的父级
                cur = cur.song.father
                # 切换到当前歌曲的父级
                threading.Thread(target=lambda: enter_music_effect.play()).start()
                switch(cur,window=window)
                # 开始播放音乐
                cur.start_music()
            # 如果当前状态被点击，并且点击的是设置按钮
            elif new_state == 'set':
                setting.choice = True
    
    cur.draw(window)
        
    # 如果当前状态为音乐播放状态
    if state == music_play_state:
        # 检查碰撞
        score=cur.check_collision_longAndRains()
        # 检查是否超出边界
        cur.is_out_of_line()
        # 更新当前状态
        cur.update()
        # 如果游戏结束
        if cur.is_game_over():    
            # 将状态设置为音乐结束状态
            state = music_end_state
            # 保存当前状态
            temp=cur
            # 填充窗口为黑色
            window.fill((0,0,0))
            # 等待0.1秒
            time.sleep(0.1)
            # 创建新的音乐结束状态
            cur=MusicEnd(cur,cur.name,cur.cover,cur.bg,cur.score,cur.total_score,cur.perfect,cur.total-cur.perfect-cur.good,cur.good)
            # 保存音乐信息
            music_inform[temp.name]=cur.rank
            temp.best_rank=cur.rank
            save_music_inform(music_inform=music_inform,music_inform_path=music_inform_path)
            # 切换状态
            switch(cur,window=window)
    else:
        # 绘制用户
        user.draw(window)
        
    # 随机生成雨滴
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
            # 从列表中移除雨滴
            raindrops.remove(raindrop)
       
    # 如果设置选项被选中
    if setting.choice:
        # 绘制设置
        setting.draw(window)
       
    window.blit(text, (WIDTH - text.get_width() - 10, HEIGHT-text.get_height() - 10))
            
    pygame.display.update()
    