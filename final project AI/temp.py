import numpy as np
from Agent import Agent
from CreateBoard import *
from Utils import *
dict_idx_to_player = { 0: Player.PLAYER_1, 1: Player.PLAYER_2}

class MinMaxAgent(Agent):
    def __init__(self, board, heuristic, depth):
        super().__init__(board, heuristic, depth)


    # def minimax_algorithm(self, state, index_player, depth):
    #     if depth == 0:
    #         return self.heuristic(state, dict_idx_to_player[index_player])
    #     if not self.has_legal_action():
    #         return self.heuristic(state, dict_idx_to_player[index_player])
    #     if index_player == 1:  # Min player
    #         val = np.inf
    #         actions = CreateBoard.static_legal_moves(state, dict_idx_to_player[index_player])
    #         num_actions = len(actions)
    #         action_idx = 0
    #         while num_actions > 0:
    #             curr_min= self.minimax_algorithm(actions[action_idx].board, 0, depth - 1)
    #             if curr_min < val:
    #                 val = curr_min
    #             num_actions -= 1
    #             action_idx += 1
    #         return val
    #     else:  # Max player
    #         val = - np.inf
    #         actions = CreateBoard.static_legal_moves(state, dict_idx_to_player[index_player])
    #         num_actions = len(actions)
    #         action_idx = 0
    #         while num_actions > 0:
    #             curr_max = self.minimax_algorithm(actions[action_idx].board, 1, depth)
    #             if curr_max > val:
    #                 val = curr_max
    #             num_actions -= 1
    #             action_idx += 1
    #         return val
    #
    # def do_action(self):
    #     """
    #     Returns the minimax action from the current gameState using self.depth
    #     and self.evaluationFunction.
    #
    #     Here are some method calls that might be useful when implementing minimax.
    #
    #     game_state.get_legal_actions(agent_index):
    #         Returns a list of legal actions for an agent
    #         agent_index=0 means our agent, the opponent is agent_index=1
    #
    #     Action.STOP:
    #         The stop direction, which is always legal
    #
    #     game_state.generate_successor(agent_index, action):
    #         Returns the successor game state after an agent takes an action
    #     """
    #     actions = self.board.legal_moves()
    #     num_actions = len(actions)
    #     action_idx = 0
    #     max_val = 0
    #     action = None
    #     while num_actions > 0:
    #         if action_idx == 0:
    #             val = self.minimax_algorithm(self.board.board, 1, self.depth)
    #             max_val = val
    #             action = actions[action_idx]
    #         else:
    #             val = self.minimax_algorithm(self.board.board, 1, self.depth)
    #             if val > max_val:
    #                 max_val = val
    #                 action = actions[action_idx]
    #         num_actions -= 1
    #         action_idx += 1
    #     return action, max_val

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
                beta = min(beta, self.alpha_beta_algorithm(alpha, beta, actions[action_idx].board, 0, depth - 1))
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
                alpha = max(alpha, self.alpha_beta_algorithm(alpha, beta, actions[action_idx].board, 1, depth))
                if alpha >= beta:
                    break
                num_actions -= 1
                action_idx += 1
            return alpha

    def do_action(self):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        actions = self.board.legal_moves()
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

