import pygame
import sys
from os import path
pygame.init()

window_width = 1200
window_height = 600

#get_mask

fps = 30
black = (0, 0, 0)
green = (0, 255, 0)
flame_rate = 25

cactus_img = pygame.image.load(r'Images\cactus_bricks.png')
cactus_img_mask = cactus_img.get_mask()
cactus_img_mask.left = 0

fire_img = pygame.image.load(r'Images\fire_bricks.png')
fire_img_rect = fire_img.get_rect()
fire_img_rect.left = 0

clock = pygame.time.Clock()
font = pygame.font.SysFont('forte', 20)

canvas = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Mario')


class Topscore:

    def __init__(self):
        self.high_score = 0

    def top_score(self, score):
        if score > self.high_score:
            self.high_score = score
        return self.high_score


topscore = Topscore()


class Dragon:

    dragon_velocity = 10

    def __init__(self):
        self.dragon_img = pygame.image.load(r'Images\dragon.png')
        self.dragon_img_rect = self.dragon_img.get_rect()
        self.dragon_img_rect.width -= 10
        self.dragon_img_rect.height -= 10
        self.dragon_img_rect.top = window_height/2
        self.dragon_img_rect.right = window_width
        self.up = True
        self.down = False

    def update(self):
        canvas.blit(self.dragon_img, self.dragon_img_rect)
        if self.dragon_img_rect.top <= cactus_img_rect.bottom:
            self.up = False
            self.down = True
        elif self.dragon_img_rect.bottom >= fire_img_rect.top:
            self.up = True
            self.down = False

        if self.up:
            self.dragon_img_rect.top -= self.dragon_velocity
        elif self.down:
            self.dragon_img_rect.top += self.dragon_velocity


class Flames:

    flames_velocity = 20

    def __init__(self):
        self.flames = pygame.image.load(r'Images\fireball.png')
        self.flames_img = pygame.transform.scale(self.flames, (20, 20))
        self.flames_img_rect = self.flames_img.get_rect()
        self.flames_img_rect.right = dragon.dragon_img_rect.left
        self.flames_img_rect.top = dragon.dragon_img_rect.top + 30


    def update(self):
        canvas.blit(self.flames_img, self.flames_img_rect)

        if self.flames_img_rect.left > 0:
            self.flames_img_rect.left -= self.flames_velocity


class Mario:

    velocity = 10

    def __init__(self):
        self.mario_img = pygame.image.load(r'Images\mario.png')
        self.mario_img_rect = self.mario_img.get_rect()
        self.mario_img_rect.left = 20
        self.mario_img_rect.top = window_height/2 - 100
        self.down = True
        self.up = False

    def update(self):
        canvas.blit(self.mario_img, self.mario_img_rect)
        if self.mario_img_rect.top <= cactus_img_rect.bottom:
            game_over()
            if score > self.mario_score:
                self.mario_score = score
        if self.mario_img_rect.bottom >= fire_img_rect.top:
            game_over()
            if score > self.mario_score:
                self.mario_score = score
        if self.up:
            self.mario_img_rect.top -= 10
        if self.down:
            self.mario_img_rect.bottom += 10

def write_to_file():
        str_highest_score = ''.join(str(score_in_file[-1]))
        if str(topscore.high_score) > str_highest_score:
            with open('High_Score.txt', 'a', encoding = 'utf-8') as file:
                hs = int(topscore.high_score)
            file.write('\n' + str(hs))


def game_over():
    pygame.mixer.music.stop()
    music = pygame.mixer.Sound(r'Music\mario_dies.wav')
    music.play()
    topscore.top_score(score)
    game_over_img = pygame.image.load(r'Images\end.png')
    game_over_img_rect = game_over_img.get_rect()
    game_over_img_rect.center = (window_width/2, window_height/2)
    canvas.blit(game_over_img, game_over_img_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                write_to_file()
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.QUIT:
                    write_to_file()
                    pygame.quit()
                    sys.exit()
                music.stop()
                game_loop()
        pygame.display.update()


def start_game():
    global highest_score
    global score_in_file
    canvas.fill(black)
    start_img = pygame.image.load(r'Images\start.png')
    start_img_rect = start_img.get_rect()
    start_img_rect.center = (window_width/2, window_height/2)
    canvas.blit(start_img, start_img_rect)

    with open('High_Score.txt') as f:
        w = [int(x) for x in next(f).split()]
        score_in_file = [[int(x) for x in line.split()]for line in f]
        highest_score = score_in_file[-1]
        f.close()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                write_to_file()
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    write_to_file()
                    pygame.quit()
                    sys.exit()
                game_loop()
        pygame.display.update()


def check_level(score):
    global level
    if score in range(0, 10):
        cactus_img_rect.bottom = 50
        fire_img_rect.top = window_height - 50
        level = 1
    elif score in range(10, 20):
        cactus_img_rect.bottom = 100
        fire_img_rect.top = window_height - 100
        level = 2
    elif score in range(20, 30):
        cactus_img_rect.bottom = 150
        fire_img_rect.top = window_height - 150
        level = 3
    elif score > 30:
        cactus_img_rect.bottom = 200
        fire_img_rect.top = window_height - 200
        level = 4


def game_loop():
    while True:
        global dragon
        global score
        dragon = Dragon()
        flames = Flames()
        mario = Mario()
        flame_counter = 0
        score = 0
        flames_list = []
        pygame.mixer.music.load(r'Music\mario_theme.wav')
        pygame.mixer.music.play(-1, 0.0)

        while True:
            canvas.fill(black)
            check_level(score)
            dragon.update()
            flame_counter += 1

            if flame_counter == flame_rate:
                flame_counter = 0
                new_flame = Flames()
                flames_list.append(new_flame)
            for f in flames_list:
                if f.flames_img_rect.left <= 0:
                    flames_list.remove(f)
                    score += 1
                f.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        mario.up = True
                        mario.down = False
                    elif event.key == pygame.K_DOWN:
                        mario.down = True
                        mario.up = False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        mario.up = False
                        mario.down = True
                    elif event.key == pygame.K_DOWN:
                        mario.down = True
                        mario.up = False

            score_font = font.render('Score:'+str(score), True, green)
            score_font_rect = score_font.get_rect()
            score_font_rect.center = (200, cactus_img_rect.bottom + score_font_rect.height/2)
            canvas.blit(score_font, score_font_rect)

            level_font = font.render('Level:'+str(level), True, green)
            level_font_rect = level_font.get_rect()
            level_font_rect.center = (400, cactus_img_rect.bottom + score_font_rect.height/2)
            canvas.blit(level_font, level_font_rect)

            top_score_font = font.render('Top Score:'+str(topscore.high_score),True, green)
            top_score_font_rect = top_score_font.get_rect()
            top_score_font_rect.center = (600, cactus_img_rect.bottom + score_font_rect.height/2)
            canvas.blit(top_score_font, top_score_font_rect)

            highest_score_font = font.render('Highest Score:'+str(highest_score).strip('[').strip(']'), True, green)
            highest_score_font_rect = highest_score_font.get_rect()
            highest_score_font_rect.center = (800, cactus_img_rect.bottom + score_font_rect.height/2)
            canvas.blit(highest_score_font, highest_score_font_rect)

            canvas.blit(cactus_img, cactus_img_rect)
            canvas.blit(fire_img, fire_img_rect)
            mario.update()

            for f in flames_list:
                if f.flames_img_rect.colliderect(mario.mario_img_rect):
                    game_over()
                    if score > mario.mario_score:
                        mario.mario_score = score
            pygame.display.update()
            clock.tick(fps)

start_game()
