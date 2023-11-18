import pygame as pg


# Window Size
WIDTH, HEIGHT = 800, 800
BG_COLOR = (0, 0, 0)

def main ():
    # Initialize pygame
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()

    FPS = 60
    clock.tick(FPS)
    run = True
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        # update

        # draw
        screen.fill(BG_COLOR)
        pg.display.flip()
        delta = clock.tick(FPS)

if __name__ == "__main__":
    main()