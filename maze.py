from pygame import *
mixer.init()
font.init()

window_x, window_y = 700, 500
background = transform.scale(image.load('background.jpg'), (window_x, window_y))

mixer.music.load('jungles.ogg')
mixer.music.play()
money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

'''kick = mixer.Sound('kick.ogg')
kick.play()'''

window = display.set_mode((window_x, window_y))
display.set_caption('Лабиринт')

clock = time.Clock()
FPS = 60

finish = False

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
    
        if keys[K_DOWN] and self.rect.y < window_y - 80:
            self.rect.y += self.speed
    
        if keys[K_RIGHT] and self.rect.x < window_x - 80:
            self.rect.x += self.speed

        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x >= window_x - 85:
            self.direction = 'left'
        
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color1, color2, color3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color1, color2, color3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
    
    


player = Player('hero.png', 5, window_y - 90, 4)
enemy = Enemy('cyborg.png', window_x - 80, 280, 2)
treasure = GameSprite('treasure.png', window_x - 380, window_y - 90, 0)

wall1 = Wall(0, 255, 200, 100, 20, 450, 10)
wall2 = Wall(0, 255, 200, 100, 480, 350, 10)
wall3 = Wall(0, 255, 200, 100, 20, 10, 380)
wall4 = Wall(0, 255, 200, 250, 125, 10, 365)
wall5 = Wall(0, 255, 200, 250, 200, 300, 10)
wall6 = Wall(0, 255, 200, 400, 30, 10, 85)
wall7 = Wall(0, 255, 200, 440, 200, 10, 50)
wall8 = Wall(0, 255, 200, 440, 330, 10, 150)
wall9 = Wall(0, 255, 200, 540, 125, 10, 80)

font = font.SysFont('Arial', 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0))



game = True
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0, 0) )

        player.update()
        player.reset()

        enemy.reset()
        enemy.update()

        treasure.reset()

        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        wall4.draw_wall()
        wall5.draw_wall()
        wall6.draw_wall()
        wall7.draw_wall()
        wall8.draw_wall()
        wall9.draw_wall()

        if sprite.collide_rect(player, treasure):
            finish = True
            window.blit(win, (200, 200))
            money.play()

        if sprite.collide_rect(player, enemy) or sprite.collide_rect(player, wall1) or sprite.collide_rect(player, wall2) or sprite.collide_rect(player, wall3) or sprite.collide_rect(player, wall4) or sprite.collide_rect(player, wall5) or sprite.collide_rect(player, wall6) or sprite.collide_rect(player, wall7) or sprite.collide_rect(player, wall8) or sprite.collide_rect(player, wall9):
            finish = True
            window.blit(lose, (200, 200))
            kick.play()
        

    

    clock.tick(FPS)
    display.update()