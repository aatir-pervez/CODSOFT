# Tic-Tac-Toe AI using Minimax
# CodSoft AI Internship - Task 2

def print_board(board):
    print()
    for i in range(3):
        print(" " + board[i*3] + " | " + board[i*3+1] + " | " + board[i*3+2])
        if i < 2:
            print("---|---|---")
    print()


def main():
    board = [" " for _ in range(9)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)


if __name__ == "__main__":
    main()
