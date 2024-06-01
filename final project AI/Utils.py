import heapq

import numpy as np

from CreateBoard import *
import matplotlib.pyplot as plt
from copy import deepcopy
from CreateBoardThreeSpecific import CreateBoardThreeSpecific
from CreateBoardRandomStart import *
CREATE_BOARD_TYPE = CreateBoard
NUM_OF_GAMES = 5
EPOCHS = 7
DEPTH = 2

# This heuristic adds 1 for every cell with the player color, and adds -1 for every cell with the opponent player color
def base_heuristic(board, player):
    sum = 0
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if board[x][y].player == player:
                sum += 1
            elif board[x][y].player is None:
                continue
            else:
                sum -= 1
    return sum / 64


def difference_heuristic(board, player):
    sum1 = 0
    sum2 = 0
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if board[x][y].player == player:
                sum1 += 1
            elif board[x][y].player is None:
                continue
            else:
                sum2 -= 1
    return (sum1 - sum2) / 64


def find_neighbors(board, x, y):
    neighbours = []
    for i in range(max(0, x - 1), min(x + 2, 8)):
        for j in range(max(0, y - 1), min(y + 2, 8)):
            if board[i][j].player != None:
                neighbours.append([i, j])
    return neighbours


def filled_cell_heuristic(board, player):
    sum = 0
    for x in range(WIDTH):
        for y in range(HEIGHT):
            neighbors = find_neighbors(board, x, y)
            for n in neighbors:
                if board[n[0]][n[1]].player == None:
                    sum -= 2
                elif board[n[0]][n[1]].player == player:
                    sum += 2
                else:
                    sum += 1
    return sum / 128


def legal_moves_heuristic(board, player):

    legal_moves = CREATE_BOARD_TYPE.static_legal_moves(board, player)
    opponent_player = Player.PLAYER_1
    if player == Player.PLAYER_1:
        opponent_player = Player.PLAYER_2
    opponent_legal_moves = CREATE_BOARD_TYPE.static_legal_moves(board, opponent_player)
    return (len(legal_moves) - len(opponent_legal_moves)) / 64


def row_leftEmpty_rightOpponent(board, player, opponent, x, y):
    curr_x = x
    # Left empty
    while curr_x >= 0 and (board[curr_x][y].player == player or board[curr_x][y].player == opponent):
        curr_x -= 1
    if curr_x == -1:
        return False
    curr_x = x
    # right opponent
    while curr_x <= 7 and board[curr_x][y].player == player:
        curr_x += 1
    if curr_x == 8:
        return False
    if board[curr_x][y].player == opponent:
        return True
    return False


def row_leftopponent_rightEmpty(board, player, opponent, x, y):
    curr_x = x
    # left opponent
    while curr_x >= 0 and board[curr_x][y].player == player:
        curr_x -= 1
    if curr_x == -1:
        return False
    if board[curr_x][y].player != opponent:
        return False
    curr_x = x
    # right empty
    while curr_x <= 7 and (board[curr_x][y].player == player or board[curr_x][y].player == opponent):
        curr_x += 1
    if curr_x == 8:
        return False
    return True


def col_upEmpty_downOpponent(board, player, opponent, x, y):
    curr_y = y
    # up empty
    while curr_y >= 0 and (board[x][curr_y].player == player or board[x][curr_y].player == opponent):
        curr_y -= 1
    if curr_y == -1:
        return False
    curr_y = y
    # down opponent
    while curr_y <= 7 and board[x][curr_y].player == player:
        curr_y += 1
    if curr_y == 8:
        return False
    if board[x][curr_y].player == opponent:
        return True
    return False


def col_upOpponent_downEmpty(board, player, opponent, x, y):
    curr_y = y
    # left opponent
    while curr_y >= 0 and board[x][curr_y].player == player:
        curr_y -= 1
    if curr_y == -1:
        return False
    if board[x][curr_y].player != opponent:
        return False
    curr_y = y
    # right empty
    while curr_y <= 7 and (board[x][curr_y].player == player or board[x][curr_y].player == opponent):
        curr_y += 1
    if curr_y == 8:
        return False
    return True


