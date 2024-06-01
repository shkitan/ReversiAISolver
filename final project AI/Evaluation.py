from Utils import *
from Reversi import *
from DeepQlearnerAgent import *


def evaluation(agent1, heuristic1, depth1, agent2, heuristic2, depth2):
    agent1_wins = 0
    agent2_wins = 0
    for g in range(NUM_OF_GAMES):
        game = Reversi(agent1, agent2, heuristic1, depth1, heuristic2, depth2)
        final_board = game.run()
        score_agent1 = 0
        score_agent2 = 0
        for i in range(WIDTH):
            for j in range(HEIGHT):
                if final_board[i][j].player == Player.PLAYER_1:
                    score_agent1 += 1
                elif final_board[i][j].player == Player.PLAYER_2:
                    score_agent2 += 1
        if score_agent1 > score_agent2:
            agent1_wins += 1
        elif score_agent2 > score_agent1:
            agent2_wins += 1
        else:
            continue
    if agent1_wins > agent2_wins:
        print("######################################")
        print("The winner is player 0: " + str((agent1_wins / NUM_OF_GAMES)))
        print("######################################")
    elif agent2_wins > agent1_wins:
        print("######################################")
        print("The winner is player 1: " + str((agent2_wins / NUM_OF_GAMES)))
        print("######################################")
    return (agent1_wins / NUM_OF_GAMES), (agent2_wins / NUM_OF_GAMES)

def get_models(player, files):
    models = []
    for i in range(3):
        model = DeepQLearnerAgent(None, weight_combined_heuristic, None, player)
        model.model.load_weights(files[i])
        models.append(model)
    for i in range(3, 6):
        model = DeepQLearnerAgent(None, weight_place_heuristic, None, player)
        model.model.load_weights(files[i])
        models.append(model)
    return models


if __name__ == '__main__':
    files_heuristic = ["player0_heuristic_player1_random_Combined", "player0_heuristic_player1_random_weight", "player0_heuristic_player1_minmax_Combined",
             "player0_heuristic_player1_minmax_weight", "player0_heuristic_player1_heuristic_Combined", "player0_heuristic_player1_heuristic_weight"]
    files_minmax = ["player0_minmax_player1_random_Combined", "player0_minmax_player1_random_weight", "player0_minmax_player1_minmax_Combined",
             "player0_minmax_player1_minmax_weight", "player0_minmax_player1_heuristic_Combined", "player0_minmax_player1_heuristic_weight"]

    # #### pair 1 - MinMax Weight combined heuristic vs MinMax Weight place heuristic ####
    # score1, score2 = evaluation("minmax", weight_combined_heuristic, 2, "minmax", weight_place_heuristic, 2)
    #
    # #### pair 2 - MinMax Weight combined heuristic vs random ####
    # score1, score2 = evaluation("minmax", weight_combined_heuristic, 2, "random", None, None)
    #
    # #### pair 3 - MinMax Weight combined heuristic vs Heuristic ####
    # score1, score2 = evaluation("minmax", weight_combined_heuristic, 2, "heuristic", weight_combined_heuristic, None)
    #
    # ### pair 4 - MinMax Weight combined heuristic vs modelMinMax ####
    # models = get_models(1, files_minmax)
    # score1, score2 = evaluation("minmax", weight_combined_heuristic, 2, "modelMinMax", models, None)
    #
    # #### pair 5 - MinMax Weight combined heuristic vs modelHeuristic ####
    # models = get_models(1, files_heuristic)
    # score1, score2 = evaluation("minmax", weight_combined_heuristic, 2, "modelHeuristic", models, None)
    #
    # #### pair 6 - MinMax Weight place heuristic vs random ####
    # score1, score2 = evaluation("minmax", weight_combined_heuristic, 2, "random", None, None)
    #
    # #### pair 7 - MinMax Weight place heuristic vs Heuristic ####
    # score1, score2 = evaluation("minmax", weight_combined_heuristic, 2, "heuristic", weight_combined_heuristic, None)
    #
    # #### pair 8 - MinMax Weight place heuristic vs Model MinMax ####
    # models = get_models(1, files_minmax)
    # score1, score2 = evaluation("minmax", weight_combined_heuristic, 2, "modelMinMax", models, None)
    #
    # #### pair 9 - MinMax Weight place heuristic vs Model Heuristic ####
    # models = get_models(1, files_heuristic)
    # score1, score2 = evaluation("minmax", weight_combined_heuristic, 2, "modelHeuristic", models, None)
    #
    # #### pair 10 - random vs  Heuristic ####
    # score1, score2 = evaluation("random",None, None, "heuristic", weight_combined_heuristic, None)

    ### pair 11 - random vs  Model MinMax ####
    models = get_models(1, files_minmax)
    score1, score2 = evaluation("random",None, None, "modelMinMax", models, None)

    # ### pair 12 random vs  Model Heuristic ####
    # models = get_models(1, files_heuristic)
    # score1, score2 = evaluation("random",None, None, "modelHeuristic", models, None)
    #
    # ### pair 13 - Heuristic vs  Model MinMax ####
    # models = get_models(1, files_minmax)
    # score1, score2 = evaluation("heuristic",weight_combined_heuristic, None, "modelMinMax", models, None)
    #
    # ### pair 14 - Heuristic vs  Model Heuristic ####
    # models = get_models(1, files_heuristic)
    # score1, score2 = evaluation("heuristic",weight_combined_heuristic, None, "modelHeuristic", models, None)
    #
    # ### pair 15 - Model MinMax vs  Model Heuristic ####
    # models = get_models(0, files_minmax)
    # models2 = get_models(1, files_heuristic)
    # score1, score2 = evaluation("modelMinMax", models, None, "modelHeuristic", models2, None)















