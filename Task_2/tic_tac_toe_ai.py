
# Tic-Tac-Toe AI using Minimax
# CodSoft AI Internship - Task 2
import random
def print_board(board):
    print()
    for i in range(3):
        print(" " + board[i*3] + " | " + board[i*3+1] + " | " + board[i*3+2])
        if i < 2:
            print("---|---|---")
    print()

def ai_move(board):
    available_positions = [i for i in range(9) if board[i] == " "]
    move = random.choice(available_positions)
    board[move] = "O"
    


def check_winner(board, player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],   # Rows
        [0,3,6], [1,4,7], [2,5,8],   # Columns
        [0,4,8], [2,4,6]             # Diagonals
    ]
    
    for positions in win_positions:
        if board[positions[0]] == player and \
           board[positions[1]] == player and \
           board[positions[2]] == player:
            return True
    return False


def is_draw(board):
    return " " not in board


def main():
    board = [" " for _ in range(9)]
    
    print("Welcome to Tic-Tac-Toe!")
    print("You are X. Choose position 0-8.\n")
    
    print_board(board)

    while True:
        # Human Move
        move = int(input("Enter your move (0-8): "))
        
        if board[move] != " ":
            print("Position already taken! Try again.")
            continue
        
        board[move] = "X"
        print_board(board)
        
        if check_winner(board, "X"):
            print("You win!")
            break

        if is_draw(board):
            print("It's a draw!")
            break

        # AI Move
        print("AI is making a move...")
        ai_move(board)
        print_board(board)

        if check_winner(board, "O"):
            print("AI wins!")
            break

        if is_draw(board):
            print("It's a draw!")
            break
   
if __name__ == "__main__":
    main()
