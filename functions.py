# Libraries
import chess
import random
import chess.polyglot
import chess
import chess.svg
from IPython.display import SVG
import pandas as pd


#%% Functions

# Return a random board
def rand_board(moves):
    ''' Returns a random board with a given number of moves'''
    board = chess.Board()
    for i in range(moves):
        rand_move = random.choice(list(board.legal_moves))
        # Print the move
        print(rand_move)
        board.push(rand_move)
    return print(board)          # Return printed or FEN board

rand_board(10)

# Return a random changing move
def rand_board_moves_df(moves):
    ''' Move given number of moves and return a DataFrame with the chosen move, the number of possible moves, and all moves'''
    board = chess.Board()
    data = []
    for i in range(moves):
        # Get all legal moves
        moves_list = []
        for move in board.legal_moves:
            moves_list.append(str(move))
        # Get a random move
        rand_move = random.choice(list(board.legal_moves))
        # Count the possible moves
        num_moves = len(moves_list)
        # Append data to list
        data.append([rand_move, num_moves, moves_list])
        # Make the move
        board.push(rand_move)

    # Return dataframe with the chosen move, the number of possible moves and all moves
    df = pd.DataFrame(data, columns=['Chosen Move', 'Number of Possible Moves', 'All Moves'])
    return df

rand_board_moves_df(10)

#%%
def rand_board_moves(moves):
    ''' Move given number of moves and return a DataFrame with the chosen move, the number of possible moves, and all moves'''
    board = chess.Board()
    data = []
    for i in range(moves):
        # Get all legal moves
        moves_list = []
        for move in board.legal_moves:
            moves_list.append(str(move))
        # Get a random move
        rand_move = random.choice(list(board.legal_moves))
        # Count the possible moves
        num_moves = len(moves_list)
        # Append data to list
        data.append([rand_move, num_moves, moves_list])
        # Make the move
        board.push(rand_move)

    # Return dataframe with the chosen move, the number of possible moves and all moves
    df = pd.DataFrame(data, columns=['Chosen Move', 'Number of Possible Moves', 'All Moves'])
    return SVG(chess.svg.board(board, size=400, lastmove=board.peek()))