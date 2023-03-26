# Python Chess Game

# Libraries
import chess
import random
import pandas as pd
import chess.polyglot
import chess
import chess.svg
from IPython.display import SVG
#%%
#
board = chess.Board()
legal_moves = board.legal_moves
board.push_san("e4")
board.push_san("e5")
board.push_san("Nf3")
board.push_san("Nc6")
board.push_san("Bb5")
board.push_san("a6")
board.push_san("Ba4")
board.push_san("Nf6")
board.push_san("O-O")
board.push_san("b5")
print(board)

#%% Random Game

# First move
board = chess.Board()

# Return a random changing move
rand_move = random.choice(list(board.legal_moves))
# Make the move
board.push(rand_move)
board

