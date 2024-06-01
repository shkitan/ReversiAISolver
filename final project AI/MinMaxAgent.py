import numpy as np
from Agent import Agent
from CreateBoard import *
from Utils import *
dict_idx_to_player = { 0: Player.PLAYER_1, 1: Player.PLAYER_2}

class MinMaxAgent(Agent):
    def __init__(self, board, heuristic, depth, current_player):
        super().__init__(board, heuristic, depth, current_player)

#### Original


    def alpha_beta_algorithm(self, alpha, beta, state, index_player, depth):
        if depth == 0:
            return self.heuristic(state, dict_idx_to_player[index_player])
        if not self.has_legal_action():
            return self.heuristic(state, dict_idx_to_player[index_player])
        if index_player == 1:  # Min player
            actions = CREATE_BOARD_TYPE.static_legal_moves(state, dict_idx_to_player[index_player])
            num_actions = len(actions)
            action_idx = 0
            while num_actions > 0:
                beta = min(beta, self.alpha_beta_algorithm(alpha, beta, actions[action_idx].board, 1 - index_player, depth - 1))
                if alpha >= beta:
                    break
                num_actions -= 1
                action_idx += 1
            return beta
        else:  # Max player
            actions = CREATE_BOARD_TYPE.static_legal_moves(state, dict_idx_to_player[index_player])
            num_actions = len(actions)
            action_idx = 0
            while num_actions > 0:
                alpha = max(alpha, self.alpha_beta_algorithm(alpha, beta, actions[action_idx].board, 1 - index_player, depth))
                if alpha >= beta:
                    break
                num_actions -= 1
                action_idx += 1
            return alpha

    def do_action(self):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        actions = CREATE_BOARD_TYPE.static_legal_moves(self.board.board, self.board.player)
        num_actions = len(actions)
        action_idx = 0
        max_val = 0
        action = None
        alpha = -np.inf
        beta = np.inf
        while num_actions > 0:
            if action_idx == 0:
                val = self.alpha_beta_algorithm(alpha, beta,  actions[action_idx].board, 1, self.depth)
                max_val = val
                action = actions[action_idx]
            else:
                val = self.alpha_beta_algorithm(alpha, beta,  actions[action_idx].board, 1, self.depth)
                if val > max_val:
                    max_val = val
                    action = actions[action_idx]
            num_actions -= 1
            action_idx += 1
        return action, max_val


# New Shir and David - not good!!!
#     def alpha_beta_algorithm(self, alpha, beta, state, index_player, depth, a):
#         actions = CREATE_BOARD_TYPE.static_legal_moves(state,  dict_idx_to_player[index_player])
#
#         if depth == self.depth:
#             return a, self.heuristic(state, dict_idx_to_player[index_player])
#         if not self.has_legal_action():
#             return a, self.heuristic(state, dict_idx_to_player[index_player])
#         if dict_idx_to_player[index_player] != self.current_player:  # Min player
#             min_val = np.inf
#             act = None
#             num_actions = len(actions)
#             action_idx = 0
#             while num_actions > 0:
#                 _, score = self.alpha_beta_algorithm(alpha, beta, actions[action_idx].board, 1 - index_player, depth + 1, actions[action_idx])
#                 if score <= min_val:
#                     min_val = beta
#                     act = actions[action_idx]
#                 beta = min(beta, score)
#                 if alpha >= beta:
#                     break
#                 num_actions -= 1
#                 action_idx += 1
#             return act, min_val
#         else:  # Max player
#             max_val = -np.inf
#             act = None
#             num_actions = len(actions)
#             action_idx = 0
#             while num_actions > 0:
#                 _, score = self.alpha_beta_algorithm(alpha, beta, actions[action_idx].board, 1 - index_player, depth, actions[action_idx])
#                 if score >= max_val:
#                     max_val = score
#                     act = actions[action_idx]
#                     alpha = max(alpha, score)
#                 if alpha >= beta:
#                     break
#                 num_actions -= 1
#                 action_idx += 1
#             return act, max_val
#
#     def do_action(self):
#         """
#         Returns the minimax action using self.depth and self.evaluationFunction
#         """
#         action = None
#         alpha = -np.inf
#         beta = np.inf
#         action, max_val = self.alpha_beta_algorithm(alpha, beta,  self.board.board, self.current_player, 0, action)
#         return action, max_val





