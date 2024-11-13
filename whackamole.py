import pygame
import sys
import random







def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("../../Desktop/lab10/whackamole-template/mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        LINE_COLOR = (0, 0, 0)
        mole_x = 0
        mole_y = 0

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                screen.fill("light green")

            # horizontal lines
                for i in range(0, 16):
                    pygame.draw.line(screen, LINE_COLOR, (0, i * 32), (640, i * 32), 1)

            # vertical lines
                for i in range(0, 20):
                    pygame.draw.line(screen, LINE_COLOR, (i * 32, 0), (i * 32, 512), 1)


                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    row = y//32
                    col = x//32
                    if (row, col) == (mole_y//32, mole_x//32): #if the grid the mouse is pressed is equal to the grid the mole is in

                        #reset random position
                        mole_x = random.randrange(0, 20) * 32
                        mole_y = random.randrange(0, 16) * 32


            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x, mole_y)))
            
            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    main()
