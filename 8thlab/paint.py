import pygame
import sys
import math

pygame.init()

# Размеры холста и панели UI
CANVAS_WIDTH, CANVAS_HEIGHT = 600, 700
UI_WIDTH = 250  # Ширина панели UI
SCREEN_WIDTH = CANVAS_WIDTH + UI_WIDTH
SCREEN_HEIGHT = CANVAS_HEIGHT

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Paint Pro Ultra Max 2000")

# Отрисовка холста
canvas = pygame.Surface((CANVAS_WIDTH, CANVAS_HEIGHT))
canvas.fill((255, 255, 255))

clock = pygame.time.Clock()

# Список инструментов
tools = [
    "pencil", "rect", "circle", "eraser", 
    "square", "r_triangle", "e_triangle", "rhombus"
]
current_tool = "pencil"

# Цвета
colors = [(0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255)]
color_names = ["Black", "Red", "Green", "Blue"]
current_color = (0, 0, 0)

font = pygame.font.SysFont(None, 24) #

# Расположение кнопок инструментов в 2 столбца
tool_start_y = 50
tool_start_x = CANVAS_WIDTH + 20
tool_height = 40    
tool_width = 110    # ширина каждой кнопки
tool_gap = 10   # зазор между колонками
tool_rects = []
for i, t in enumerate(tools):
    col = i % 2     # 0 или 1
    row = i // 2    # номер ряда
    x = tool_start_x + col * (tool_width + tool_gap)
    y = tool_start_y + row * (tool_height + tool_gap)
    rect = pygame.Rect(x, y, tool_width, tool_height)
    tool_rects.append((t, rect))

# Вычисляем число рядов с инструментами
num_tool_rows = (len(tools) + 1) // 2

# Толщины для карандаша и ластика
pencil_thickness = 3
eraser_thickness = 20

# Блок изменения толщины располагается ниже кнопок инструментов
thickness_section_y = tool_start_y + num_tool_rows * (tool_height + tool_gap) + 20

# Кнопки изменения толщины для карандаша
pencil_minus_rect = pygame.Rect(CANVAS_WIDTH + 20, thickness_section_y, 40, 40)
pencil_plus_rect = pygame.Rect(CANVAS_WIDTH + 70, thickness_section_y, 40, 40)

# Блок для изменения толщины ластика
eraser_section_y = thickness_section_y + 70
eraser_minus_rect = pygame.Rect(CANVAS_WIDTH + 20, eraser_section_y, 40, 40)
eraser_plus_rect = pygame.Rect(CANVAS_WIDTH + 70, eraser_section_y, 40, 40)

# Блок выбора цветов 
color_start_y = eraser_section_y + 80
color_size = 40
color_rects = []
for i, c in enumerate(colors):
    rect = pygame.Rect(
        CANVAS_WIDTH + 20,
        color_start_y + i * (color_size + tool_gap),
        color_size,
        color_size
    )
    color_rects.append((c, rect))

# Точка начала для рисования (запоминается при нажатии мыши)
start_pos = None

