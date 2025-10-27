'''

Last time, you implemented the functions:
- print_board()
- check_winner()

Today, you will use these functions to create an unbeatable Tic Tac Toe AI that plays against a human player.

Your goal:
1. Display the Tic Tac Toe board.
2. Alternate turns between the human player and the AI.
3. Use check_winner() after each move to detect a win or draw.
4. Make sure the AI never loses!

The function AI(board, player) is already provided.
- It takes the current board and the AI's symbol ('X' or 'O') as input.
- It returns the best move for the AI to play.
Your task is to integrate this function into your game loop.
'''
def AI(board, player):
    # Don't worry to much about the code here. It's just a bunch of maths
    # to make the AI work
    import math

    board = [[x if x != ' ' else '' for x in row] for row in board]

    def is_moves_left(b):
        return any('' in row for row in b)

    def evaluate(b):
        for i in range(3):
            if b[i][0] == b[i][1] == b[i][2] != '':
                return 10 if b[i][0] == 'X' else -10
            if b[0][i] == b[1][i] == b[2][i] != '':
                return 10 if b[0][i] == 'X' else -10
        if b[0][0] == b[1][1] == b[2][2] != '':
            return 10 if b[0][0] == 'X' else -10
        if b[0][2] == b[1][1] == b[2][0] != '':
            return 10 if b[0][2] == 'X' else -10
        return 0

    def minimax(b, depth, is_max):
        score = evaluate(b)
        if score == 10 or score == -10:
            return score - depth if score > 0 else score + depth
        if not is_moves_left(b):
            return 0

        if is_max:
            best = -math.inf
            for i in range(3):
                for j in range(3):
                    if b[i][j] == '':
                        b[i][j] = 'X'
                        best = max(best, minimax(b, depth + 1, False))
                        b[i][j] = ''
            return best
        else:
            best = math.inf
            for i in range(3):
                for j in range(3):
                    if b[i][j] == '':
                        b[i][j] = 'O'
                        best = min(best, minimax(b, depth + 1, True))
                        b[i][j] = ''
            return best

    best_val = -math.inf if player == 'X' else math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == '':
                board[i][j] = player
                move_val = minimax(board, 0, player == 'O')
                board[i][j] = ''
                if (player == 'X' and move_val > best_val) or (player == 'O' and move_val < best_val):
                    best_val = move_val
                    best_move = (i, j)
    return best_move


# example use of the AI

board = [
['X','O','X'],
['O','X','O'],
['O',' ','']
]

best_move = AI(board, 'O')
print(best_move)

print(board)


# How to proceed

# Step 1: Create a 3x3 board (list of lists) filled with spaces
# Hint: Use a list comprehension or manually write it out.
# Example idea: [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
board = ...

# Step 2: Choose symbols for human and AI
# (You can decide or ask the player!)
# Example idea: human = 'O', ai = 'X'
human = ...
ai = ...

# Step 3: Start a game loop
# Hint: Use `while True:` to keep the game running until someone wins or it’s a draw.
while True:
    # 3a. Show the current board
    # Call print_board(board)
    ...

    # 3b. Ask the human for a move
    # - Ask for row and column numbers (0, 1, or 2)
    # - Check that the chosen cell is empty (' ')
    # - Place their symbol on the board
    # Hint: Use input(), int(), and simple if-checks
    ...

    # 3c. Check if the human won or if it’s a draw
    # - Call check_winner(board)
    # - If it returns something other than None, show the board, print the result, and break out of the loop
    ...

    # 3d. Let the AI play
    # - Use AI(board, ai) to get the best (row, col)
    # - Place the AI’s symbol on the board
    # - Print what move the AI made
    ...

    # 3e. Check if the AI won or if it’s a draw (same as above)
    ...

# Optional Step 4:
# After the game ends, you can ask:
# “Play again?” and reset the board if the player says yes.