from HeuristicPlayer import HeuristicPlayer
from RandomAgent import RandomAgent
from CreateBoard import *
from MinMaxAgent import MinMaxAgent
from Utils import *
import numpy as np
from ModelMinMaxAgent import *
from ModelHeuristicAgent import *

agents_dict = {"random": RandomAgent, "minmax": MinMaxAgent, "heuristic": HeuristicPlayer, "modelMinMax": ModelMinMaxAgent,
               "ModelHeuristic": ModelHeuristicAgent}


class Reversi:
    def __init__(self, agent1, agent2, heuristic1=None, depth1=None, heuristic2=None, depth2=None):
        self.board = CREATE_BOARD_TYPE()
        # self.pyboard = [] # TODO delete
        self.agent1 = agents_dict[agent1](self.board, heuristic1, depth1, 0)
        self.agent2 = agents_dict[agent2](self.board, heuristic2, depth2, 1)

    def game_over(self):
        for x in range(WIDTH):
            for y in range(HEIGHT):
                if CREATE_BOARD_TYPE.static_validation(self.board.board, Player.PLAYER_1, x, y) or CREATE_BOARD_TYPE.static_validation(self.board.board, Player.PLAYER_2, x, y):
                    return False
        return True


    # def create_py_board(self):
    #     board = []
    #     for i in range(8):
    #         row = []
    #         for j in range(8):
    #             if self.board.board[i][j].player == Player.PLAYER_1:
    #                 row.append(1)
    #             elif self.board.board[i][j].player == Player.PLAYER_2:
    #                 row.append(2)


    def run(self):
        if CREATE_BOARD_TYPE != CreateBoardRandomStart:
            # to create non deterministic moves
            for i in range(2):
                random1 = RandomAgent(self.board, None, None, None)
                act, _ = random1.do_action()
                x = act.loc[0]
                y = act.loc[1]
                self.board.move(x, y)
        while True:
            if self.game_over():
                return self.board.board
            if (self.board.player == Player.PLAYER_1):
                if not self.agent1.has_legal_action():
                    self.board.player = Player.PLAYER_2
                    continue
                else:
                    act, _ = self.agent1.do_action()
                    x = act.loc[0]
                    y = act.loc[1]
                    self.board.move(x, y)
            else:
                if not self.agent2.has_legal_action():
                    self.board.player = Player.PLAYER_1
                    continue
                else:
                    act, _ = self.agent2.do_action()
                    x = act.loc[0]
                    y = act.loc[1]
                    self.board.move(x, y)

# TODO: EVALUATIONNNNNNNNNN

#
# x = Reversi("minmax", "minmax", weight_combined_heuristic, 2, weight_combined_heuristic, 2)
# x.run()

# x = Reversi("minmax", "random", weight_combined_heuristic, 2, None, None)
# x.run()