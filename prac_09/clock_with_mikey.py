import pygame
from datetime import datetime

pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption('My clock')

center = (400, 400)
clock = pygame.time.Clock()

clockk = pygame.image.load('images\clock.png')
min = pygame.image.load('images\min_hand.png')
sec = pygame.image.load('images\sec_hand.png')

def rotate_image(image, angle, pivot):
    # Вращаем стрелки вокруг центра
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=pivot)
    return rotated_image, new_rect

def draw_hands():
    now = datetime.now()

    sec_angle = -now.second * 6  
    min_angle = -(now.minute + 10) * 6  

    # Вращаем стрелки
    rotated_minute, minute_rect = rotate_image(min, min_angle, center)
    rotated_second, second_rect = rotate_image(sec, sec_angle, center)

    # Отображаем стрелки
    screen.blit(rotated_minute, minute_rect.topleft)
    screen.blit(rotated_second, second_rect.topleft)

running = True
while running:
    screen.fill((255,255,255))
    screen.blit(clockk, (0,100))

    draw_hands()  

    pygame.display.flip()
    clock.tick(1)  

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()