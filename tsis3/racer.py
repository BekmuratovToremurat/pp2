import pygame
import random

WIDTH, HEIGHT = 800, 600


# ---------------- PLAYER ----------------
class Player:
    def __init__(self):
        self.x = 380
        self.y = 500
        self.speed = 5
        self.width = 40
        self.height = 70

        # POWER UPS
        self.nitro = 0
        self.shield = False
        self.repair = 0

    def move(self, keys):
        speed = self.speed + (5 if self.nitro > 0 else 0)

        if keys[pygame.K_LEFT]:
            self.x -= speed
        if keys[pygame.K_RIGHT]:
            self.x += speed

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0),
                         (self.x, self.y, self.width, self.height))


# ---------------- OBSTACLE ----------------
class Obstacle:
    def __init__(self):
        self.x = random.choice([200, 350, 500])
        self.y = -50
        self.speed = random.randint(4, 8)

    def update(self):
        self.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, 40, 70))


# ---------------- POWER UPS ----------------
class PowerUp:
    def __init__(self):
        self.x = random.choice([200, 350, 500])
        self.y = -50
        self.type = random.choice(["nitro", "shield", "repair"])

    def update(self):
        self.y += 5

    def draw(self, screen):
        color = {
            "nitro": (0, 255, 255),
            "shield": (0, 255, 0),
            "repair": (255, 255, 0)
        }[self.type]

        pygame.draw.circle(screen, color, (self.x, self.y), 15)


# ---------------- GAME ----------------
class Game:
    def __init__(self):
        self.player = Player()
        self.obstacles = []
        self.powerups = []

        self.score = 0
        self.distance = 0

        # ================= REQUIRED ADDITION =================
        self.crash_event = False
        self.powerup_event = False
        self.sound_enabled = True

    def update(self):
        keys = pygame.key.get_pressed()
        self.player.move(keys)

        self.distance += 1
        self.score += 1

        # reset events each frame
        self.crash_event = False
        self.powerup_event = False

        # obstacles spawn
        if random.randint(1, 35) == 1:
            self.obstacles.append(Obstacle())

        # powerups spawn
        if random.randint(1, 120) == 1:
            self.powerups.append(PowerUp())

        # nitro timer
        if self.player.nitro > 0:
            self.player.nitro -= 1

        # ---------------- OBSTACLES ----------------
        for o in self.obstacles[:]:
            o.update()

            if self.collision(o):

                # shield
                if self.player.shield:
                    self.player.shield = False
                    self.obstacles.remove(o)
                    continue

                # repair
                if self.player.repair > 0:
                    self.player.repair -= 1
                    self.obstacles.remove(o)
                    continue

                # 💥 CRASH EVENT
                self.crash_event = True

                return False

        # ---------------- POWERUPS ----------------
        for p in self.powerups[:]:
            p.update()

            if self.pickup(p):

                # ⚡ POWERUP EVENT
                self.powerup_event = True

                if p.type == "nitro":
                    self.player.nitro = 180
                elif p.type == "shield":
                    self.player.shield = True
                elif p.type == "repair":
                    self.player.repair += 1

                self.powerups.remove(p)

        # cleanup
        self.obstacles = [o for o in self.obstacles if o.y < HEIGHT]
        self.powerups = [p for p in self.powerups if p.y < HEIGHT]

        return True

    # ---------------- COLLISION ----------------
    def collision(self, o):
        return (
            self.player.x < o.x + 40 and
            self.player.x + 40 > o.x and
            self.player.y < o.y + 70 and
            self.player.y + 70 > o.y
        )

    # ---------------- PICKUP ----------------
    def pickup(self, p):
        return (
            abs(self.player.x - p.x) < 30 and
            abs(self.player.y - p.y) < 30
        )

    # ---------------- DRAW ----------------
    def draw(self, screen):
        self.player.draw(screen)

        for o in self.obstacles:
            o.draw(screen)

        for p in self.powerups:
            p.draw(screen)

        font = pygame.font.SysFont(None, 25)

        if self.player.nitro > 0:
            screen.blit(font.render("NITRO", True, (0, 255, 255)), (10, 10))

        if self.player.shield:
            screen.blit(font.render("SHIELD", True, (0, 255, 0)), (10, 30))

        if self.player.repair > 0:
            screen.blit(font.render(f"REPAIR x{self.player.repair}", True, (255, 255, 0)), (10, 50))