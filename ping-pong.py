from pygame import *
from random import *
import os

#окно игры
window = display.set_mode((1250, 720))
display.set_caption("PING-PONG")

#задай фон сцены
dir = os.path.dirname(os.path.abspath(__file__))
dir = dir + "/"
dir_platform = dir + "platform.png"
dir_ball = dir + "ball.png"
dir_background = dir + "background.jpg"
dir_musick = dir + "theme.mp3"

background = transform.scale(image.load(dir_background), (1250, 720))

def text():
    window.blit(background, (0, 0))

#class
class GameSprite(sprite.Sprite):
   #конструктор класса
    def __init__(self, p_image, player_x, player_y, w, h):
       super().__init__()
       # каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(p_image), (w, h))
       self.speed = 5
       # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
       self.speed_y = 5
       self.speed_x = 5

    def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        if  ball.rect.y == 0:
            self.speed_y *= -1

        if ball.rect.y == 670:
            self.speed_y *= -1
        
        if ball.rect.colliderect(rocket_1.rect):
            self.speed_x *= -1
        
        if ball.rect.colliderect(rocket_2.rect):
            self.speed_x *= -1

        ball.rect.x += self.speed_x
        ball.rect.y += self.speed_y
        
rocket_1 = GameSprite(dir_platform, 0, 0, 35, 130)
rocket_2 = GameSprite(dir_platform, 1215, 0, 35, 130)
ball = Player(dir_ball, 625, 360, 50, 50)

#additionally
clock = time.Clock()
FPS = 60
mixer.init()
mixer.music.load(dir_musick)
mixer.music.play()

font.init()
font = font.Font(None, 30)

#game code
finish = False
game = True
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        text()
        ball.update()
        ball.reset()
        rocket_1.update()
        rocket_1.reset()
        rocket_2.update()
        rocket_2.reset()

        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and rocket_1.rect.y >= 5:
            rocket_1.rect.y -= rocket_1.speed
        if keys_pressed[K_s] and rocket_1.rect.y <= 585:
            rocket_1.rect.y += rocket_1.speed

        if keys_pressed[K_UP] and rocket_2.rect.y >= 5:
            rocket_2.rect.y -= rocket_2.speed
        if keys_pressed[K_DOWN] and rocket_2.rect.y <= 585:
            rocket_2.rect.y += rocket_2.speed

        #win-lose
        if ball.rect.x < 0:
            finish = True
            win = font.render("Win 1st player!", True, (255, 255, 255))
            window.blit(win, (200, 200))
        if ball.rect.x > 1250:
            finish = True
            win = font.render("Win 2rd player!", True, (255, 255, 255))
            window.blit(win, (200, 200))
    display.flip()
    clock.tick(FPS)