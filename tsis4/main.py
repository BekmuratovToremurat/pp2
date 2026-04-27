import pygame
import sys
import json
from game import SnakeGame
from db import *

pygame.init()

screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 40)

# SETTINGS
settings = json.load(open("settings.json"))

# ---------------- TEXT INPUT ----------------
def input_name():
    text = ""
    while True:
        screen.fill((0,0,0))
        t = font.render("Enter name: " + text, True, (255,255,255))
        screen.blit(t, (50, 250))
        pygame.display.update()

        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    return text
                elif e.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += e.unicode

# ---------------- LEADERBOARD ----------------
def show_leaderboard():
    data = leaderboard()
    while True:
        screen.fill((0,0,0))

        y = 50
        for i, row in enumerate(data):
            txt = font.render(f"{i+1}. {row[0]} {row[1]} lvl:{row[2]}", True, (255,255,255))
            screen.blit(txt, (50,y))
            y += 40

        pygame.display.update()

        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                return

# ---------------- MAIN ----------------
name = input_name()
pid = get_player(name)

game = SnakeGame()

running = True
while running:
    screen.fill((0,0,0))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]: game.dx, game.dy = -20,0
    if keys[pygame.K_RIGHT]: game.dx, game.dy = 20,0
    if keys[pygame.K_UP]: game.dx, game.dy = 0,-20
    if keys[pygame.K_DOWN]: game.dx, game.dy = 0,20

    if not game.update():
        save_game(pid, game.score, game.level)
        show_leaderboard()
        break

    game.draw(screen)

    ui = font.render(f"Score {game.score} Level {game.level}", True, (255,255,255))
    screen.blit(ui, (10,10))

    pygame.display.update()
    clock.tick(game.speed)

pygame.quit()