import pygame
from pygame.locals import *
import time

SIZE = 40


class Apple:
    def __init__(self, surface):
        self.parent_screen = surface
        self.apple = pygame.image.load(
            "Snake_Game/resources/apple.jpg").convert()
        self.x = SIZE * 3
        self.y = SIZE * 3

    def draw(self):
        self.parent_screen .blit(self.apple, (self.x, self.y))
        pygame.display.flip()

class Snake:
    def __init__(self, surface, length):
        self.parent_screen = surface
        self.len = length
        self.block = pygame.image.load(
            "Snake_Game/resources/block.jpg").convert()
        self.x = [SIZE] * length
        self.y = [SIZE] * length
        self.direction = "right"

    def draw(self):
        self.parent_screen.fill((108, 57, 145))
        for i in range(self.len):
            self.parent_screen .blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

    def move_up(self):
        self.direction = "up"

    def move_down(self):
        self.direction = "down"

    def move_left(self):
        self.direction = "left"

    def move_right(self):
        self.direction = "right"

    def move(self):

        for i in range(self.len - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        if self.direction == "up":
            self.y[0] -= SIZE
        elif self.direction == "down":
            self.y[0] += SIZE
        elif self.direction == "left":
            self.x[0] -= SIZE
        elif self.direction == "right":
            self.x[0] += SIZE

        self.draw()

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 600))
        self.surface.fill((108, 57, 145))

        self.snake = Snake(self.surface, 2)
        self.snake.draw()

        self.apple = Apple(self.surface)
        self.apple.draw()

    def play(self):
        self.snake.move()
        self.apple.draw()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_UP:
                        self.snake.move_up()
                    if event.key == K_DOWN:
                        self.snake.move_down()
                    if event.key == K_LEFT:
                        self.snake.move_left()
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                elif event.type == QUIT:
                    running = False
            
            self.play()
            time.sleep(0.3)


if __name__ == "__main__":
    game = Game()
    game.run()

    pygame.display.flip()

    
