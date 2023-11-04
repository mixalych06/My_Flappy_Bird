import pygame as pg
from random import randint

pg.init()

RES = WIDTH, HEIGHT = 1000, 600
FPS = 60
play = True

window = pg.display.set_mode(RES)  # отображаемый экран
clock = pg.time.Clock()  # для отслеживания варемени
background = pg.image.load(r'images/app1.png').convert_alpha()


class Bird(pg.sprite.Sprite):
    def __init__(self, file_name, px=WIDTH // 4, py=HEIGHT // 2, ):
        pg.sprite.Sprite.__init__(self)
        self.px = px
        self.py = py
        self.file_name = file_name
        self.image = pg.image.load(self.file_name).convert_alpha()
        self.rect = pg.Rect(self.px, self.py, 30, 30)
        self.up = pg.K_SPACE
        self.speed = 0
        self.bird_rect = self.image.get_rect()

    def transform(self):
        if self.speed >= 0 and self.rect.y <= HEIGHT // 2:
            self.image = pg.image.load(self.file_name).convert_alpha()
            return
        elif self.speed < 0:
            self.image = pg.transform.rotate(pg.image.load(self.file_name).convert_alpha(), 45)
            return
        elif self.speed > 3:
            self.image = pg.transform.rotate(pg.image.load(self.file_name).convert_alpha(), 300)

    def update(self):
        if keys[self.up] and self.rect.y >= 0:
            self.transform()
            self.speed = -3
            self.rect.y -= self.speed + 5
            return
        elif self.rect.y <= 550:
            self.transform()
            self.speed += 0.3
            self.rect.y += self.speed

    def draw(self):
        pass


class Tree(pg.sprite.Sprite):
    r = 0
    speed_tree = 1

    def __init__(self, px, py):
        pg.sprite.Sprite.__init__(self)
        trees.append(self)
        self.px = px
        self.py = py
        self.file_name = r'images/pipe.png'
        if Tree.r % 2 == 0:
            self.image = pg.image.load(self.file_name)

        else:
            self.image = pg.transform.flip(pg.image.load(self.file_name), False, True)
        self.rect = pg.Rect(self.px, self.py, 89, 420)

    def update(self):
        self.rect.x -= Tree.speed_tree


bird = Bird(file_name=r'images/bird1.png')
trees = []
gener_tree = 0

while play:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            play = False
    keys = pg.key.get_pressed()

    window.blit(background, (0, 0))
    gener_tree += 1
    if gener_tree >= 240:
        yq = randint(-100, 100)
        zq = randint(25, 80)
        Tree(1000, 300 + yq)
        Tree.r += 1
        Tree(1000, 300 + yq - 500 - zq)
        Tree.r += 1
        gener_tree = 0

    for tree in trees:
        window.blit(tree.image, tree.rect)

        if tree.rect.colliderect(bird.rect):

            Tree.speed_tree = 0
        tree.update()

    bird.update()
    window.blit(bird.image, bird.rect)
    pg.display.update()
    clock.tick(FPS)
