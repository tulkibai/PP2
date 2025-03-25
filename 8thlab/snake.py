import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Размер клетки и сетки
TILE_SIZE = 20
GRID_WIDTH = 30
GRID_HEIGHT = 30

# Создание окна
SCREEN = pygame.display.set_mode((GRID_WIDTH * TILE_SIZE, GRID_HEIGHT * TILE_SIZE))
pygame.display.set_caption("Snake Game")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)

# Шрифт
font = pygame.font.SysFont(None, 36)

# Функция для случайной позиции еды
def get_random_food_position(snake):
    while True:
        x = random.randint(0, GRID_WIDTH - 1)
        y = random.randint(0, GRID_HEIGHT - 1)
        if (x, y) not in snake:
            return (x, y)

def main():
    clock = pygame.time.Clock()

    # Начальные координаты змейки
    snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
    # Начальное направление (dx, dy)
    direction = (1, 0)

    # Начальная еда
    food = get_random_food_position(snake)

    # Счёт и уровень
    score = 0
    level = 1

    running = True
    while running:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # Управление змейкой
                if event.key == pygame.K_UP and direction != (0, 1):
                    direction = (0, -1)
                elif event.key == pygame.K_DOWN and direction != (0, -1):
                    direction = (0, 1)
                elif event.key == pygame.K_LEFT and direction != (1, 0):
                    direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                    direction = (1, 0)

        # Движение змейки
        head_x, head_y = snake[0]
        dx, dy = direction
        new_head = (head_x + dx, head_y + dy)

        # Проверка столкновения со стеной
        if (new_head[0] < 0 or new_head[0] >= GRID_WIDTH or
            new_head[1] < 0 or new_head[1] >= GRID_HEIGHT):
            running = False
            break

        # Проверка столкновения с собой
        if new_head in snake:
            running = False
            break

        # Добавляем новую голову
        snake.insert(0, new_head)

        # Если съели еду
        if new_head == food:
            score += 1
            food = get_random_food_position(snake)
        else:
            snake.pop()

        # Определение уровня (каждые 4 очка)
        level = score // 4 + 1

        # Отрисовка фона
        SCREEN.fill(BLACK)

        # Отрисовка змейки
        for (x, y) in snake:
            rect = (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(SCREEN, GREEN, rect)

        # Отрисовка еды
        food_rect = (food[0] * TILE_SIZE, food[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        pygame.draw.rect(SCREEN, RED, food_rect)

        # Отрисовка счета и уровня
        text = font.render(f"Счёт: {score}  Уровень: {level}", True, WHITE)
        SCREEN.blit(text, (10, 10))

        # Обновляем экран
        pygame.display.flip()

        # Увеличиваем скорость с ростом уровня
        # Например, базовая скорость 10, плюс 2 за каждый уровень сверх первого
        clock.tick(10 + (level - 1) * 2)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()