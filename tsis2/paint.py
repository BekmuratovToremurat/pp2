import pygame
import sys
from datetime import datetime
from tools import *

pygame.init()

WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TSIS 2 Paint")

canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill((255, 255, 255))

clock = pygame.time.Clock()

# ---------------- SETTINGS ----------------
color = (0, 0, 0)
brush_size = 2

tool = "pencil"
drawing = False

start_pos = None
last_pos = None

eraser = False

# ---------------- TEXT ----------------
font = pygame.font.SysFont(None, 30)
text_mode = False
text = ""
text_pos = (0, 0)

# ---------------- LOOP ----------------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # ---------------- KEYBOARD ----------------
        if event.type == pygame.KEYDOWN:

            # brush size
            if event.key == pygame.K_1:
                brush_size = 2
            if event.key == pygame.K_2:
                brush_size = 5
            if event.key == pygame.K_3:
                brush_size = 10

            # tools
            if event.key == pygame.K_p:
                tool = "pencil"
            if event.key == pygame.K_l:
                tool = "line"
            if event.key == pygame.K_r:
                tool = "rect"
            if event.key == pygame.K_q:
                tool = "square"
            if event.key == pygame.K_c:
                tool = "circle"
            if event.key == pygame.K_t:
                tool = "triangle"
            if event.key == pygame.K_h:
                tool = "rhombus"
            if event.key == pygame.K_e:
                tool = "eraser"
            if event.key == pygame.K_f:
                tool = "fill"
            if event.key == pygame.K_x:
                tool = "text"

            # save
            if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                filename = f"paint_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                pygame.image.save(canvas, filename)
                print("Saved:", filename)

            # TEXT INPUT
            if tool == "text":
                if text_mode:
                    if event.key == pygame.K_RETURN:
                        rendered = font.render(text, True, color)
                        canvas.blit(rendered, text_pos)
                        text = ""
                        text_mode = False

                    elif event.key == pygame.K_ESCAPE:
                        text = ""
                        text_mode = False

                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]

                    else:
                        text += event.unicode

        # ---------------- MOUSE DOWN ----------------
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos
            last_pos = event.pos

            if tool == "fill":
                flood_fill(canvas, event.pos, color)

            if tool == "text":
                text_mode = True
                text_pos = event.pos
                text = ""

        # ---------------- MOUSE UP ----------------
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False

            if tool == "line":
                draw_line(canvas, color, start_pos, event.pos, brush_size)

            elif tool == "rect":
                draw_rect(canvas, color, start_pos, event.pos, brush_size)

            elif tool == "square":
                draw_square(canvas, color, start_pos, event.pos, brush_size)

            elif tool == "circle":
                draw_circle(canvas, color, start_pos, event.pos, brush_size)

            elif tool == "triangle":
                draw_triangle(canvas, color, start_pos, event.pos, brush_size)

            elif tool == "rhombus":
                draw_rhombus(canvas, color, start_pos, event.pos, brush_size)

        # ---------------- DRAW ----------------
        if event.type == pygame.MOUSEMOTION and drawing:

            if tool == "pencil":
                pygame.draw.line(canvas, color, last_pos, event.pos, brush_size)
                last_pos = event.pos

            elif tool == "eraser":
                pygame.draw.line(canvas, (255, 255, 255), last_pos, event.pos, brush_size * 2)
                last_pos = event.pos

    # ---------------- RENDER ----------------
    screen.fill((200, 200, 200))
    screen.blit(canvas, (0, 0))

    mouse = pygame.mouse.get_pos()

    # previews
    if drawing:
        if tool == "line":
            pygame.draw.line(screen, color, start_pos, mouse, brush_size)

        elif tool == "rect":
            pygame.draw.rect(screen, color, pygame.Rect(start_pos, (mouse[0]-start_pos[0], mouse[1]-start_pos[1])), brush_size)

        elif tool == "circle":
            radius = int(((mouse[0]-start_pos[0])**2 + (mouse[1]-start_pos[1])**2) ** 0.5)
            pygame.draw.circle(screen, color, start_pos, radius, brush_size)

    # text preview
    if text_mode:
        preview = font.render(text, True, color)
        screen.blit(preview, text_pos)

    pygame.display.flip()
    clock.tick(60)

#P - pencil
#L - line
#R - rectangle
#Q - square
#C - circle
#T - triangle (equilateral)
#H - rhombus
#E - eraser
#F - fill
#X - text

#1 = small
#2 = medium
#3 = large