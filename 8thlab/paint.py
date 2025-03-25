import pygame
import sys

pygame.init()

# Размеры холста и панели
CANVAS_WIDTH, CANVAS_HEIGHT = 600, 700
UI_WIDTH = 250  # Ширина панели UI
SCREEN_WIDTH = CANVAS_WIDTH + UI_WIDTH
SCREEN_HEIGHT = 700

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Paint")

# Холст
canvas = pygame.Surface((CANVAS_WIDTH, CANVAS_HEIGHT))
canvas.fill((255, 255, 255))

clock = pygame.time.Clock()

# Инструменты
tools = ["pencil", "rect", "circle", "eraser"]
current_tool = "pencil"

# Цвета
colors = [(0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 255)]
color_names = ["Black", "Red", "Green", "Blue", "White"]
current_color = (0, 0, 0)

font = pygame.font.SysFont(None, 24)

# Расположение кнопок инструментов
tool_start_y = 50
tool_height = 40
tool_margin = 10
tool_rects = []
for i, t in enumerate(tools):
    rect = pygame.Rect(
        CANVAS_WIDTH + 20,
        tool_start_y + i * (tool_height + tool_margin),
        160,
        tool_height
    )
    tool_rects.append((t, rect))

# Толщины для карандаша и ластика
pencil_thickness = 3
eraser_thickness = 20

# Расположение блоков изменения толщины
# После инструментов делаем отступ +20
thickness_section_y = tool_start_y + len(tools)*(tool_height + tool_margin) + 20

# Кнопки для изменения толщины карандаша
pencil_minus_rect = pygame.Rect(CANVAS_WIDTH + 20, thickness_section_y, 40, 40)
pencil_plus_rect = pygame.Rect(CANVAS_WIDTH + 70, thickness_section_y, 40, 40)

# Смещаем блок ластика чуть ниже
eraser_section_y = thickness_section_y + 70
eraser_minus_rect = pygame.Rect(CANVAS_WIDTH + 20, eraser_section_y, 40, 40)
eraser_plus_rect = pygame.Rect(CANVAS_WIDTH + 70, eraser_section_y, 40, 40)

# Начало блока выбора цветов ниже ещё на 80 пикселей
color_start_y = eraser_section_y + 80
color_size = 40
color_rects = []
for i, c in enumerate(colors):
    rect = pygame.Rect(
        CANVAS_WIDTH + 20,
        color_start_y + i * (color_size + tool_margin),
        color_size,
        color_size
    )
    color_rects.append((c, rect))

# Точка начала для рисования фигур
start_pos = None

def draw_ui():
    # Заливка панели
    ui_rect = pygame.Rect(CANVAS_WIDTH, 0, UI_WIDTH, SCREEN_HEIGHT)
    pygame.draw.rect(screen, (200, 200, 200), ui_rect)

    # Кнопки инструментов
    for t, rect in tool_rects:
        color_rect = (180, 180, 255) if t == current_tool else (150, 150, 150)
        pygame.draw.rect(screen, color_rect, rect)
        text = font.render(t.capitalize(), True, (0, 0, 0))
        text_rect = text.get_rect(center=rect.center)
        screen.blit(text, text_rect)

    # Толщина карандаша
    pencil_text = font.render(f"Карандаш: {pencil_thickness}", True, (0, 0, 0))
    screen.blit(pencil_text, (CANVAS_WIDTH + 20, thickness_section_y - 25))
    pygame.draw.rect(screen, (180, 180, 180), pencil_minus_rect)
    minus_text = font.render("-", True, (0, 0, 0))
    screen.blit(minus_text, pencil_minus_rect.move(12, 7))
    pygame.draw.rect(screen, (180, 180, 180), pencil_plus_rect)
    plus_text = font.render("+", True, (0, 0, 0))
    screen.blit(plus_text, pencil_plus_rect.move(12, 7))

    # Толщина ластика
    eraser_text = font.render(f"Ластик: {eraser_thickness}", True, (0, 0, 0))
    screen.blit(eraser_text, (CANVAS_WIDTH + 20, eraser_section_y - 25))
    pygame.draw.rect(screen, (180, 180, 180), eraser_minus_rect)
    minus_text2 = font.render("-", True, (0, 0, 0))
    screen.blit(minus_text2, eraser_minus_rect.move(12, 7))
    pygame.draw.rect(screen, (180, 180, 180), eraser_plus_rect)
    plus_text2 = font.render("+", True, (0, 0, 0))
    screen.blit(plus_text2, eraser_plus_rect.move(12, 7))

    # Кнопки цветов
    for c, rect in color_rects:
        pygame.draw.rect(screen, c, rect)
        if c == current_color:
            pygame.draw.rect(screen, (0, 0, 0), rect, 3)

def main():
    global current_tool, current_color, start_pos
    global pencil_thickness, eraser_thickness

    running = True
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mx, my = event.pos
                    # Если нажато в зоне панели
                    if mx > CANVAS_WIDTH:
                        # Проверка кнопок инструментов
                        for t, rect in tool_rects:
                            if rect.collidepoint(mx, my):
                                current_tool = t

                        # Проверка кнопок изменения толщины карандаша
                        if pencil_minus_rect.collidepoint(mx, my):
                            pencil_thickness = max(1, pencil_thickness - 1)
                        elif pencil_plus_rect.collidepoint(mx, my):
                            pencil_thickness += 1

                        # Проверка кнопок изменения толщины ластика
                        if eraser_minus_rect.collidepoint(mx, my):
                            eraser_thickness = max(1, eraser_thickness - 1)
                        elif eraser_plus_rect.collidepoint(mx, my):
                            eraser_thickness += 1

                        # Проверка кнопок выбора цвета
                        for c, rect in color_rects:
                            if rect.collidepoint(mx, my):
                                current_color = c

                    else:
                        # Клик на холсте
                        start_pos = (mx, my)
                        if current_tool == "pencil":
                            pygame.draw.circle(canvas, current_color, (mx, my), pencil_thickness // 2)
                        elif current_tool == "eraser":
                            pygame.draw.circle(canvas, (255, 255, 255), (mx, my), eraser_thickness // 2)

            elif event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:
                mx, my = event.pos
                if mx < CANVAS_WIDTH and my < CANVAS_HEIGHT:
                    if current_tool == "pencil":
                        pygame.draw.line(canvas, current_color, start_pos, (mx, my), pencil_thickness)
                        start_pos = (mx, my)
                    elif current_tool == "eraser":
                        pygame.draw.line(canvas, (255, 255, 255), start_pos, (mx, my), eraser_thickness)
                        start_pos = (mx, my)

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    mx, my = event.pos
                    if mx < CANVAS_WIDTH and my < CANVAS_HEIGHT and start_pos:
                        if current_tool == "rect":
                            x1, y1 = start_pos
                            x2, y2 = mx, my
                            rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))
                            pygame.draw.rect(canvas, current_color, rect, pencil_thickness)
                        elif current_tool == "circle":
                            x1, y1 = start_pos
                            x2, y2 = mx, my
                            radius = int(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 / 2)
                            center = ((x1 + x2) // 2, (y1 + y2) // 2)
                            pygame.draw.circle(canvas, current_color, center, radius, pencil_thickness)
                    start_pos = None

        # Отрисовка фона и холста
        screen.fill((255, 255, 255))
        screen.blit(canvas, (0, 0))

        # Отрисовка интерфейса
        draw_ui()

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
