import pygame
import random
import sys

pygame.init()

# Размеры экрана
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer с противниками и монетами")

clock = pygame.time.Clock()
FPS = 60

# Цвета
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Размеры машин
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 100
OPPONENT_WIDTH, OPPONENT_HEIGHT = 50, 100

# Создание изображения игрока (красный прямоугольник)
player_img = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
player_img.fill(RED)

# Создание изображения противника (синий прямоугольник)
opponent_img = pygame.Surface((OPPONENT_WIDTH, OPPONENT_HEIGHT))
opponent_img.fill(BLUE)

# Создание изображения монеты (жёлтый круг)
coin_radius = 15
coin_img = pygame.Surface((coin_radius * 2, coin_radius * 2), pygame.SRCALPHA)
pygame.draw.circle(coin_img, YELLOW, (coin_radius, coin_radius), coin_radius)

# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10  # располагается внизу экрана
        self.speed = 5

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
        self.rect.x = random.randint(0, WIDTH - OPPONENT_WIDTH)
        self.rect.y = -OPPONENT_HEIGHT  # появляется выше экрана
        self.speed = random.randint(3, 7)  # случайная скорость движения

    def update(self):
        self.rect.y += self.speed  # движение вниз

# Класс монеты
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - coin_img.get_width())
        self.rect.y = -coin_img.get_height()  # появляется выше экрана
        self.speed = 5  # скорость падения монеты

    def update(self):
        self.rect.y += self.speed

# Группы спрайтов
all_sprites = pygame.sprite.Group()
opponents = pygame.sprite.Group()
coins = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

# Счёт: количество успешно избегнутых противников
score = 0
# Количество собранных монет
coins_collected = 0

# Таймеры для появления противников и монет
opponent_timer = 0
opponent_spawn_interval = 90  # каждые ~1.5 секунды при 60 FPS

coin_timer = 0
coin_spawn_interval = 120  # каждые ~2 секунды при 60 FPS

# Шрифт для отрисовки текста
font = pygame.font.SysFont(None, 36)

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Спавн противников
    opponent_timer += 1
    if opponent_timer >= opponent_spawn_interval:
        opponent_timer = 0
        opp = Opponent()
        all_sprites.add(opp)
        opponents.add(opp)

    # Спавн монет
    coin_timer += 1
    if coin_timer >= coin_spawn_interval:
        coin_timer = 0
        coin = Coin()
        all_sprites.add(coin)
        coins.add(coin)

    # Обновление всех спрайтов
    all_sprites.update()

    # Проверка столкновения игрока с противниками
    if pygame.sprite.spritecollide(player, opponents, True):
        # При столкновении игра заканчивается
        running = False

    # Проверка столкновения игрока с монетами
    coins_hit = pygame.sprite.spritecollide(player, coins, True)
    if coins_hit:
        coins_collected += len(coins_hit)

    # Если противник проехал весь экран (игрок успешно его избежал)
    for opp in opponents:
        if opp.rect.top > HEIGHT:
            score += 1  # увеличиваем счёт на 1
            opp.kill()  # удаляем противника

    # Отрисовка фона (дорога)
    screen.fill(GRAY)
    all_sprites.draw(screen)

    # Отрисовка счета (избежанных противников) в левом верхнем углу
    score_text = font.render("Очки: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

    # Отрисовка количества собранных монет в правом верхнем углу
    coin_text = font.render("Монеты: " + str(coins_collected), True, WHITE)
    coin_text_rect = coin_text.get_rect(topright=(WIDTH - 10, 10))
    screen.blit(coin_text, coin_text_rect)

    pygame.display.flip()

pygame.quit()
sys.exit()
