def tictactoe():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    player = 'X'
    moves = 0
    win = False

    # prints board
    def print_board():
        print()
        for i in range(0, len(board)):
            if (i+1) % 3 == 0:
                print(board[i])
                if i != 8:
                    print('---------')
            else:
                print(board[i], end=' | ')
        print()

    # toggles piece
    def toggle(position):
        while(position < 1 or position > 9):
            position = int(
                input('Invalid spot. Please enter another number: '))

        while(type(board[position-1]) == str):
            position = int(
                input('Spot already taken. Please enter another number: '))

        board[position-1] = player

    # checks for 3 in a row
    def check_win():
        nonlocal win
        # check vertical
        col = (position-1) % 3
        if board[col] == player and board[col+3] == player and board[col+6] == player:
            win = True
            return True

        # check horizontal
        if col == 0:
            if board[position] == player and board[position+1] == player:
                win = True
                return True
        elif col == 1:
            if board[position-2] == player and board[position] == player:
                win = True
                return True
        elif col == 2:
            if board[position-3] == player and board[position-2] == player:
                win = True
                return True

        # check diagnols
        if board[0] == player and board[4] == player and board[8] == player:
            win = True
            return True

        if board[2] == player and board[4] == player and board[6] == player:
            win = True
            return True

    # start of game
    print('Welcome to Tic-Tac-Toe')
    print_board()

    while moves < 9:
        print(f'Player {player},')
        position = int(input('Where would you like to place your piece? '))
        toggle(position)
        print_board()
        moves += 1

        if moves > 4:
            if check_win():
                break

        # switches turn
        if player == 'X':
            player = 'O'
        else:
            player = 'X'

    # result of game
    if win == False:
        print('Scratch')
    else:
        print(f'Player {player} wins!')

    # restart or exit
    again = input('Play again (Y/N)? ').upper()
    if again == 'Y':
        tictactoe()
    else:
        print('Good-bye')
        return


tictactoe()
