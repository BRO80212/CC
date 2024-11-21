import time
from sprite import *

# функ-я которая избавит нас от повторения кода
def dialogue_mode(sprite, text): #ниже меняем start_text  на text - тот список текста который будет использоваться в функции в конкретной сцене
    sprite.update() #здесь наш спрайт должен появляться и обновляться
    screen.blit(space, (0, 0))  # отрисовка фона на сцене экрана
    screen.blit(sprite.image, sprite.rect) #и  спрайт должен прогружаться с картинкой и в координаты

    text1 = f1.render(text[text_number], True, pg.Color("white"))  # выводим-создаем (render) текст на экране. True - сглаживание, цвет - белый.
    screen.blit(text1, (280, 450))  # текст буквально отрисовывается на экране как фото через скрин-блит
    if text_number < len(text) - 1:  # выводим вторую фразу если она вобще существует
        text2 = f1.render(text[text_number + 1], True, pg.Color("white"))  # выводим-создаем вторую фразу
        screen.blit(text2, (280, 470))  # 470 чтобы вторая строчка была пониже


pg.init()
pg.mixer.init()

size = (800, 600) # Установка окна
screen = pg.display.set_mode(size) # Установка окна
pg.display.set_caption("Космические коты") # Установка окна

FPS = 120 #Это значение указывает частоту кадров в секунду (Frames Per Second), которая определяет,
          # сколько раз в секунду будет обновляться экран. Чем выше это значение, тем плавнее будут
        # выглядеть движения на экране. Однако, слишком высокое значение может привести к повышенной
        # нагрузке на систему.
clock = pg.time.Clock() #Объект Clock используется для управления временными интервалами в программе.
                        # Он позволяет синхронизировать обновления экрана и другие события с реальным
                        # временем, что важно для создания интерактивного приложения.


is_running = True #переменная is_running - пока она True - основной цикл игры работает
mode = "start_scene" #режим.  С помощью переменной mode переключается сцена

meteorites = pg.sprite.Group() # группа для спрайта
mice = pg.sprite.Group() # группа для спрайта
lasers = pg.sprite.Group() # группа для спрайта

space = pg.image.load("Background.png").convert() #загружаем фон на экран
space = pg.transform.scale(space, size) # растягиваем фон на размер экрана size

heart = pg.image.load("Heart.png").convert_alpha() #подгружаем картинку сердец и конвертируем через КОНВЕРТ-АЛЬФА потому что у картинки есть прозрачный фон
heart = pg.transform.scale(heart, (30, 30)) #адаптируем размер
heart_count = 3

capitan = Captain()  #создаём капитана (он в sprite.py)
alien = Alien() #создаём инопланетянина (он в sprite.py)
starship = Starship()


start_text = ["Мы засекли сигнал с планеты Мур.",
              "",
              "Наши друзья, инопланетные коты,",
              "нуждаются в помощи.",
              "Космические мыши хотят съесть их луну,",
              "потому что она похожа на сыр.",
              "Как долго наш народ страдал от них, ",
              "теперь и муряне в беде...",
              "Мы должны помочь им.",
              "Вылетаем прямо сейчас.",
              "Спасибо, что починил звездолёт, штурман. ",
              "Наконец-то функция автопилота работает.",
              "Поехали!"]

alien_text = ["СПАСИТЕ! МЫ ЕЛЕ ДЕРЖИМСЯ!",
              "",
              "Мыши уже начали грызть луну...",
              "Скоро куски луны будут падать на нас.",
              "Спасите муриан!", ]

final_text = ["Огромное вам спасибо,",
              "друзья с планеты Мяу!",
              "Как вас называть? Мяуанцы? Мяуриане?",
              "В любом случае, ",
              "теперь наша планета спасена!",
              "Мы хотим отблагодарить вас.",
              "Капитан Василий и его штурман получают",
              "орден SKYSMART.",
              "А также несколько бутылок нашей",
              "лучшей валерьянки.",
              "",
              ""]

text_number = 0  #переменная text_number устанавливает какой номер фразы выводить на экран
f1 = pg.font.Font("Fonts.otf", 25)  #25й шрифт  (если в скобках None - то используем стандартный шрифт системы

pg.mixer.music.load("Music.wav")
pg.mixer.music.set_volume(0.2)
pg.mixer.music.play()

laser_sound = pg.mixer.Sound("LazerSound.wav")
win_sound = pg.mixer.Sound("WinSound.wav")

