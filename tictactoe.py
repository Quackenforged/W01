#in main we will need to call a function for the board, the players and their turns, and how someone wins
def main():
    player = next_turn("")
    board = create_board()
    while not (winner(board) or no_contest(board)):
        display(board)
        move(player, board)
        player = next_turn(player)
        
    display(board)
    print("Good game. Thanks for playing!")

#we will need to create a list for the symbols for the board
def create_board():
    board = []
    for space in range(9):
        board.append(space + 1)
    return board

#we will need a way to display characters to form the board
def display(board):
    print()
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print("-----")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-----")
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print()

#Here we define a Tie
def no_contest(board):
    for space in range(9):
        if board[space] !="x" and board[space] != "O":
            #cannot be FALSE must be False
            return False
    return True

#Here we define the winner          
def winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])



#Here we will define how a turn is played
def move(player, board):
    space = int(input(f"{player}'s turn to choose a space (1-9): "))
    board[space - 1] = player

#Here we define how the turns progress
def next_turn(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"

if __name__ == "__main__":
    main()