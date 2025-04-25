import pygame
from node import Ball, Particle, LONGBALL, RaindropBall
import time
import random
import threading
from Source import *

pygame.display.init()
pygame.mixer.init()
pygame.font.init()
WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
diff = 50/1536*WIDTH

sound_effect = pygame.mixer.Sound('./music/sound_effect.MP3')
stop_img = pygame.transform.scale(pygame.image.load('./image/stop.png'),(small_setting_length,small_setting_length))
continue_img = pygame.transform.scale(pygame.image.load('./image/continue.png'),(small_setting_length,small_setting_length))
return_img = pygame.transform.scale(pygame.image.load('./image/return.png'),(small_setting_length,small_setting_length))
music_pickle_dirs = "./musics_pickles" 
def get_bg_by_name(name):
    if name[0] == " ":
        name = name[1:]
    with open(music_pickle_dirs+"/"+name+"_bg.pkl", 'rb') as f:
        data = pickle.load(f)
        img = pygame.image.fromstring(data["image_bytes"], data["size"], 'RGBA')
        img = pygame.transform.scale(img,(WIDTH,HEIGHT))
    return img

def get_cover_by_name(name):
    if name[0] == " ":
        name = name[1:]
    with open(music_pickle_dirs+"/"+name+"_cover.pkl", 'rb') as f:
        data = pickle.load(f)
        img = pygame.image.fromstring(data["image_bytes"], data["size"], 'RGBA')
        img = pygame.transform.scale(img,(WIDTH//2,HEIGHT//2))
    return img

class MUSICPAUSER:

    def __init__(self):
        self.choice = False

    def draw(self,window):
        rect_surface = pygame.Surface((WIDTH//3, HEIGHT//3))
        rect_surface.set_alpha(200)
        rect_surface.fill((0,0,0))
        window.blit(rect_surface,(WIDTH//3,HEIGHT//3))
        window.blit(return_img,(WIDTH//3+WIDTH//12-36,HEIGHT//3+HEIGHT//6-36))
        window.blit(continue_img,(WIDTH//2+WIDTH//12-36,HEIGHT//3+HEIGHT//6-36))
        # x,y = pygame.mouse.get_pos()
        # window.blit(mouse,(x,y))
        
    def check(self,event):
        # 检查事件类型是否为鼠标点击事件
        if event.type == pygame.MOUSEBUTTONDOWN:
            # 检查鼠标点击的按钮是否为左键
            if event.button == 1:
                
                # 获取鼠标点击的位置
                pos = pygame.mouse.get_pos()
                # 检查鼠标点击的位置是否在第一个选项的范围内
                if WIDTH//3+WIDTH//12-36 <= pos[0] and pos[0] <= WIDTH//3+WIDTH//12+36 and HEIGHT//3+HEIGHT//6-36 <= pos[1] and pos[1] <= HEIGHT//3+HEIGHT//6+36:
                    # 设置选项为已选择
                    self.choice = True
                    # 返回'return'
                    return 'return'
                # 检查鼠标点击的位置是否在第二个选项的范围内
                elif WIDTH//2+WIDTH//12-36 <= pos[0] and pos[0] <= WIDTH//2+WIDTH//12+36 and HEIGHT//3+HEIGHT//6-36 <= pos[1] and pos[1] <= HEIGHT//3+HEIGHT//6+36:
                    # 设置选项为已选择
                    self.choice = True
                    # 返回'continue'
                    return 'continue'
                    
class MUSIC:
    def __init__(self, name,writer,cover,file_name, init_pos,count,bg_images, test_y, best_rank = "未开始"):
        '''
        :param name: 歌曲名
        :param writer: 歌手
        :param cover: 封面(圆角,路径)
        :param file_name: 歌曲文件名
        :param init_pos: 初始位置
        :param count: 初始数量
        :param bg_images: 背景图片
        :param test_y: 测试y轴
        '''
        self.name = name
        self.writer = writer
        self.cover = get_cover_by_name(name)
        self.bg = get_bg_by_name(name)
        self.music = file_name
        self.notes = []
        self.particles = []
        self.balls = []
        self.longballs = []
        self.raindrops = []
        self.init_pos = init_pos
        # self.start_time = None
        self.current_note_index = 0
        self.count = 0
        self.num = count
        # self.bg_images_name = bg_images
        # self.bg_images_index = 0
        self.test_y = test_y
        self.sound = pygame.mixer.Sound(self.music)
        self.sound_length = self.sound.get_length()*1000
        self.cur = 0
        self.continue_bit = 0
        self.score = 0
        self.total_score = 0
        self.font = pygame.font.Font("./font/SanJiLuRongTi/SanJiLuRongTi-2.ttf", int(50/1536*WIDTH))
        self.is_load = False
        self.perfect = 0
        self.good = 0
        self.total = 0
        self.best_rank = best_rank
        self.current_long_pos = []
        
    def get_notes(self):
        # y, sr = librosa.load(self.music)
        # tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
        # beat_times = librosa.frames_to_time(beat_frames, sr=sr)
        # for time in beat_times:
        #     # print(time * 1000 - self.test_y / (1000/60 * 5) * 1000)
        #     if time * 1000 - self.test_y / (1000/60 * speed) * 1000 > 0:
        #         self.notes.append(time * 1000 - self.test_y / (1000/60 * speed) * 1000)
        # print(len(self.notes))
        self.notes = music_note[self.name]


    def play_music(self):
        pygame.mixer.music.load(self.music)
        pygame.mixer.music.play()
        self.start_time = time.time() * 1000

    def play_sound(self):
        self.sound.play()
    
    def stop_music(self):
        pygame.mixer.music.stop()
    
    def again(self):
        self.score = 0
        self.perfect = 0
        self.good = 0
        self.current_note_index = 0
        self.continue_bit = 0
        self.total = 0
        self.total_score = 15
        self.longballs = []
        self.balls = []
        self.raindrops = []
        self.particles = []
        self.current_long_pos = []
        self.effect = True
        # self.init_balls()
        
    def replay_music(self):
        
        pygame.mixer.music.rewind()
    
    def continue_music(self):
        pygame.mixer.music.unpause()
    
    def pause_music(self):
        pygame.mixer.music.pause()
    
    def stop_sound(self):
        # print("stop")
        self.sound.stop()

    def change_sound_volumn(self,v):
        self.sound.set_volume(v)
        pygame.mixer.music.set_volume(v)

    def get_particles(self, x, y, color):
        for i in range(20):
            self.particles.append(Particle(x, y, color))

    def draw(self, window):
        
        window.blit(self.bg, (0, 0))
        window.blit(black, (0, 0))
        window.blit(stop_img,(25,40))
        
        pygame.draw.line(window, (255, 255, 255), (0, 0), (WIDTH*self.get_cur_pos(), 0), 4)
        
        continue_img = self.font.render("Continue: "+str(self.continue_bit), True, (255, 255, 255))
        score_img = self.font.render("Score: "+str(int(self.score)), True, (255, 255, 255))
        
        window.blit(continue_img,(WIDTH//2-continue_img.get_width()//2,75))
        window.blit(score_img,(WIDTH-score_img.get_width() - WIDTH //20,75))
        
        for ball in self.balls:
            # print(ball.y)
            ball.draw(window)
        
        for longball in self.longballs:
            longball.draw(window)
        
        for raindrop in self.raindrops:
            raindrop.draw(window)
            
        for particle in self.particles:
            particle.draw(window)    

    def is_valid(self,pos,current):
        for p in self.current_long_pos:
            # print(4,len(self.current_long_pos))
            if p[0] == pos[0] and p[1] + (current - p[2])/1000 * (1000/FPS * speed) <= 100:
                return False
            elif p[1] + (current - p[2])/1000 * (1000/FPS * speed) > 100:
                self.current_long_pos.remove(p)
        return True
                
    def update(self):
        current_time = (time.time() * 1000) - self.start_time
        # 根据节拍时间添加新的 Ball
        while self.current_note_index < len(self.notes) and current_time >= self.notes[self.current_note_index]:
            # print(current_time , self.notes[self.current_note_index])
            pos = random.choice(self.init_pos)
            choice = random.randint(0,10)
            count = 0
            if choice < 3:
                while not self.is_valid(pos, current_time) and count < 5:
                    pos = random.choice(self.init_pos)
                    count += 1    
                if count == 5:
                    self.current_note_index += 1
                    continue
                self.balls.append(Ball(pos[0], pos[1], (0, 0, 255), self.test_y))
                self.total_score += 5
                self.current_long_pos.append([pos[0],pos[1],current_time])
                self.total += 1
            elif choice < 9:
                while not self.is_valid(pos, current_time) and count < 5:
                    pos = random.choice(self.init_pos)
                    count += 1
                if count == 5:
                    self.current_note_index += 1
                    continue
                self.total += 1
                self.raindrops.append(RaindropBall(pos[0], pos[1], (0, 0, 255), 20, self.test_y))
                self.total_score += 5
                self.current_long_pos.append([pos[0],pos[1],current_time])
            else:
                while not self.is_valid(pos, current_time) and count < 5:
                    pos = random.choice(self.init_pos)
                    count += 1
                if count == 5:
                    self.current_note_index += 1
                    continue
                self.total += 1
                length = random.randint(100, 200)
                self.longballs.append(LONGBALL(pos[0], pos[1] - length, (0, 0, 255), length, self.test_y))
                self.total_score += 40
                self.current_long_pos.append([pos[0],pos[1]-length,current_time])
            
            self.current_note_index += 1

        for ball in self.balls:
            ball.update()
            if ball.y > HEIGHT:
                self.balls.remove(ball)

        for particle in self.particles:
            particle.update()
            if particle.size <= 0:
                self.particles.remove(particle)
        
        for longball in self.longballs:
            longball.update()
            if longball.y > HEIGHT:
                self.longballs.remove(longball)

        for raindrop in self.raindrops:
            raindrop.update()
            if raindrop.y > HEIGHT:
                self.raindrops.remove(raindrop)

    def is_out_of_line(self):
        # 遍历所有球
        for ball in self.balls:
            # 如果球的y坐标大于测试y坐标加上diff
            if ball.y > ball.test_y + diff:
                # 继续位设为0
                self.continue_bit = 0
                # 失球数加1
                # 从球列表中移除该球
                self.balls.remove(ball)
                # 获取粒子效果
                self.get_particles(ball.x + 25/1536*WIDTH, ball.y, (255, 0, 0))
                
        # 遍历所有长球
        for longball in self.longballs:
            # 如果长球的y坐标加上长度大于测试y坐标加上diff
            if longball.y + longball.length > longball.test_y + diff:
                # 如果长球没有赢或者没有开始
                if not longball.win and not longball.start:
                    # 继续位设为0
                    self.continue_bit = 0
                    # 从长球列表中移除该长球
                    self.longballs.remove(longball)
                    # 获取粒子效果
                    self.get_particles(longball.x+25/1536*WIDTH, longball.test_y, (255, 0, 0))
            # 如果长球的y坐标大于测试y坐标加上diff
            if longball.y > longball.test_y + diff:
                # 如果长球在长球列表中
                if longball in self.longballs:
                    # 从长球列表中移除该长球
                    self.longballs.remove(longball)

        # 遍历所有雨滴
        for raindrop in self.raindrops:
            # 如果雨滴的y坐标大于测试y坐标加上diff
            if raindrop.y > raindrop.test_y + diff:
                # 继续位设为0
                self.continue_bit = 0
                # 从雨滴列表中移除该雨滴
                self.raindrops.remove(raindrop)
                # 获取粒子效果
                self.get_particles(raindrop.x+25/1536*WIDTH, raindrop.y, (255, 0, 0))
                
    def check_collision(self, event):
        # 检测碰撞事件
        if event.type == pygame.KEYDOWN:
            # print("key pressed")
            # 获取当前按下的键的数量
            count = sum(pygame.key.get_pressed())
            # 遍历所有小球
            for ball in self.balls:
                # 测试小球是否碰撞
                test = ball.test()
                if test:
                    # 播放音效
                    if self.effect:
                        threading.Thread(target=sound_effect.play).start()
                    # 移除碰撞的小球
                    self.balls.remove(ball)
                    # 如果碰撞类型为1且按下的键数量大于0
                    if test == 1 and count > 0:
                        # 获取粒子效果
                        self.get_particles(ball.x+25/1536*WIDTH, ball.y, (0, 255, 0))
                        # 增加分数
                        self.score += 5
                        # 减少按下的键数量
                        count -= 1
                        # 增加连续击中次数
                        self.continue_bit += 1
                        # 增加完美击中次数
                        self.perfect += 1
                    # 如果按下的键数量大于0
                    elif count > 0:
                        # 获取粒子效果
                        self.get_particles(ball.x+25/1536*WIDTH, ball.y, (0, 0, 255))
                        # 增加分数
                        self.score += 1
                        # 减少按下的键数量
                        count -= 1
                        # 增加连续击中次数
                        self.continue_bit += 1
                        # 增加良好击中次数
                        self.good += 1
                    # 否则
                    else:
                        # 获取粒子效果
                        self.get_particles(ball.x+25/1536*WIDTH, ball.y, (255, 0, 0))
            # 遍历所有长球
            for longball in self.longballs:
                # 测试长球是否碰撞
                test = longball.test()
                # print("longball test")
                # 如果碰撞且按下的键数量大于0且长球未死亡
                if test and count > 0 and not longball.isdie:
                    # 开始长球
                    longball.start = True
                    # 增加连续击中次数
                    self.continue_bit += 1
                    # 增加完美击中次数
                    self.perfect += 1
                    # 如果长球长度小于100
                    if longball.length < 50/1536*WIDTH:
                        # 长球死亡
                        longball.isdie = True
                    # 减少按下的键数量
                    count -= 1
        # 返回分数
        return self.score

    def check_collision_longAndRains(self):
        # 获取当前按下的键
        keys = pygame.key.get_pressed()
        # 判断是否有键被按下
        is_any_key_pressed = any(keys)
        if is_any_key_pressed:
            # print("key pressed")
            # 计算被按下的键的数量
            count = sum(keys)
            # 遍历所有的longball
            for longball in self.longballs:
                # 测试longball是否碰撞
                test = longball.test()
                if test:
                    # 如果longball碰撞并且有键被按下并且被按下的键的数量大于0并且longball已经启动并且longball没有死亡
                    if test == 1 and is_any_key_pressed and count > 0 and longball.start and not longball.isdie:
                        # 如果longball没有胜利
                        if not longball.win:
                            # 设置longball胜利
                            longball.win = True
                            # 增加分数
                            self.score += longball.length/10 * 5
                            # 播放音效
                            if self.effect:
                                threading.Thread(target=sound_effect.play).start()
                        # 如果计数器是5的倍数
                        if self.count % 5 == 0:
                            # 获取粒子效果
                            self.get_particles(longball.x+25/1536*WIDTH, longball.test_y+25/1536*WIDTH, (0, 255, 0))
                        # 计数器加1
                        self.count += 1
                        # 被按下的键的数量减1
                        count -= 1
                    # 如果有键被按下并且被按下的键的数量大于0并且longball已经启动并且longball没有死亡
                    elif is_any_key_pressed and count > 0 and longball.start and not longball.isdie:
                        # 如果longball没有胜利
                        if not longball.win:
                            # 设置longball胜利
                            longball.win = True
                            # 增加分数
                            self.score += longball.length/10 * 1
                            # 播放音效
                            if self.effect:
                                threading.Thread(target=sound_effect.play).start()
                        # 如果计数器是5的倍数
                        if self.count % 5 == 0:
                            # 获取粒子效果
                            self.get_particles(longball.x+25/1536*WIDTH, longball.test_y+25/1536*WIDTH, (0, 255, 0))
                        # 计数器加1
                        self.count += 1
                        # 被按下的键的数量减1
                        count -= 1
            # 遍历所有的raindrop
            for raindrop in self.raindrops:
                # 测试raindrop是否碰撞
                test = raindrop.test()
                if test:
                    # 增加继续的次数
                    self.continue_bit += 1
                    # 增加完美的次数
                    self.perfect += 1
                    # print("raindrop test")
                    # 移除raindrop
                    self.raindrops.remove(raindrop)
                    # 如果raindrop碰撞并且有键被按下
                    if test == 1 and is_any_key_pressed:
                        # 播放音效
                        if self.effect:
                            threading.Thread(target=sound_effect.play).start()
                        # 获取粒子效果
                        self.get_particles(raindrop.x+25/1536*WIDTH, raindrop.y, (0, 255, 0))
                        # 增加分数
                        self.score += 5 
        # 返回分数
        return self.score
        
    def is_game_over(self):
        return pygame.mixer.music.get_busy() == 0
    
    def is_check_setting(self, event,window):
        # 检查是否点击了设置按钮
        if event.type == pygame.MOUSEBUTTONDOWN:
            # 获取鼠标点击位置
            pos = pygame.mouse.get_pos()
            # 判断鼠标点击位置是否在设置按钮范围内
            if pos[0] >= 25/1536*WIDTH and pos[0] <= 97/1536*WIDTH and pos[1] >= 40/1536*WIDTH and pos[1] <= 112/1536*WIDTH and event.button == 1:
                # 暂停音乐
                self.pause_music()
                # 创建设置界面
                musicpauser = MUSICPAUSER()
                # pygame.mouse.set_visible(True)
                # 循环等待用户选择
                while musicpauser.choice == False:
                    # 设置帧率
                    clock.tick(60)
                    # 获取事件
                    for event in pygame.event.get():
                        # 如果用户点击了关闭按钮
                        if event.type == pygame.QUIT:
                            # 退出游戏
                            pygame.quit()
                            sys.exit()
                        # 如果用户选择了继续游戏
                        if musicpauser.check(event)=="continue":
                            # 继续音乐
                            self.continue_music()
                            pygame.mouse.set_visible(False)
                            # 返回"NotReturn"，表示不返回主菜单
                            return "NotReturn"
                    # 绘制设置界面
                    musicpauser.draw(window)
                    # 更新显示
                    pygame.display.update()
                # 返回"Return"，表示返回主菜单
                # pygame.mouse.set_visible(False)
                return "Return"

    def set_father(self, father):
        self.father = father
                                 
    def get_cur_pos(self):
        """
        获取当前播放进度（以百分比表示）。

        Args:
            无

        Returns:
            float: 当前播放进度，以百分比表示。如果游戏已经结束，返回1。

        """
        if not self.is_game_over():
            self.cur = pygame.mixer.music.get_pos()
            return self.cur/self.sound_length
        return 1
    