from Agent import Agent
import random
from Utils import *

class RandomAgent(Agent):
    def __init__(self, board, heuristic, depth, current_player):
        super().__init__(board, heuristic, depth, current_player)

    def do_action(self):
        legal_moves = CREATE_BOARD_TYPE.static_legal_moves(self.board.board, self.board.player)
        if len(legal_moves) > 0:
            return random.choice(legal_moves), None
        return None, None
