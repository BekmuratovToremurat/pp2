import pygame
import sys

from racer import Game
from ui import main_menu, game_over, leaderboard_screen
from persistence import (
    load_settings,
    load_leaderboard,
    add_score,
    save_settings
)

pygame.init()
pygame.mixer.init()

# ---------------- SCREEN ----------------
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TSIS 3 Racer")

clock = pygame.time.Clock()

# ---------------- DATA ----------------
settings = load_settings()
leaderboard = load_leaderboard()

# ---------------- SOUND ----------------
music_loaded = False

def start_music():
    global music_loaded
    if settings["sound"] and not music_loaded:
        pygame.mixer.music.load("assets/music.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        music_loaded = True

def stop_music():
    pygame.mixer.music.stop()

start_music()

crash_sound = pygame.mixer.Sound("assets/crash.mp3")
powerup_sound = pygame.mixer.Sound("assets/powerup.mp3")

# ---------------- STATE ----------------
state = "menu"
game = Game()
player_name = "Player"

# ---------------- LOOP ----------------
while True:
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # ---------------- MENU ----------------
        if state == "menu":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game = Game()
                    game.sound_enabled = settings["sound"]
                    state = "game"

                elif event.key == pygame.K_l:
                    leaderboard = load_leaderboard()
                    state = "leaderboard"

                elif event.key == pygame.K_s:
                    state = "settings"

        # ---------------- GAME OVER ----------------
        elif state == "game_over":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game = Game()
                    game.sound_enabled = settings["sound"]
                    state = "game"

                elif event.key == pygame.K_m:
                    state = "menu"

        # ---------------- LEADERBOARD ----------------
        elif state == "leaderboard":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    state = "menu"

        # ---------------- SETTINGS ----------------
        elif state == "settings":
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_s:
                    settings["sound"] = not settings["sound"]

                    if settings["sound"]:
                        start_music()
                    else:
                        stop_music()

                elif event.key == pygame.K_c:
                    settings["car_color"] = "blue" if settings["car_color"] == "red" else "red"

                elif event.key == pygame.K_d:
                    settings["difficulty"] = "hard" if settings["difficulty"] == "normal" else "normal"

                elif event.key == pygame.K_ESCAPE:
                    save_settings(settings)
                    state = "menu"

    # ---------------- GAME ----------------
    if state == "game":
        alive = game.update()
        game.draw(screen)

        # SOUND EVENTS
        if hasattr(game, "crash_event") and game.crash_event:
            crash_sound.play()
            game.crash_event = False

        if hasattr(game, "powerup_event") and game.powerup_event:
            powerup_sound.play()
            game.powerup_event = False

        if not alive:
            add_score(player_name, game.score, game.distance)
            leaderboard = load_leaderboard()
            state = "game_over"

    # ---------------- MENU ----------------
    elif state == "menu":
        main_menu(screen)

    # ---------------- GAME OVER ----------------
    elif state == "game_over":
        game_over(screen, game.score)

    # ---------------- LEADERBOARD ----------------
    elif state == "leaderboard":
        leaderboard_screen(screen, leaderboard)

    # ---------------- SETTINGS ----------------
    elif state == "settings":
        font = pygame.font.SysFont(None, 40)

        txt1 = font.render(f"Sound: {settings['sound']} (S)", True, (255,255,255))
        txt2 = font.render(f"Car color: {settings['car_color']} (C)", True, (255,255,255))
        txt3 = font.render(f"Difficulty: {settings['difficulty']} (D)", True, (255,255,255))
        txt4 = font.render("ESC - Save & Back", True, (255,255,255))

        screen.blit(txt1, (200, 150))
        screen.blit(txt2, (200, 200))
        screen.blit(txt3, (200, 250))
        screen.blit(txt4, (200, 350))

    pygame.display.flip()
    clock.tick(60)