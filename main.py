import os
import random

c = ("\033[34mOX\033[37m" * 16)
c2 = ("-" * 32)

# SCREEN
def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

# G-BOARD
def print_board(board):
    print(c,"TIC-TAC-TOE".rjust(20), c, "", sep='\n')
    print("  Propoj 3 znaky a vyhraj hru!","", sep='\n')
    print("        +---+---+---+")
    for row in range(3):
        print(f"        | {board[row][0]} | {board[row][1]} | {board[row][2]} |")
        print("        +---+---+---+")
    print("",c,sep='\n')

# INIT_G_BOARD
def initialize_board():
    return [[" " for _ in range(3)] for _ in range(3)]

# ADD_SYMBOL
def make_move(board, player):
    while True:
        print(c2,f"        \033[37mHraje hráč {player}.",c2,sep='\n')
        move = input("zadej číslo pole (1-9): ").strip()
        print("")

        if move.isdigit() and 1 <= int(move) <= 9:
            move = int(move) - 1
            row = move // 3
            col = move % 3

            if board[row][col] == " ":
                board[row][col] = player
                break
            else:
                print("\033[31mPole je obsazené!\033[37m Zkus to znovu.")
        else:
            print("\033[31mMusíš zadat číslo pole!\033[37m (1 až 9)")

# WIN_CONTROL
def check_winner(board, player):

    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or all([board[j][i] == player for j in range(3)]):
            return True
        
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    
    return False

# PLAY_AGAIN
def play_again():
    while True:
        again = input("Chcete hrát znovu? (Y/N): ").upper()
        if again == "Y":
            return True
        elif again == "N":
            return False
        else:
            print("Neplatná volba. Zadej 'Y' nebo 'N'.")

# RAND_PLAY_START
def random_player():
    return random.choice(["X", "O"])

# GAME
def main():
    while True:
        board = initialize_board()
        current_player = random_player()
        turns = 0

        while turns < 9:
            clear_screen()
            print_board(board)
            make_move(board, current_player)
            
            if check_winner(board, current_player):
                clear_screen()
                print_board(board)
                print("")
                print(c2,f"Hráč {current_player} vyhrál! \033[33mGratuluji!\033[37m",c2,sep='\n')
                break
            
            current_player = "O" if current_player == "X" else "X"
            turns += 1

        if turns == 9:
            clear_screen()
            print_board(board)
            print("")
            print("Je to remíza!")
            print("")

        if not play_again():
            print("Ukončuji program. Díky za hru!")
            break

if __name__ == "__main__":
    main()
