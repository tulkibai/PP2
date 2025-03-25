import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 600, 600
# Создание окна
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer with Coins")
clock = pygame.time.Clock()
FPS = 60

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ROAD_COLOR = (50, 50, 50)

# Изображение игрока 
playerImg = pygame.Surface((50, 80))
playerImg.fill((255, 0, 0))

# Изображение монеты
coinImg = pygame.Surface((20, 20))
pygame.draw.circle(coinImg, (255, 255, 0), (10, 10), 10)
coinImg.set_colorkey(BLACK)

# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = playerImg
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 5

    # Обновление позиции игрока
    def update(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed

# Класс монеты
class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = coinImg
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 3

    # Обновление позиции монеты
    def update(self, keys):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.kill()  # Удаляем монету, если она вышла за экран

# Основная функция игры
def main():
    all_sprites = pygame.sprite.Group()  # Группа всех спрайтов
    coin_group = pygame.sprite.Group()     # Группа монет

    player = Player(WIDTH // 2, HEIGHT - 100)  # Создаем игрока
    all_sprites.add(player)

    font = pygame.font.SysFont(None, 36)   # Шрифт для текста
    coin_count = 0  # Счетчик собранных монет
    coin_timer = 0  # Таймер для появления монет
    coin_interval = 60  # Интервал появления монет (в кадрах)

    running = True
    while running:
        clock.tick(FPS)  # Ограничение FPS

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()  # Получаем нажатые клавиши
        coin_timer += 1
        if coin_timer >= coin_interval:
            coin_timer = 0
            coin_x = random.randint(50, WIDTH - 50)  # Случайная позиция по оси X
            coin_y = -20  # Позиция монеты над экраном
            new_coin = Coin(coin_x, coin_y)
            all_sprites.add(new_coin)
            coin_group.add(new_coin)

        # Обновление всех спрайтов с передачей нажатых клавиш
        all_sprites.update(keys)

        # Проверка столкновений игрока с монетами
        collected_coins = pygame.sprite.spritecollide(player, coin_group, True)
        if collected_coins:
            coin_count += len(collected_coins)

        SCREEN.fill(ROAD_COLOR)  # Заливка фона
        all_sprites.draw(SCREEN)  # Отрисовка всех спрайтов

        # Отрисовка текста со счетом монет
        coin_text = font.render(f"Coins: {coin_count}", True, WHITE)
        text_rect = coin_text.get_rect(topright=(WIDTH - 10, 10))
        SCREEN.blit(coin_text, text_rect)

        pygame.display.flip()  # Обновление экрана

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()