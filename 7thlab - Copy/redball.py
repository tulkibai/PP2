import pygame
pygame.init()

screen_width = 810
screen_height = 610
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Red Ball Movement")

red = (255, 0, 0)
white = (255, 255, 255)

ball_radius = 25
ball_x = 25
ball_y = 25

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    new_x = ball_x
    new_y = ball_y

    if keys[pygame.K_UP]:
        new_y -= 20
    if keys[pygame.K_DOWN]:
        new_y += 20
    if keys[pygame.K_LEFT]:
        new_x -= 20
    if keys[pygame.K_RIGHT]:
        new_x += 20

    # Проверка границ для горизонтали и вертикали
    if new_x >= ball_radius and new_x <= screen_width - ball_radius:
        ball_x = new_x
    if new_y >= ball_radius and new_y <= screen_height - ball_radius:
        ball_y = new_y

    screen.fill(white)
    pygame.draw.circle(screen, red, (ball_x, ball_y), ball_radius)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
