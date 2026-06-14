import os

def clear_screen():
    """Clears the console screen for a better UI experience."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board):
    """Prints the current state of the Tic-Tac-Toe board."""
    clear_screen()
    print('\n\tTic Tac Toe - NIIT Foundation (Cisco)\n')
    print('Player 1 (X)  -  Player 2 (O)\n')
    
    print('     |     |     ')
    print(f'  {board[1]}  |  {board[2]}  |  {board[3]}  ')
    print('_____|_____|_____')
    print('     |     |     ')
    print(f'  {board[4]}  |  {board[5]}  |  {board[6]}  ')
    print('_____|_____|_____')
    print('     |     |     ')
    print(f'  {board[7]}  |  {board[8]}  |  {board[9]}  ')
    print('     |     |     \n')

def check_win(board):
    """Checks all 8 possible winning conditions."""
    win_conditions = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9), # Horizontal rows
        (1, 4, 7), (2, 5, 8), (3, 6, 9), # Vertical columns
        (1, 5, 9), (3, 5, 7)             # Diagonals
    ]
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c]:
            return True
    return False

def check_draw(board):
    """Checks if all spots are filled (meaning no numbers are left)."""
    return all(isinstance(spot, str) for spot in board[1:])

def main():
    """Main game loop and logic."""
    # Index 0 is ignored for easier 1-9 mapping
    board = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  
    player = 1

    while True:
        print_board(board)
        current_mark = 'X' if player == 1 else 'O'

        print(f'Player {player} ({current_mark}), it is your turn.')

        # Input validation to prevent crashes
        try:
            choice = int(input('Enter a number (1-9): '))
        except ValueError:
            print('Invalid input! Please enter a valid number.')
            input('Press Enter to try again...')
            continue

        # Check if choice is within bounds and the spot is available
        if 1 <= choice <= 9 and board[choice] == choice:
            board[choice] = current_mark
        else:
            print('Invalid move! That spot is either taken or out of bounds.')
            input('Press Enter to try again...')
            continue

        # Check for Win or Draw
        if check_win(board):
            print_board(board)
            print(f'🎉 RESULT: Player {player} ({current_mark}) wins! 🎉\n')
            break

        if check_draw(board):
            print_board(board)
            print('🤝 RESULT: It is a draw! 🤝\n')
            break

        # Switch turns
        player = 2 if player == 1 else 1

if __name__ == '__main__':
    main()