def draw_ui():
    # Заливка фона панели
    ui_rect = pygame.Rect(CANVAS_WIDTH, 0, UI_WIDTH, SCREEN_HEIGHT)
    pygame.draw.rect(screen, (200, 200, 200), ui_rect)

    # Отрисовка кнопок инструментов
    for t, rect in tool_rects:
        btn_color = (180, 180, 255) if t == current_tool else (150, 150, 150)
        pygame.draw.rect(screen, btn_color, rect)
        # Замена "_" пробелом для улучшения читаемости
        text = font.render(t.replace("_", " ").capitalize(), True, (0, 0, 0))
        text_rect = text.get_rect(center=rect.center)
        screen.blit(text, text_rect)

    # Отрисовка секции изменения толщины карандаша
    pencil_text = font.render(f"Карандаш: {pencil_thickness}", True, (0, 0, 0))
    screen.blit(pencil_text, (CANVAS_WIDTH + 20, thickness_section_y - 25))
    pygame.draw.rect(screen, (180, 180, 180), pencil_minus_rect)
    screen.blit(font.render("-", True, (0, 0, 0)), pencil_minus_rect.move(12, 7))
    pygame.draw.rect(screen, (180, 180, 180), pencil_plus_rect)
    screen.blit(font.render("+", True, (0, 0, 0)), pencil_plus_rect.move(12, 7))

    # Отрисовка секции изменения толщины ластика
    eraser_text = font.render(f"Ластик: {eraser_thickness}", True, (0, 0, 0))
    screen.blit(eraser_text, (CANVAS_WIDTH + 20, eraser_section_y - 25))
    pygame.draw.rect(screen, (180, 180, 180), eraser_minus_rect)
    screen.blit(font.render("-", True, (0, 0, 0)), eraser_minus_rect.move(12, 7))
    pygame.draw.rect(screen, (180, 180, 180), eraser_plus_rect)
    screen.blit(font.render("+", True, (0, 0, 0)), eraser_plus_rect.move(12, 7))

    # Отрисовка кнопок выбора цветов
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
                    # Если клик в области панели UI
                    if mx > CANVAS_WIDTH:
                        # Выбор инструмента
                        for t, rect in tool_rects:
                            if rect.collidepoint(mx, my):
                                current_tool = t
                        # Изменение толщины карандаша
                        if pencil_minus_rect.collidepoint(mx, my):
                            pencil_thickness = max(1, pencil_thickness - 1)
                        elif pencil_plus_rect.collidepoint(mx, my):
                            pencil_thickness += 1
                        # Изменение толщины ластика
                        if eraser_minus_rect.collidepoint(mx, my):
                            eraser_thickness = max(1, eraser_thickness - 1)
                        elif eraser_plus_rect.collidepoint(mx, my):
                            eraser_thickness += 1
                        # Выбор цвета
                        for c, rect in color_rects:
                            if rect.collidepoint(mx, my):
                                current_color = c
                    else:
                        # Клик на холсте – запоминаем начальную точку
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
                if event.button == 1 and start_pos:
                    mx, my = event.pos
                    if mx < CANVAS_WIDTH and my < CANVAS_HEIGHT:
                        x1, y1 = start_pos
                        x2, y2 = mx, my
                        if current_tool == "rect":
                            rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))
                            pygame.draw.rect(canvas, current_color, rect, pencil_thickness)
                        elif current_tool == "circle":
                            radius = int(math.hypot(x2 - x1, y2 - y1) / 2)
                            center = ((x1 + x2) // 2, (y1 + y2) // 2)
                            pygame.draw.circle(canvas, current_color, center, radius, pencil_thickness)
                        elif current_tool == "square":
                            dx = x2 - x1
                            dy = y2 - y1
                            side = min(abs(dx), abs(dy))
                            new_x2 = x1 + (side if dx >= 0 else -side)
                            new_y2 = y1 + (side if dy >= 0 else -side)
                            rect = pygame.Rect(min(x1, new_x2), min(y1, new_y2), side, side)
                            pygame.draw.rect(canvas, current_color, rect, pencil_thickness)
                        elif current_tool == "right_triangle":
                            points = [(x1, y1), (x2, y1), (x1, y2)]
                            pygame.draw.polygon(canvas, current_color, points, pencil_thickness)
                        elif current_tool == "equilateral_triangle":
                            side = abs(x2 - x1)
                            left_x = min(x1, x2)
                            right_x = max(x1, x2)
                            base_y = y2
                            height = int(side * math.sqrt(3) / 2)
                            apex = ((left_x + right_x) // 2, base_y - height)
                            points = [(left_x, base_y), (right_x, base_y), apex]
                            pygame.draw.polygon(canvas, current_color, points, pencil_thickness)
                        elif current_tool == "rhombus":
                            mid_x = (x1 + x2) // 2
                            mid_y = (y1 + y2) // 2
                            top = (mid_x, y1)
                            right = (x2, mid_y)
                            bottom = (mid_x, y2)
                            left = (x1, mid_y)
                            points = [top, right, bottom, left]
                            pygame.draw.polygon(canvas, current_color, points, pencil_thickness)
                    start_pos = None

        # Отрисовка фона и холста
        screen.fill((255, 255, 255))
        screen.blit(canvas, (0, 0))
        # Отрисовка панели UI
        draw_ui()
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()