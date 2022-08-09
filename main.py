import pygame
from pygame.locals import *
import time
import random

SIZE = 40
BACKGROUND_COLOR = (108, 57, 145)

class Apple:
    def __init__(self, surface):
        self.parent_screen = surface
        self.apple = pygame.image.load(
            "Snake_Game/resources/apple.jpg").convert()
        self.x = SIZE * 8
        self.y = SIZE * 8

    def draw(self):
        self.parent_screen .blit(self.apple, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = SIZE * random.randint(0, 24)
        self.y = SIZE * random.randint(0, 14)

class Snake:
    def __init__(self, surface, length):
        self.parent_screen = surface
        self.len = length
        self.block = pygame.image.load(
            "Snake_Game/resources/block.jpg").convert()

        self.x = [SIZE] * length
        self.y = [SIZE] * length
        self.direction = "right"

    def ate_apple(self):
        self.len += 1
        self.x.append(-1)
        self.y.append(-1)

    def draw(self):
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
        pygame.mixer.init()

        self.play_bg_music()

        self.surface = pygame.display.set_mode((1000, 600))

        self.snake = Snake(self.surface, 1)
        self.snake.draw()

        self.apple = Apple(self.surface)
        self.apple.draw()

        self.pause = False

    def render_bg(self):
        bg = pygame.image.load("Snake_Game/resources/background.jpg")
        self.surface.blit(bg, (0, 0))

    def play(self):
        self.render_bg()
        self.snake.move()
        self.apple.draw()
        self.display_score()

        # collision with apple
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            pygame.mixer.Sound("Snake_Game/resources/1_snake_game_resources_ding.mp3").play()
            self.snake.ate_apple()
            self.apple.move()

        # collision with itself
        for i in range(1, self.snake.len):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                pygame.mixer.Sound("Snake_Game/resources/1_snake_game_resources_crash.mp3").play()
                self.pause = True
                pygame.mixer.music.pause()
                self.display_game_over()

        # collision with the wall
        if self.snake.x[0] >= 1000 or self.snake.x[0] < 0 or self.snake.y[0] >= 600 or self.snake.y[0] < 0:
            pygame.mixer.Sound("Snake_Game/resources/1_snake_game_resources_crash.mp3").play()
            self.pause = True
            pygame.mixer.music.pause()
            self.display_game_over()

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True

        return False

    def play_bg_music(self):
        pygame.mixer.music.load("Snake_Game/resources/Queen - 'Bohemian Rhapsody'.mp3")
        pygame.mixer.music.play()

    def display_score(self):
        font = pygame.font.SysFont("comicsansms", 25)
        score = font.render(f"Score: {self.snake.len}", True, (255, 255, 255))
        self.surface.blit(score, (850, 10))
        pygame.display.flip()

    def display_game_over(self):
        self.surface.fill((10, 10, 10))
        font = pygame.font.SysFont("comicsansms", 50)
        font2 = pygame.font.SysFont("comicsansms", 20)

        over = font.render("Game Over", True, (235, 9, 9))
        self.surface.blit(over, (375, 200))

        score = font.render(f"Score: {self.snake.len}", True, (235, 9, 9))
        self.surface.blit(score, (390, 250))

        warning = font2.render("Press SPACE to play again. Press ESC to exit", True, (97, 94, 94))
        self.surface.blit(warning, (325, 340))

        pygame.display.flip()
        
    def reset(self):
        self.snake = Snake(self.surface, 1)
        self.apple = Apple(self.surface)
        pygame.mixer.music.unpause()

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_SPACE:
                        self.pause = False
                        self.reset()
                    
                    if not self.pause:
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
            
            if not self.pause:
                self.play()
    
            time.sleep(0.3)


if __name__ == "__main__":
    game = Game()
    game.run()

    pygame.display.flip()

    
