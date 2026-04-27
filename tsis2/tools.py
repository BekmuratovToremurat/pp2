import pygame
from collections import deque
import math

# ---------------- FLOOD FILL ----------------
def flood_fill(surface, start_pos, new_color):
    width, height = surface.get_size()
    target_color = surface.get_at(start_pos)

    if target_color == new_color:
        return

    queue = deque([start_pos])

    while queue:
        x, y = queue.popleft()

        if x < 0 or x >= width or y < 0 or y >= height:
            continue

        if surface.get_at((x, y)) != target_color:
            continue

        surface.set_at((x, y), new_color)

        queue.append((x+1, y))
        queue.append((x-1, y))
        queue.append((x, y+1))
        queue.append((x, y-1))


# ---------------- BASIC ----------------
def draw_line(surface, color, start, end, size):
    pygame.draw.line(surface, color, start, end, size)


def draw_rect(surface, color, start, end, size):
    rect = pygame.Rect(start, (end[0]-start[0], end[1]-start[1]))
    pygame.draw.rect(surface, color, rect, size)


def draw_square(surface, color, start, end, size):
    side = min(abs(end[0]-start[0]), abs(end[1]-start[1]))
    rect = pygame.Rect(start, (side, side))
    pygame.draw.rect(surface, color, rect, size)


def draw_circle(surface, color, start, end, size):
    radius = int(math.hypot(end[0]-start[0], end[1]-start[1]))
    pygame.draw.circle(surface, color, start, radius, size)


# ---------------- TRIANGLE ----------------
def draw_triangle(surface, color, start, end, size):
    x1, y1 = start
    x2, y2 = end

    base = abs(x2 - x1)
    height = int(base * math.sqrt(3) / 2)

    points = [
        (x1, y1),
        (x2, y1),
        ((x1 + x2) // 2, y1 - height)
    ]

    pygame.draw.polygon(surface, color, points, size)


# ---------------- RHOMBUS ----------------
def draw_rhombus(surface, color, start, end, size):
    x1, y1 = start
    x2, y2 = end

    cx = (x1 + x2) // 2
    cy = (y1 + y2) // 2

    points = [
        (cx, y1),
        (x2, cy),
        (cx, y2),
        (x1, cy)
    ]

    pygame.draw.polygon(surface, color, points, size)