while is_running:   # основной цикл с кодом

    # СОБЫТИЯ
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False
        if event.type == pg.KEYDOWN:  #если нажимаем любу. кнопку на клавиатуре

            if mode == "start_scene": # и если мы в режиме стартовой сцены
                text_number +=2 #прибавляем 2 для перехода на следующую фразу
                if text_number > len(start_text): #если номер text_number больше общего кол-ва фраз то -
                    text_number = 0 # то сбрасываем переменную в ноль, т.к. след-ий режим у нас метеориты
                    mode = "meteorites"
                    start_time = time.time()

            if mode == "alien_scene": # и если мы в режиме ALIEN сцены
                text_number +=2 #прибавляем 2 для перехода на следующую фразу
                if text_number > len(alien_text): #если номер text_number больше общего кол-ва фраз то -
                    text_number = 0 # то сбрасываем переменную в ноль, т.к. след-ий режим у нас метеориты
                    alien.rect.topleft = (-30, 600) #скопировали это из sprite.py  чтобы Alien снова выезжал снизу-вверх
                    alien.mode = "up" #скопировали это из sprite.py  чтобы Alien снова выезжал снизу-вверх
                    mode = "moon"
                    start_time = time.time()
                    starship.switch_mode()

            if mode == "moon":
                if event.key == pg.K_SPACE:
                    lasers.add(Laser(starship.rect.midtop))
                    laser_sound.play()

            if mode == "final_scene": # и если мы в режиме ALIEN сцены
                text_number +=2 #прибавляем 2 для перехода на следующую фразу
                if text_number > len(final_text): #если номер text_number больше общего кол-ва фраз то -
                    text_number = 0 # то сбрасываем переменную в ноль, т.к. след-ий режим у нас метеориты
                    mode = "end"

    # ОБНОВЛЕНИЯ   (прописаны условия для каждого из режимов)
    if mode == "start_scene":  #стартовая сцена
        dialogue_mode(capitan, start_text)  #вставляем функцию вместо прежнего текста

    if mode == "meteorites": #сцена с метеоритами
        if time.time() - start_time > 5.0:
            mode = "alien_scene"

        if random.randint(1, 50) == 1: #генерация метеоритов (вероятность возникновения метеоритов)
            meteorites.add(Meteorite())


        starship.update() #обновляем звездолёт
        meteorites.update() #обновляем метеориты

        hits = pg.sprite.spritecollide(starship, meteorites, True) # столкновение зведолета с метеоритами.  В скобках Спрайт-ГруппаСпрайтов-Удалять-или-нет-элемент группы)
        for hit in hits: #цикл для изменения сердечек
            heart_count -= 1 # при каждом столкновени с метеоритом сердечко исчезает
            if heart_count <= 0: #ыы если сердечек = 0
                is_running = False  #  то основной цикл программы останавливается

        screen.blit(space, (0, 0))
        screen.blit(starship.image, starship.rect) #отрисовка звездолета
        meteorites.draw(screen) #отрисовка метеоритов

        for i in range(heart_count): #отрисовываем сердечки с помощью цикла
            screen.blit(heart, (i*30, 0)) # 1-е сердечко в 0 по иксу, 2-е в 60, 3-е 90

    if mode == "alien_scene": # сцена с инопланетянином
        dialogue_mode(alien, alien_text)

    if mode == "moon":  # лунная сцена
        if time.time() - start_time > 5.0:
            mode = "final_scene"
            pg.mixer.music.fadeout(3)
            win_sound.play()

        if random.randint(1, 50) == 1:  # генерация метеоритов (вероятность возникновения метеоритов)
            mice.add(Mouse_starship())

        starship.update()  # обновляем звездолёт
        mice.update()  # обновляем метеориты
        lasers.update() # обновляем лазеры

        hits = pg.sprite.spritecollide(starship, mice,True)  # столкновение зведолета с метеоритами.  В скобках Спрайт-ГруппаСпрайтов-Удалять-или-нет-элемент группы)
        for hit in hits:  # цикл для изменения сердечек
            heart_count -= 1  # при каждом столкновени с метеоритом сердечко исчезает
            if heart_count <= 0:  # ыы если сердечек = 0
                is_running = False  # то основной цикл программы останавливается

        hits = pg.sprite.groupcollide(lasers, mice, True, True) #group потомучто столкновение двух групп а не спрайта и группы

        screen.blit(space, (0, 0))
        screen.blit(starship.image, starship.rect)  # отрисовка звездолета
        mice.draw(screen)  # отрисовка метеоритов
        lasers.draw(screen) # отрисовка лазеров

        for i in range(heart_count):  # отрисовываем сердечки с помощью цикла
            screen.blit(heart, (i * 30, 0))  # 1-е сердечко в 0 по иксу, 2-е в 60, 3-е 90

    if mode == "final_scene":  #финальная сцена где вас похвалят
        dialogue_mode(alien, final_text)

    pg.display.flip()  #обновления экрана
    clock.tick(FPS)    #обновления экрана
