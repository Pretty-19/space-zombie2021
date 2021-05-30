from enemies.zombie import Zombie
from enemies import enemy
import pygame
import os

class Game:
    def __init__(self):
        self.width = 1350
        self.height = 700
        self.win = pygame.display.set_mode((self.width, self.height ))
        self.enemys = [Zombie()]
        self.lives = 10
        self.money = 2000
        self.back_ground=pygame.image.load(r'D:\Projects\game-cad\game_assets\rocketImages\bg_path.jpg')
        self.back_ground = pygame.transform.scale(self.back_ground, (self.width, self.height))
        self.clicks=[]
        self.pause = True

    def run(self):
                run=True
                clock =pygame.time.Clock()
                while run:
                    clock.tick(100)
                    for event in pygame.event.get():
                        if event.type ==pygame.QUIT:
                            run =False
                        pos=pygame.mouse.get_pos()
                        #if   event.type ==pygame.MOUSEBUTTONDOWN:
                            #self.clicks.append(pos)
                            #print(pos)
                        if not self.pause:
                                    to_del = []
                                    for en in self.enemys:
                                          en.move()
                                          if en.x < -15:
                                             to_del.append(en)
                    self.draw_win()
                pygame.quit()



    def draw_win(self):
        self.win.blit(self.back_ground,(0,0))
        #for p in self.clicks:
               # pygame.draw.circle(self.win,(255,0,0),(p[0],p[1]),5,0)
        #WIN.fill((0,0,128))
        for en in self.enemys:
              en.draw(self.win)
        pygame.display.update()

   
g=Game()
g.run()
