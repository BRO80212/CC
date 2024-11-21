import random #используется для того, чтобы подключить модуль random, который предоставляет
            # функции для генерации случайных чисел и выборок элементов из последовательностей.
            #  Этот модуль является частью стандартной библиотеки Python и часто применяется при
            #  создании программ, где требуется элемент случайности.

import pygame as pg #import pygame as pg,  используется для переименования модуля pygame на pg.
                        # Это сделано для удобства написания кода и избежания конфликтов имен.

# делается для того, чтобы избежать конфликта имён классов при использовании
# нескольких библиотек одновременно. Например, в классе Meteotite
# происходит замена имён pg.sprite.Sprite на self. Это необходимо,
# потому что исходный код использует ту же библиотеку Pygame, которая также имеет класс Sprite,
# и чтобы избежать путаницы, имя класса изменяют на self.Sprite.

class Meteorite(pg.sprite.Sprite):  #класс метеоритов
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load("Meteor.png")
        size = random.randint(70, 150)   #генерация метеоритов с рандомным размером

        self.image = pg.transform.scale(self.image, (size, size))

        self.rect = self.image.get_rect()
        self.rect.topleft = (800, random.randint(0, 600 - size))

        self.speedx = random.randint(1, 3) #рандомное движение по скорости
        self.speedy = random.randint(-1, 1)

    def update(self):
        self.rect.x -= self.speedx   #задаем движение метеоритов справа на лево
        self.rect.y += self.speedy


class Mouse_starship(pg.sprite.Sprite):  #класс для звездолёта наших врагов
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load("StarShipMouse.png")
        size = random.randint(70, 150)

        self.image = pg.transform.scale(self.image, (size, size))
        self.image = pg.transform.flip(self.image, False, True)

        self.rect = self.image.get_rect()
        self.rect.midbottom = (random.randint(0, 600 - size), 0)

        self.speedx = random.randint(-1, +1)
        self.speedy = random.randint(1, 2)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy


class Laser(pg.sprite.Sprite):  #класс для нашего лазера
    def __init__(self, pos): #pos - это аргумент "позиция"
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load("Lazer.png")

        self.image = pg.transform.scale(self.image, (30, 30))

        self.rect = self.image.get_rect(midbottom=pos) #указываем что лазер должен вылетать из носа корабля (спавниться)

        self.speed = 2

    def update(self):
        self.rect.y -= self.speed


class Starship(pg.sprite.Sprite):  #класс для нашего звездолёта
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load("StarShipHorizontal.png") #загруж картинку звездолета
        self.image = pg.transform.scale(self.image, (100, 100))
        self.image = pg.transform.flip(self.image, False, True)

        self.rect = self.image.get_rect()
        self.rect.midleft = (0, 300)

        self.mode = "vertical"  #режим вертикальный

    def update(self):
        keys = pg.key.get_pressed()
        if self.mode == "horizontal": # настройка режима полёта звездолёта - горизонтально
            if keys[pg.K_a]:
                self.rect.x -= 1
            if keys[pg.K_d]:
                self.rect.x += 1

        if self.mode == "vertical":  # настройка режима полёта звездолёта - вертикально
            if keys[pg.K_w]:
                self.rect.y -= 1
            if keys[pg.K_s]:
                self.rect.y += 1

    def switch_mode(self):  # мотод для смены режима с вертикального на горизонтальный
        self.image = pg.image.load("StarShip.png")
        self.image = pg.transform.scale(self.image, (100, 100))

        self.rect = self.image.get_rect()
        self.rect.midbottom = (400, 580)

        self.mode = "horizontal"


class Captain(pg.sprite.Sprite):  #класс для капитана-кота
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load("Capitan.png")  #загружаем картинку
        self.image = pg.transform.scale(self.image, (400, 400)) #обозначаем координаты картинки

        self.rect = self.image.get_rect()
        self.rect.topleft = (-30, 600)

        self.mode = "up"

    def update(self):   #выдвигаем картинку наверх, пока она не достигнет 300
        if self.mode == "up":
            self.rect.y -= 3
            if self.rect.y <= 300:
                self.mode = "stay"


class Alien(pg.sprite.Sprite): #класс для иноплатнетного кота
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load("Alien_cat.png")
        self.image = pg.transform.scale(self.image, (400, 400))

        self.rect = self.image.get_rect()
        self.rect.topleft = (-30, 600)

        self.mode = "up"

    def update(self):
        if self.mode == "up":
            self.rect.y -= 3
            if self.rect.y <= 300:
                self.mode = "stay"
