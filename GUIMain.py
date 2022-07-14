import pygame
from Board import Board
pygame.init()

# Define some colors
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)

# Open a new window
size = (512, 512)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Minesweeper")
# The loop will carry on until the user exits the game (e.g. clicks the close button).
carryOn = True
 
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

board = Board(16, 16, 16)
square_size = (size[0] / board.width, size[1] / board.height)


# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we can exit the while loop
 
    # --- Game logic should go here
 
    # --- Drawing code should go here
    # First, clear the screen to white. 
    screen.fill(WHITE)
    #The you can draw different shapes and lines or add text to your background stage.
    pygame.draw.rect(screen, RED, [0, 0, *square_size],0)
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
     
    # --- Limit to 60 frames per second
    clock.tick(60)
 
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()
