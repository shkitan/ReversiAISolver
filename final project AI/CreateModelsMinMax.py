from DeepQlearnerAgent import *
from Utils import *
from HeuristicPlayer import *

def player1_minmax_player2_random_Combined():
    player0 = MinMaxAgent(None, weight_combined_heuristic, DEPTH, 0)
    player1 = RandomAgent(None, None, None, 1)
    model = DeepQLearnerAgent(None, weight_combined_heuristic, None, None)
    losses = model.train(player0, player1, NUM_OF_GAMES, "player0_minmax_player1_random_Combined")
    plot_loss(losses)


def player1_minmax_player2_random_weight():
    player0 = MinMaxAgent(None, weight_place_heuristic, DEPTH, 0)
    player1 = RandomAgent(None, None, None, 1)
    model = DeepQLearnerAgent(None, weight_place_heuristic, None, None)
    losses = model.train(player0, player1, NUM_OF_GAMES, "player0_minmax_player1_random_weight")
    plot_loss(losses)


def player1_minmax_player2_minmax_Combined():
    player0 = MinMaxAgent(None, weight_combined_heuristic, DEPTH, 0)
    player1 = MinMaxAgent(None, weight_combined_heuristic, None, 1)
    model = DeepQLearnerAgent(None, weight_combined_heuristic, None, None)
    losses = model.train(player0, player1, NUM_OF_GAMES, "player0_minmax_player1_minmax_Combined")
    plot_loss(losses)


def player1_minmax_player2_minmax_weight():
    player0 = MinMaxAgent(None, weight_place_heuristic, DEPTH, 0)
    player1 = MinMaxAgent(None, weight_place_heuristic, None, 1)
    model = DeepQLearnerAgent(None, weight_place_heuristic, None, None)
    losses = model.train(player0, player1, NUM_OF_GAMES, "player0_minmax_player1_minmax_weight")
    plot_loss(losses)


def player1_minmax_player2_heuristic_Combined():
    player0 = MinMaxAgent(None, weight_combined_heuristic, DEPTH, 0)
    player1 = HeuristicPlayer(None, weight_combined_heuristic, None, 1)
    model = DeepQLearnerAgent(None, weight_combined_heuristic, None, None)
    losses = model.train(player0, player1, NUM_OF_GAMES, "player0_minmax_player1_heuristic_Combined")
    plot_loss(losses)


def player1_minmax_player2_heuristic_weight():
    player0 = MinMaxAgent(None, weight_place_heuristic, DEPTH, 0)
    player1 = HeuristicPlayer(None, weight_place_heuristic, None, 1)
    model = DeepQLearnerAgent(None, weight_place_heuristic, None, None)
    losses = model.train(player0, player1, NUM_OF_GAMES, "player0_minmax_player1_heuristic_weight")
    plot_loss(losses)


if __name__ == '__main__':
    player1_minmax_player2_random_Combined()
    # player1_minmax_player2_random_weight()
    # player1_minmax_player2_minmax_Combined()
    # player1_minmax_player2_minmax_weight()
    # player1_minmax_player2_heuristic_Combined()
    # player1_minmax_player2_heuristic_weight()
