import pygame
from Board import Board
pygame.init()

# Define some colors
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)
CLOSED_COLOR = (180, 180, 180)
OPEN_COLOR = (150, 150, 150)
MINE_COLOR = RED
# Open a new window
size = (512, 512)
border = 2
mouse_down_square = (-1, -1)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Minesweeper")
# The loop will carry on until the user exits the game (e.g. clicks the close button).
carryOn = True
font = pygame.font.Font('freesansbold.ttf', 32)

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

board = Board(16, 16, 30)
square_size = (size[0] / board.width - border, size[1] / board.height - border)
left_click_last_square = (-1, -1)
right_click_last_square = (-1, -1)


# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    left_down = False
    right_down = False
    left_up = False
    right_up = False
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            carryOn = False # Flag that we are done so we can exit the while loop

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                left_down = True
            elif event.button == 3:
                right_down = True
            
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                left_up = True
            elif event.button == 3:
                right_up = True
            
    # --- Game logic should go here
    
    # --- Drawing code should go here
    # First, clear the screen to white. 
    screen.fill(WHITE)
    #The you can draw different shapes and lines or add text to your background stage.
    #pygame.draw.rect(screen, RED, [0, 0, *square_size],0
    
    coordinates = [border / 2, border / 2]
    for i in range(board.width):
        for j in range(board.height):
            square = pygame.Rect(coordinates[0], coordinates[1], *square_size)
            square_color = RED
            square_text = ""
            if square.collidepoint(pygame.mouse.get_pos()):
                square_color = GREEN
                if left_down:
                    print("left_down")
                    left_click_last_square = (i, j)
                if right_down:
                    print("right_down")
                    right_click_last_square = (i, j)
                if left_up:
                    print("left_up")
                    if (i, j) == left_click_last_square:
                        board.dig(i, j)
                if right_up:
                    print("right up")
                    if (i, j) == right_click_last_square:
                        board.flag(i, j)

            data = board.get_square(i, j)
            game_over = not board.alive or board.win()
            
            
            
            if data["status"] == 1 and not game_over:
                square_color = CLOSED_COLOR
            elif data["status"] == 0 or game_over:
                if data["danger"] == -1:
                    if board.alive:
                        square_color = GREEN
                        
                    else:
                        square_color = MINE_COLOR
                        
                elif data["danger"] == 0:
                    square_color = OPEN_COLOR
                else:
                    square_color = OPEN_COLOR
                    danger = data["danger"]
                    square_text = str(danger)
                    
                    
            elif data["status"] == -1:
                square_color = CLOSED_COLOR
                square_text = "!"

    
                
            
                
            pygame.draw.rect(screen, square_color, square, 0)
            text = font.render(square_text, True, BLACK)
            textRect = text.get_rect()
            textRect.center = (coordinates[0] + square_size[0] / 2, coordinates[1] + square_size[1] / 2)
            screen.blit(text, textRect)
            coordinates[1] += square_size[1] + border
        coordinates[0] += square_size[0] + border
        coordinates[1] = border / 2

    if board.win():  
        text = font.render("You win! GG", True, BLACK, WHITE)
        textRect = text.get_rect()
        textRect.center = (size[0] / 2, size[1] / 2)
        screen.blit(text, textRect)

    elif not board.alive:
        text = font.render("You lose. Try again!", True, BLACK, WHITE)
        textRect = text.get_rect()
        textRect.center = (size[0] / 2, size[1] / 2)
        screen.blit(text, textRect)
        

        
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
     
    # --- Limit to 60 frames per second
    clock.tick(60)
 
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()
