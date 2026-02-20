# Tic-Tac-Toe AI using Minimax
# CodSoft AI Internship - Task 2

def print_board(board):
    print()
    for i in range(3):
        print(" " + board[i*3] + " | " + board[i*3+1] + " | " + board[i*3+2])
        if i < 2:
            print("---|---|---")
    print()


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


def main():
    board = [" " for _ in range(9)]
    
    board[0] = "X"
    board[1] = "X"
    board[2] = "X"
    
    print_board(board)
    
    if check_winner(board, "X"):
        print("X wins!")


if __name__ == "__main__":
    main()
