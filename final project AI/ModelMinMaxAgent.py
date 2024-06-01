import numpy as np
from CreateBoard import *
from Agent import Agent
from Utils import *
# must be the first player!!!!!!!!!!!!!!!
class ModelMinMaxAgent(Agent):
    def __init__(self, board, models, depth, current_player):
        super().__init__(board, models, depth, current_player)

    def do_action(self):
        legal_moves = CREATE_BOARD_TYPE.static_legal_moves(self.board.board, self.board.player)
        if len(legal_moves) == 0:
            return None
        best_scores = np.zeros(len(legal_moves))
        # files = ["player0_minmax_player1_random_Combined", "player0_minmax_player1_random_weight", "player0_minmax_player1_minmax_Combined",
        #          "player0_minmax_player1_minmax_weight", "player0_minmax_player1_heuristic_Combined", "player0_minmax_player1_heuristic_weight"]
        # for i in range(len(files)):
        #     self.heuristic[i].load_weights(files[i])
        for i in range(len(legal_moves)):
            for j in range(len(self.heuristic)):
                if self.current_player == 0:
                    new_score = self.heuristic[j].calculate_q_value(legal_moves[i].board, Player.PLAYER_1)
                else:
                    opposite_board = switch_board_players(legal_moves[i].board)
                    new_score = self.heuristic[j].calculate_q_value(opposite_board, Player.PLAYER_2)
                best_scores[i] += new_score[0][0][0]
        best_index = np.argmax(best_scores)
        return legal_moves[best_index], best_scores[best_index]

