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