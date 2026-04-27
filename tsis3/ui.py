import pygame

def get_font():
    return pygame.font.SysFont(None, 40)


def draw_text(screen, text, x, y, color=(255,255,255)):
    font = pygame.font.SysFont(None, 40)
    img = font.render(text, True, color)
    screen.blit(img, (x, y))


def main_menu(screen):
    draw_text(screen, "RACER GAME", 300, 100)
    draw_text(screen, "Press ENTER to Play", 280, 200)
    draw_text(screen, "L - Leaderboard", 300, 250)
    draw_text(screen, "S - Settings", 320, 300)


def game_over(screen, score):
    draw_text(screen, "GAME OVER", 320, 150)
    draw_text(screen, f"Score: {score}", 330, 220)
    draw_text(screen, "ENTER - Restart", 300, 300)


def leaderboard_screen(screen, data):
    draw_text(screen, "LEADERBOARD", 300, 50)

    y = 120
    for i, d in enumerate(data):
        draw_text(screen, f"{i+1}. {d['name']} - {d['score']}", 250, y)
        y += 40