from Source import *

pygame.init()
WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h

icon = pygame.transform.scale(pygame.image.load("./image/icon.png"), (100/1536*WIDTH, 100/1536*WIDTH))
userboard = pygame.transform.scale(pygame.image.load("./image/userboard.png"), (HEIGHT*0.6, HEIGHT))
board = pygame.transform.scale(pygame.image.load("./image/board.png"), (120/1536*WIDTH,120/1536*WIDTH))
font = pygame.font.Font("./font/SanJiLuRongTi/SanJiLuRongTi-2.ttf", int(30/1536*WIDTH))
font1 = pygame.font.Font("./font/SanJiLuRongTi/SanJiLuRongTi-2.ttf", int(20/1536*WIDTH))
return_img = pygame.transform.scale(pygame.image.load('./image/Userreturn.png'),(small_setting_length,small_setting_length))
set_img = pygame.transform.scale(pygame.image.load('./image/Userset.png'),(small_setting_length,small_setting_length))

authors = ["迷路的小朋友","正趣果上课","14911.","友人A","风笙"]
information = ["24级SYSU","24级FZU","24级CDUT","24级CMC","24级SWMU"]

class User:
    def __init__(self,name,icon_path,description):
        self.name = name
        self.show = False
        self.description = description
        self.icon = pygame.transform.scale(pygame.image.load(icon_path), (100/1536*WIDTH, 100/1536*WIDTH))
    def draw(self,window):
        if self.show:
            window.blit(userboard, (WIDTH - userboard.get_width(), 0))
            window.blit(board, (WIDTH - userboard.get_width(), 0))
            window.blit(self.icon, (WIDTH - userboard.get_width() + 10/1536*WIDTH, 10/1536*WIDTH))
            
            name = font.render("User: "+self.name, True, (0, 0, 0))
            window.blit(name, (WIDTH - userboard.get_width() // 2 - name.get_width() // 2, 50/1536*WIDTH))
            
            description = font.render("简介: "+self.description, True, (0, 0, 0))
            window.blit(description, (WIDTH - userboard.get_width() // 2 - description.get_width() // 2, 135/1536*WIDTH))
            
            about = font.render("创作者们: ", True, (0, 0, 0))
            window.blit(about, (WIDTH - userboard.get_width() + 100/1536*WIDTH, 220/1536*WIDTH))
            
            for i in range(len(authors)):
                author = font.render(authors[i], True, (0, 0, 0))
                window.blit(author, (WIDTH - userboard.get_width() // 3 - author.get_width() // 2 , 270/1536*WIDTH + 80*i))
            
            for i in range(len(information)):
                info = font1.render(information[i], True, (0, 0, 0))
                window.blit(info, (WIDTH - userboard.get_width() // 3 - info.get_width() // 2 , 300/1536*WIDTH + 80*i))
            window.blit(set_img,(WIDTH - set_img.get_width() - 25/1536*WIDTH,HEIGHT - set_img.get_height()*2 - 80/1536*WIDTH))
            
            window.blit(return_img,(WIDTH - return_img.get_width() - 25/1536*WIDTH,HEIGHT - return_img.get_height() - 40/1536*WIDTH))

        window.blit(icon, (WIDTH - icon.get_width() - 20/1536*WIDTH, 20/1536*WIDTH))    
        
    def check(self,event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if event.button == 1:
                if pos[0] > WIDTH - icon.get_width() - 20/1536*WIDTH and pos[0] < WIDTH - 20/1536*WIDTH and pos[1] > 20/1536*WIDTH and pos[1] < 20/1536*WIDTH + icon.get_height():
                    return "User"
                if pos[0] > WIDTH - userboard.get_width() and pos[0] < WIDTH - userboard.get_width() + board.get_width() and pos[1] > 0 and pos[1] < board.get_height():
                    set_user_imform(user_imform_path=user_inform_path)
                    self.name = user_imform["name"]
                    self.description = user_imform["description"]
                    self.icon = pygame.transform.scale(pygame.image.load(user_imform["icon_path"]), (100/1536*WIDTH, 100/1536*WIDTH))
                    return "Board"
                if pos[0] > WIDTH - set_img.get_width() - 25/1536*WIDTH and pos[0] < WIDTH - 25/1536*WIDTH and pos[1] > HEIGHT - set_img.get_height()*2 - 80/1536*WIDTH and pos[1] < HEIGHT - set_img.get_height() - 80/1536*WIDTH:
                    return "Set"
                if pos[0] > WIDTH - return_img.get_width() - 25/1536*WIDTH and pos[0] < WIDTH - 25/1536*WIDTH and pos[1] > HEIGHT - return_img.get_height() - 40/1536*WIDTH and pos[1] < HEIGHT - 40/1536*WIDTH:
                    pygame.quit()
                    sys.exit()
                