import pygame
import random
import sys

pygame.init()

# Размер клетки и сетки
TILE_SIZE = 20
GRID_WIDTH = 30
GRID_HEIGHT = 30

# Создание окна игры
SCREEN = pygame.display.set_mode((GRID_WIDTH * TILE_SIZE, GRID_HEIGHT * TILE_SIZE))
pygame.display.set_caption("Snake Game")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)

# Шрифт для отображения текста
font = pygame.font.SysFont(None, 36)

# Функция для получения случайной позиции еды (не на теле змейки)
def get_random_food_position(snake):
    while True:
        x = random.randint(0, GRID_WIDTH - 1)
        y = random.randint(0, GRID_HEIGHT - 1)
        if (x, y) not in snake:
            return (x, y)

# Функция для создания еды с случайной позицией, весом и временем появления
def create_food(snake):
    pos = get_random_food_position(snake)
    weight = random.randint(1, 3)  # вес еды от 1 до 3
    spawn_time = pygame.time.get_ticks()  # время создания еды (в мс)
    return {"position": pos, "weight": weight, "spawn_time": spawn_time}

def main():
    clock = pygame.time.Clock()

    # Изначальное положение змейки (список координат)
    snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
    # Переменная для прироста: сколько сегментов надо добавить (увеличивается на вес еды)
    growth = 0
    # Начальное направление движения (dx, dy)
    direction = (1, 0)

    score = 0  # счет очков
    food_lifetime = 5000  # время жизни еды в мс (5 секунд)

    # Создаем первую еду
    food = create_food(snake)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # Управление змейкой (без разворота на 180 градусов)
                if event.key == pygame.K_UP and direction != (0, 1):
                    direction = (0, -1)
                elif event.key == pygame.K_DOWN and direction != (0, -1):
                    direction = (0, 1)
                elif event.key == pygame.K_LEFT and direction != (1, 0):
                    direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                    direction = (1, 0)

        # Вычисляем новую позицию головы змейки
        head_x, head_y = snake[0]
        dx, dy = direction
        new_head = (head_x + dx, head_y + dy)

        # Проверка столкновения со стенами
        if (new_head[0] < 0 or new_head[0] >= GRID_WIDTH or
            new_head[1] < 0 or new_head[1] >= GRID_HEIGHT):
            running = False
            break

        # Проверка столкновения с самим собой
        if new_head in snake:
            running = False
            break

        # Добавляем новую голову змейки
        snake.insert(0, new_head)

        # Если змейка съела еду
        if new_head == food["position"]:
            score += food["weight"]  # счет увеличивается на вес еды
            growth += food["weight"]  # увеличение длины змейки равно весу еды
            food = create_food(snake)  # создаем новую еду
        else:
            # Если есть прирост (growth > 0), не удаляем хвост, чтобы змейка росла
            if growth > 0:
                growth -= 1
            else:
                snake.pop()

        # Если время жизни еды истекло, создаем новую еду
        current_time = pygame.time.get_ticks()
        if current_time - food["spawn_time"] > food_lifetime:
            food = create_food(snake)

        # Определяем уровень (например, каждые 4 очка)
        level = score // 4 + 1

        # Отрисовка фона
        SCREEN.fill(BLACK)

        # Отрисовка змейки
        for (x, y) in snake:
            rect = (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(SCREEN, GREEN, rect)

        # Отрисовка еды
        food_rect = (food["position"][0] * TILE_SIZE, food["position"][1] * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        pygame.draw.rect(SCREEN, RED, food_rect)
        # Отображаем вес еды поверх неё
        weight_text = font.render(str(food["weight"]), True, WHITE)
        text_rect = weight_text.get_rect(center=(food["position"][0] * TILE_SIZE + TILE_SIZE / 2,
                                                  food["position"][1] * TILE_SIZE + TILE_SIZE / 2))
        SCREEN.blit(weight_text, text_rect)

        # Отрисовка счета и уровня
        text = font.render(f"Счёт: {score}  Уровень: {level}", True, WHITE)
        SCREEN.blit(text, (10, 10))

        pygame.display.flip()

        # Регулируем скорость игры (увеличивается с уровнем)
        clock.tick(10 + (level - 1) * 2)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
