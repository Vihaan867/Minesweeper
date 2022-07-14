from Board import Board
print("Welcome to Minesweeper!")
while True:
    try:
        board_size = input("What board size of Minesweeper do you want to play? ")
        number_of_mines = input("How many mines do you want on the board? ")
        number_of_mines = int(number_of_mines)
        board_size = board_size.split()
        board_size[0] = int(board_size[0])
        board_size[1] = int(board_size[1])
        if number_of_mines > board_size[0] * board_size[1]:
            print("The number of mines you inputted won't fit in the board.")
            continue
    except ValueError:
        print("The size of the board must be formatted in numbers.")
        continue

    break

board = Board(*board_size, number_of_mines)

while True:
    print(board)
    while True:
        try:
            while True:
                user_choice = input("Do you want to flag or dig a square? Enter d or f followed by coordinates.")
                user_choice = user_choice.split()
                if len(user_choice) == 3:
                    break
            x = int(user_choice[1]) - 1
            y = int(user_choice[2]) - 1
            if x < 0 or x >= board.width or y < 0 or y >= board.height:
                print("The coordinates you inputted were outside the board.")
                continue
            if user_choice[0] not in ("f", "d"):
                print("The command you inputted doesn't exist.")
                continue
        except ValueError:
            print("You need to input coordinates in the form of integers.")
            continue
        break
    if user_choice[0] == "f":
        board.flag(x, y)

    elif user_choice[0] == "d":
        board.dig(x, y)
        if not board.alive:
            break

    if board.win():
        break
print(board)

if board.alive == True:
    print("You win!")

else:
    print("Game over. You lose!")
        
        
    
        
        
    
    

