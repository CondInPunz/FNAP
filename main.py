import pygame

WIDTH = 1280
HEIGHT = 720

FPS = 30

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

MAIN_MENU = 0
LOAD_GAME = 1
GAME_MODE = 2
GAME_OVER = 3


def main():
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption('FNAP')
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    running = True
    while running:
        screen.fill(BLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()


if __name__ == '__main__':
    main()
