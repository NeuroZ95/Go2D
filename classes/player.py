import pygame
from classes.gameobject import GameObject
from settings import S_punch1

class Player(GameObject):
    def __init__(self, X, Y):
        super().__init__(X, Y)
        self.vx = 0
        self.vy = 0
        self.gravity = 0
        self.onland = False

    def Update(self, screen, color, radius, speed):
        keys = pygame.key.get_pressed()

        sw, sh = screen.get_size()

        # Горизонтальное движение
        if keys[pygame.K_d] and self.onland:
            self.vx = speed
        elif keys[pygame.K_a] and self.onland:
            self.vx = -speed
        elif self.onland:
            self.vx = 0

        self.x += self.vx

        # Столкновение с границами по X
        if self.x + radius > sw:
            if self.onland:
                self.x = sw - radius
            else:
                self.vx = -self.vx
                S_punch1.play()
        if self.x - radius < 0:
            if self.onland:
                self.x = radius
            else:
                self.vx = -self.vx
                S_punch1.play()

        # Прыжок
        if keys[pygame.K_SPACE] and self.onland:
            self.gravity = -5  # начальная скорость прыжка
            self.onland = False
            S_punch1.play()

        # Гравитация
        self.vy = self.gravity
        self.y += self.vy
        self.gravity += 0.05  # сила гравитации

        # Проверка земли
        if self.y + radius >= sh:
            self.y = sh - radius
            self.vy = 0
            self.gravity = 0
            self.onland = True

        # Изменение цвета в воздухе
        if not self.onland:
            color = (255, 0, 0)

        # Отрисовка игрока
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), radius)
