import pygame
import random
import sys
import psycopg2
from psycopg2 import sql

pygame.init()

# -----------------------------------------------------------------------------------
# 1. ПАРАМЕТРЫ ИГРЫ
# -----------------------------------------------------------------------------------

TILE_SIZE = 20
GRID_WIDTH = 30
GRID_HEIGHT = 30

SCREEN = pygame.display.set_mode((GRID_WIDTH * TILE_SIZE, GRID_HEIGHT * TILE_SIZE))
pygame.display.set_caption("Snake Game with PostgreSQL (Self-contained)")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)

font = pygame.font.SysFont(None, 36)

# -----------------------------------------------------------------------------------
# 2. ФУНКЦИЯ ДЛЯ УБЕЖДЕНИЯ, ЧТО БАЗА СУЩЕСТВУЕТ
# -----------------------------------------------------------------------------------
def ensure_database(dbname, user, password, host, port):
    """
    Подключается к служебной базе 'postgres', проверяет,
    существует ли БД dbname, и если нет – создаёт её.
    """
    conn = psycopg2.connect(
        dbname="postgres",  # служебная БД PostgreSQL
        user=user,
        password=password,
        host=host,
        port=port
    )
    conn.autocommit = True
    cursor = conn.cursor()
    
    # Проверяем, есть ли уже такая база
    cursor.execute("SELECT 1 FROM pg_database WHERE datname = %s", (dbname,))
    exists = cursor.fetchone()
    
    if not exists:
        # Создаём базу, если её нет
        cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(dbname)))
        print(f"База данных '{dbname}' успешно создана.")
    else:
        print(f"База данных '{dbname}' уже существует.")
    
    cursor.close()
    conn.close()

# -----------------------------------------------------------------------------------
# 3. ПАРАМЕТРЫ ДЛЯ ПОДКЛЮЧЕНИЯ К БД
# -----------------------------------------------------------------------------------
DB_NAME = "snake_db"
DB_USER = "postgres"   # Ваш пользователь, имеющий CREATE DATABASE
DB_PASSWORD = "123"  # Ваш пароль
DB_HOST = "localhost"
DB_PORT = "5432"

# -----------------------------------------------------------------------------------
# 4. ФУНКЦИЯ ПОДКЛЮЧЕНИЯ К SNAKE_DB
# -----------------------------------------------------------------------------------
def db_connect():
    """
    Подключаемся к БД snake_db (она уже должна существовать после ensure_database).
    Возвращаем (conn, cursor).
    """
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    cursor = conn.cursor()
    return conn, cursor

