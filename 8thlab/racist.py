import pygame
import random
import sys

pygame.init()

# Параметры экрана и общие константы
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer: Противники и монеты с весом")

clock = pygame.time.Clock()
FPS = 60

# Цвета
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Размеры машин игрока и противников
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 100
OPPONENT_WIDTH, OPPONENT_HEIGHT = 50, 100

# Константа для повышения скорости противников:
# За каждые COINS_FOR_SPEED_INCREASE собранных монет скорость противников увеличивается
COINS_FOR_SPEED_INCREASE = 5

# Изображения спрайтов

# Изображение игрока – красный прямоугольник
player_img = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
player_img.fill(RED)

# Изображение противника – синий прямоугольник
opponent_img = pygame.Surface((OPPONENT_WIDTH, OPPONENT_HEIGHT))
opponent_img.fill(BLUE)

# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10  # располагается снизу экрана
        self.speed = 7

    def update(self):
        # Управление машиной с помощью стрелок влево/вправо
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed

# Класс противника (машины‑противника)
class Opponent(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = opponent_img
        self.rect = self.image.get_rect()
        # Появление противника в случайной позиции по оси X
        self.rect.x = random.randint(0, WIDTH - OPPONENT_WIDTH)
        self.rect.y = -OPPONENT_HEIGHT  # появляется выше экрана
        
        # Рассчитываем бонус к скорости в зависимости от собранных монет
        bonus = coins_collected // COINS_FOR_SPEED_INCREASE
        # Базовая скорость от 3 до 7 плюс бонус
        self.speed = random.randint(10, 20) + bonus

    def update(self):
        self.rect.y += self.speed  # движение вниз

# Класс монеты
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Определяем случайный вес монеты (значение от 1 до 3)
        self.value = random.randint(1, 3)
        # Размер монеты зависит от её веса (чем больше вес – тем больше монета)
        self.radius = 10 + self.value * 5  # базовый радиус 10, плюс увеличение
        # Создаём поверхность с прозрачным фоном для монеты
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, YELLOW, (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect()
        # Монета появляется в случайном месте по оси X
        self.rect.x = random.randint(0, WIDTH - self.image.get_width())
        self.rect.y = -self.image.get_height()  # появляется выше экрана
        self.speed = 5  # скорость падения монеты

    def update(self):
        self.rect.y += self.speed

# Группы спрайтов
all_sprites = pygame.sprite.Group()
opponents = pygame.sprite.Group()
coins = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

# Переменные для счета
# Счет за успешно избегнутых противников (проезд мимо игрока)
score = 0
# Общее количество собранных монет (с учетом веса монет)
coins_collected = 0

# Таймеры для спавна противников и монет
opponent_timer = 0
opponent_spawn_interval = 27  # примерно каждые 0.42 сек при 60 FPS

coin_timer = 0
coin_spawn_interval = 60  # примерно каждые 1 сек при 60 FPS

# Шрифт для отображения текста
font = pygame.font.SysFont(None, 36)

# Основной игровой цикл
running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Спавн противников: каждую итерацию увеличиваем таймер и создаем нового противника при достижении интервала
    opponent_timer += 1
    if opponent_timer >= opponent_spawn_interval:
        opponent_timer = 0
        opp = Opponent()
        all_sprites.add(opp)
        opponents.add(opp)

    # Спавн монет: аналогично противникам
    coin_timer += 1
    if coin_timer >= coin_spawn_interval:
        coin_timer = 0
        coin = Coin()
        all_sprites.add(coin)
        coins.add(coin)

    # Обновляем все спрайты
    all_sprites.update()

    # Проверка столкновения игрока с противниками
    if pygame.sprite.spritecollide(player, opponents, True):
        # При столкновении игра заканчивается
        running = False

    # Проверка столкновения игрока с монетами
    coins_hit = pygame.sprite.spritecollide(player, coins, True)
    if coins_hit:
        # Для каждой подобранной монеты добавляем её значение к общему счету монет
        for coin in coins_hit:
            coins_collected += coin.value

    # Если противник проехал весь экран (игрок успешно его избежал)
    for opp in opponents:
        if opp.rect.top > HEIGHT:
            score += 1  # увеличиваем счет за избегание
            opp.kill()

    # Отрисовка фона и спрайтов
    screen.fill(GRAY)
    all_sprites.draw(screen)

    # Отрисовка счета (избежанных противников) в левом верхнем углу
    score_text = font.render("Очки: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

    # Отрисовка количества собранных монет (с учетом веса) в правом верхнем углу
    coin_text = font.render("Монеты: " + str(coins_collected), True, WHITE)
    coin_text_rect = coin_text.get_rect(topright=(WIDTH - 10, 10))
    screen.blit(coin_text, coin_text_rect)

    pygame.display.flip()

pygame.quit()
sys.exit()
