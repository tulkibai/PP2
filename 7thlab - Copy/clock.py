import pygame
import time

pygame.init()

WIDTH, HEIGHT = 460, 460
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")
clock_fps = pygame.time.Clock()

clock_face = pygame.image.load("clock_face.png").convert_alpha()
right_hand = pygame.image.load("right_hand.png").convert_alpha() 
left_hand = pygame.image.load("left_hand.png").convert_alpha()

clock_face = pygame.transform.scale(clock_face, (460, 460))
right_hand = pygame.transform.scale(right_hand, (150, 150))
left_hand = pygame.transform.scale(left_hand, (150, 150))

CENTER = (WIDTH // 2, HEIGHT // 2)

def blitRotate(surf, image, pos, originPos, angle):
    image_rect = image.get_rect(topleft=(pos[0] - originPos[0], pos[1] - originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
    rotated_offset = offset_center_to_pivot.rotate(angle)
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)
    rotated_image = pygame.transform.rotate(image, -angle)
    rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)
    surf.blit(rotated_image, rotated_image_rect)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    minute_angle = (minutes / 60) * 360
    second_angle = (seconds / 60) * 360

    screen.fill((255, 255, 255))
    face_rect = clock_face.get_rect(center=CENTER)
    screen.blit(clock_face, face_rect.topleft)

    right_origin = (right_hand.get_width() / 2, right_hand.get_height())
    left_origin = (left_hand.get_width() / 2, left_hand.get_height())

    blitRotate(screen, right_hand, CENTER, right_origin, minute_angle)
    blitRotate(screen, left_hand, CENTER, left_origin, second_angle)

    pygame.display.flip()
    clock_fps.tick(60)

pygame.quit()