# -----------------------------------------------------------------------------------
# 5. АВТОМАТИЧЕСКИ СОЗДАЕМ ТАБЛИЦУ HIGHSCORES (ЕСЛИ ЕЩЁ НЕТ)
# -----------------------------------------------------------------------------------
def ensure_table():
    conn, cursor = db_connect()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS highscores (
            id SERIAL PRIMARY KEY,
            score INT NOT NULL,
            level INT NOT NULL,
            play_time TIMESTAMP NOT NULL DEFAULT NOW()
        );
    """)
    conn.commit()
    cursor.close()
    conn.close()
    print("Таблица 'highscores' проверена/создана.")

# -----------------------------------------------------------------------------------
# 6. ФУНКЦИИ ДЛЯ РАБОТЫ С ТАБЛИЦЕЙ HIGHSCORES
# -----------------------------------------------------------------------------------
def get_best_score():
    """Получаем максимальный score из таблицы highscores."""
    try:
        conn, cursor = db_connect()
        cursor.execute("SELECT MAX(score) FROM highscores;")
        result = cursor.fetchone()
        cursor.close()
        conn.close()

        if result and result[0] is not None:
            return result[0]
        return 0
    except Exception as e:
        print("Ошибка при получении лучшего счёта:", e)
        return 0

def save_score(score, level):
    """Сохраняем (score, level) в таблицу highscores."""
    try:
        conn, cursor = db_connect()
        cursor.execute("INSERT INTO highscores (score, level) VALUES (%s, %s);", (score, level))
        conn.commit()
        cursor.close()
        conn.close()
        print(f"Счёт {score} (уровень {level}) сохранён в БД.")
    except Exception as e:
        print("Ошибка при сохранении счёта:", e)

# -----------------------------------------------------------------------------------
# 7. ФУНКЦИИ ДЛЯ ИГРОВОЙ ЛОГИКИ
# -----------------------------------------------------------------------------------
def get_random_food_position(snake):
    """Находим случайную позицию еды, не совпадающую с телом змейки."""
    while True:
        x = random.randint(0, GRID_WIDTH - 1)
        y = random.randint(0, GRID_HEIGHT - 1)
        if (x, y) not in snake:
            return (x, y)

def create_food(snake):
    """Создаём объект 'еда' со случайной позицией, весом и временем появления."""
    pos = get_random_food_position(snake)
    weight = random.randint(1, 3)      # вес еды от 1 до 3
    spawn_time = pygame.time.get_ticks()  # время создания еды (миллисекунды)
    return {"position": pos, "weight": weight, "spawn_time": spawn_time}

# -----------------------------------------------------------------------------------
# 8. ОСНОВНОЙ ЦИКЛ ИГРЫ
# -----------------------------------------------------------------------------------
def main():
    # 8.1. Сначала убеждаемся, что у нас есть база snake_db
    ensure_database(DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT)
    # 8.2. Затем убеждаемся, что есть таблица highscores
    ensure_table()

    clock = pygame.time.Clock()

    # Получаем лучший счёт, чтобы показать при старте
    best_score = get_best_score()
    print(f"Лучший счёт в БД: {best_score}")

    # Начальные настройки змейки
    snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
    growth = 0
    direction = (1, 0)
    score = 0
    food_lifetime = 5000  # 5 секунд

    # Создаём еду
    food = create_food(snake)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # Стрелки: меняем направление, не допускаем разворот на 180
                if event.key == pygame.K_UP and direction != (0, 1):
                    direction = (0, -1)
                elif event.key == pygame.K_DOWN and direction != (0, -1):
                    direction = (0, 1)
                elif event.key == pygame.K_LEFT and direction != (1, 0):
                    direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                    direction = (1, 0)

        # Новая позиция головы
        head_x, head_y = snake[0]
        dx, dy = direction
        new_head = (head_x + dx, head_y + dy)

        # Проверка столкновения со стенами
        if new_head[0] < 0 or new_head[0] >= GRID_WIDTH or new_head[1] < 0 or new_head[1] >= GRID_HEIGHT:
            running = False
            break

        # Проверка столкновения с собой
        if new_head in snake:
            running = False
            break

        snake.insert(0, new_head)

        # Проверяем, съела ли змейка еду
        if new_head == food["position"]:
            score += food["weight"]
            growth += food["weight"]
            food = create_food(snake)  # Создаём новую еду
        else:
            # Если нужно расти, уменьшаем growth, не удаляя хвост
            if growth > 0:
                growth -= 1
            else:
                snake.pop()

        # Если время еды истекло, создаём новую
        current_time = pygame.time.get_ticks()
        if current_time - food["spawn_time"] > food_lifetime:
            food = create_food(snake)

        # Уровень растёт каждые 4 очка
        level = score // 4 + 1

        # -----------------------------------------------------------------------------
        # ОТРИСОВКА
        # -----------------------------------------------------------------------------
        SCREEN.fill(BLACK)

        # Змейка
        for (x, y) in snake:
            rect = (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(SCREEN, GREEN, rect)

        # Еда
        food_rect = (
            food["position"][0] * TILE_SIZE,
            food["position"][1] * TILE_SIZE,
            TILE_SIZE,
            TILE_SIZE
        )
        pygame.draw.rect(SCREEN, RED, food_rect)

        # Рисуем текст веса еды на ней
        weight_text = font.render(str(food["weight"]), True, WHITE)
        text_rect = weight_text.get_rect(center=(
            food["position"][0] * TILE_SIZE + TILE_SIZE / 2,
            food["position"][1] * TILE_SIZE + TILE_SIZE / 2
        ))
        SCREEN.blit(weight_text, text_rect)

        # Отображаем счёт и уровень
        score_text = font.render(f"Счёт: {score}  Уровень: {level}", True, WHITE)
        SCREEN.blit(score_text, (10, 10))

        # Отображаем лучший счёт (из БД)
        best_text = font.render(f"Лучший счёт (из БД): {best_score}", True, WHITE)
        SCREEN.blit(best_text, (10, 50))

        pygame.display.flip()

        # Скорость игры (увеличиваем при повышении уровня)
        clock.tick(10 + (level - 1) * 2)

    # -----------------------------------------------------------------------------
    # Завершаем игру
    # -----------------------------------------------------------------------------
    pygame.quit()

    # Сохраняем счёт в БД (если больше 0)
    if score > 0:
        save_score(score, level)

    sys.exit()


# -----------------------------------------------------------------------------------
# 9. СТАРТ ИГРЫ
# -----------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
