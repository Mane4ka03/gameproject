import pygame, sys, random #импортирую необходимые библиотеки

pygame.display.set_caption('Flappy bird') #создаем название рабочего окна
pygame.init()  #запуск рабочего окна
screen = pygame.display.set_mode((580, 1000)) # создание рабочего окна
clock = pygame.time.Clock()
game_font = pygame.font.SysFont('Colibli', 60) #шрифт игры

gravity = 0.25   #гравитация птички
birdmov = 0 #движение пртицы
game_active = True
score = 0 #счет
high_score = 0 #лучший счет
can_score = True
bg = pygame.image.load('background.png').convert() #загрузка фона игры и конвертация
tubesu = pygame.image.load('tube.png')
message = pygame.transform.scale2x(pygame.image.load('message.png').convert_alpha())


# загрузка картинок для птички и конвертация их под удобный для питона формат
bird_downflap = pygame.transform.scale2x(pygame.image.load('bird3.png').convert_alpha())
bird_midflap = pygame.transform.scale2x(pygame.image.load('bird2.png').convert_alpha())
bird_upflap = pygame.transform.scale2x(pygame.image.load('bird1.png').convert_alpha())
bird_frames = [bird_downflap, bird_midflap, bird_upflap] # создание листа, где будут хранится состояния птицы для анимации
bird_index = 0
birds = bird_frames[bird_index]
birdr = birds.get_rect(center=(90, 512))

birdfl = pygame.USEREVENT + 1
pygame.time.set_timer(birdfl, 200)


message_r = message.get_rect(center=(288, 512)) #расположение итогового окна
tubesu = pygame.transform.scale2x(tubesu)
tubel = []
sptube = pygame.USEREVENT
pygame.time.set_timer(sptube, 1200)
tube_height = [500, 700, 800] #доступные высоты расположения высоты




eventscore = pygame.USEREVENT + 2
pygame.time.set_timer(eventscore, 100)

def rotate_bird(bird):       #вращение птички
    #new_bird - расположение квадрата птицы
    new_bird = pygame.transform.rotozoom(bird, -birdmov * 5, 1)
    return new_bird

def create_tube():
    # bottom tube - позиция нижней трубы
    # top_tube - позиция верхней трубы
    _tube_pos = random.choice(tube_height) #выбираем рандомную позицию для трубы
    bottom_tube = tubesu.get_rect(midtop=(600, _tube_pos))
    top_tube = tubesu.get_rect(midbottom=(600, _tube_pos - 300)) #создание расстояния между трубами
    return bottom_tube, top_tube


def moving_tube(tubes): #функция отвечающая за передвижение труб
    # visible_tubes - движение трубы
    for tube in tubes:
        tube.centerx -= 5
    visible_tubes = [tube for tube in tubes if tube.right > -50]
    return visible_tubes


def print_tubes(tubes):  #отрисовка труб
    for tube in tubes:
        if tube.bottom >= 1000:
            screen.blit(tubesu, tube)
        else:
            flip_tube = pygame.transform.flip(tubesu, False, True) #переворачиваем трубу по у
            screen.blit(flip_tube, tube)


def check(tubes):    #если птица сталкивается с трубой
    global can_score
    for tube in tubes:
        if birdr.colliderect(tube):
            can_score = True
            return False

    if birdr.top <= -100 or birdr.bottom >= 1000:
        can_score = True
        return False

    return True


def bird_animation():         #смена картинок птицы для анимации
    # new_bird - картинка птицы
    #new_birdr - расположение картинки птицы
    new_bird = bird_frames[bird_index]
    new_birdr = new_bird.get_rect(center=(100, birdr.centery))
    return new_bird, new_birdr


def score_display(game_state): # функция подсчета счета
    if game_state == 'main_game':
        score_surface = game_font.render(f'Текущий счет:{int(score)}', True, (100, 0, 0))  #подсчет счета в самой игре и выбор цвета
        score_rect = score_surface.get_rect(center=(280, 100)) #расположение счета
        screen.blit(score_surface, score_rect)
    if game_state == 'game_over':
        score_surface = game_font.render(f'Счет игры: {int(score)}', True, (100, 0, 0)) #если игра заканчивается, то на экране появляется счет завершенной игры
        score_rect = score_surface.get_rect(center=(280, 850))
        screen.blit(score_surface, score_rect)

        high_score_surface = game_font.render(f'Лучший счет игры: {int(high_score)}', True, (100, 0, 0)) # полсчет лучшего счета
        high_score_rect = high_score_surface.get_rect(center=(280, 100))
        screen.blit(high_score_surface, high_score_rect)


def new_score(score, high_score):  #функция обновления счета
    # hight_score - обновление лучшего счета
    if score > high_score:    #если текущий счет игры становится больше чем лучший счет, то он обновляется
        high_score = score
    return high_score


def tube_check():            #функция проверки счета и его увеличения при пролетании трубы
    global score, can_score

    if tubel:
        for tube in tubel:
            if 95 < tube.centerx < 105 and can_score:
                score += 1
                can_score = False
            if tube.centerx < 0:
                can_score = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:              #если зажата клавиша
            if event.key == pygame.K_SPACE and game_active:
                birdmov = 0
                birdmov -= 7
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                tubel.clear()
                birdr.center = (100, 512)
                birdmov = 0
                score = 0

        if event.type == sptube:
            tubel.extend(create_tube())

        if event.type == birdfl:
            if bird_index < 2:
                bird_index += 1
            else:
                bird_index = 0

            birds, birdr = bird_animation()

    screen.blit(bg, (0, 0))

    if game_active:

        birdmov += gravity               #физические составляющие игры
        rotated_bird = rotate_bird(birds)
        birdr.centery += birdmov
        screen.blit(rotated_bird, birdr)

        game_active = check(tubel)


        tubel = moving_tube(tubel)
        print_tubes(tubel)


        tube_check()
        score_display('main_game')
    else:
        screen.blit(message, message_r)
        high_score = new_score(score, high_score)
        score_display('game_over')


    pygame.display.update()  #обновление экрана игры
    clock.tick(130) #кол-во кадров в секунду


