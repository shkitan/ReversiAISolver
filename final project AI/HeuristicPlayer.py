from Agent import Agent
from Utils import *

class HeuristicPlayer(Agent):
    def __init__(self, board, heuristic, depth, current_player):
        super().__init__(board, heuristic, depth, current_player)

    def do_action(self):
        legal_moves = CREATE_BOARD_TYPE.static_legal_moves(self.board.board, self.board.player)
        if len(legal_moves) == 0:
            return None, None
        best_move = legal_moves[0]
        best_move_score = self.heuristic(self.board.board, self.board.player)
        for i in range(1, len(legal_moves)):
            new_score = self.heuristic(legal_moves[i].board, self.board.player)
            if new_score > best_move_score:
                best_move = legal_moves[i]
                best_move_score = new_score
        return best_move, best_move_score