def vulnerable_heuristic(board, player):
    score = 0
    opponent_player = Player.PLAYER_1
    if player == Player.PLAYER_1:
        opponent_player = Player.PLAYER_2
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if board[x][y].player == player:
                if (row_leftEmpty_rightOpponent(board, player, opponent_player, x, y) or
                        row_leftopponent_rightEmpty(board, player, opponent_player, x, y) or
                        col_upEmpty_downOpponent(board, player, opponent_player, x, y) or
                        col_upOpponent_downEmpty(board, player, opponent_player, x, y)):
                    score -= 2
            elif board[x][y].player == opponent_player:
                if (row_leftEmpty_rightOpponent(board, opponent_player, player, x, y) or
                        row_leftopponent_rightEmpty(board, opponent_player, player, x, y) or
                        col_upEmpty_downOpponent(board, opponent_player, player, x, y) or
                        col_upOpponent_downEmpty(board, opponent_player, player, x, y)):
                    score += 1
    return score / 128


def weight_place_heuristic(board, player):
    score = 0
    near_corner = 1
    corner = 30000
    frame = 10000
    regular = 1000
    center = 3000

    sum1 = (score + near_corner + corner + frame + regular + center) * 64


    for x in range(WIDTH):
        for y in range(HEIGHT):
            to_add = 0
            # corner cell
            if (x == 0 and y == 0) or (x == 0 and y == 7) or (x == 7 and y == 0) or (x == 7 and y == 7):
                to_add += corner
            # adjust to the left up corner
            elif (x == 0 and y == 1) or (x == 1 and y == 1) or (x == 1 and y == 0):
                to_add += near_corner
            # adjust to the right up corner
            elif (x == 0 and y == 6) or (x == 1 and y == 6) or (x == 1 and y == 7):
                to_add += near_corner
            # adjust to the left down corner
            elif (x == 6 and y == 0) or (x == 6 and y == 1) or (x == 7 and y == 1):
                to_add += near_corner
            # adjust to the right down corner
            elif (x == 7 and y == 6) or (x == 6 and y == 6) or (x == 6 and y == 7):
                to_add += near_corner
            # frame cell
            elif (x == 0 and 2 <= y <= 5) or (x == 7 and 2 <= y <= 5) or (2 <= x <= 5 and y == 0) or (
                    2 <= x <= 5 and y == 7):
                to_add += frame
            # center cell
            elif (x == 3 and y == 3) or (x == 3 and y == 4) or (x == 4 and y == 3) or (x == 4 and y == 4):
                to_add += center
            else:
                to_add += regular
            if board[x][y].player is not None and board[x][y].player.name == player.name:
                score += to_add
            elif board[x][y].player is None:
                continue
            else:
                score -= to_add
    return score / sum1

def weight_combined_heuristic(board, player):
    heuristics = [base_heuristic, difference_heuristic, filled_cell_heuristic, legal_moves_heuristic, vulnerable_heuristic, weight_place_heuristic]
    weights = [0.0025, 0.0025, 0.0025, 0.0025, 0.01, 0.98]
    # return heuristics[5](board, player)
    score = 0
    for i in range(len(heuristics)):
        s = heuristics[i](board, player)
        score += s * weights[i]
    return score


def plot_loss(losses):
    # to_plot = [l.history['loss'] for l in losses]
    # plt.plot(to_plot)
    # plt.title("losses")
    # plt.xlabel("Epochs")
    # plt.ylabel("Loss")
    # plt.show()
    new_losses = []
    for loss_history in losses:
        new_losses += loss_history.history['loss']
    plt.plot(new_losses)
    plt.show()

def switch_board_players(board):
    opposite_board = deepcopy(board)
    for i in range(WIDTH):
        for j in range(HEIGHT):
            if board[i][j].player == Player.PLAYER_1:
                opposite_board[i][j].player = Player.PLAYER_2
            elif board[i][j].player == Player.PLAYER_2:
                opposite_board[i][j].player = Player.PLAYER_1
    return opposite_board


