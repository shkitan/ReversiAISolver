from Utils import *

class Agent:
    def __init__(self, board, heuristic, depth, current_player):
        self.board = board
        self.depth = depth
        self.heuristic = heuristic
        self.current_player = current_player

    def has_legal_action(self):
        return len(CREATE_BOARD_TYPE.static_legal_moves(self.board.board, self.board.player)) != 0

    def do_action(self):
        raise NotImplementedError
