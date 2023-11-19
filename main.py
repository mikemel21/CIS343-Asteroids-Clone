import pygame as pg
from Player import Player

# Window Size
WIDTH, HEIGHT = 800, 800
BG_COLOR = (0, 0, 0)

def main ():
    # Initialize pygame
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()

    player = Player()

    delta = 0
    FPS = 60
    clock.tick(FPS)
    run = True
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        # player movement
        keys = pg.key.get_pressed()
        playerMoving = False
        if keys[pg.K_w]:
            playerMoving = True
            player.forward(delta)
        if keys[pg.K_a]:
            player.rotate(screen, "left")
        if keys[pg.K_d]:
            player.rotate(screen, "right")

        if not playerMoving:
            player.decelerate()

        # update
        player.update(delta)

        # draw
        screen.fill(BG_COLOR)

        player.draw(screen)

        pg.display.flip()

        delta = clock.tick(FPS)

if __name__ == "__main__":
    main()