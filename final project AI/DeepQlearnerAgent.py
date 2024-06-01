import numpy as np

from keras import Sequential, Model
from keras.layers import Dense, Embedding, Reshape, Activation, Conv2D, BatchNormalization, Flatten, Dropout, Input
from tensorflow.keras.optimizers import Adam
from tensorflow import keras

from Agent import Agent
from CreateBoard import *
from MinMaxAgent import MinMaxAgent
from Utils import *

import random

from RandomAgent import RandomAgent

OFFSET = 10



class DeepQLearnerAgent(Agent):

    def __init__(self, board, heuristic, depth, current_player):
        # TODO: check values of parameters
        super().__init__(board, heuristic, depth, current_player)
        self.epsilon = 0.3
        self.decay_epsilon = 0.995
        self.learning_rate = 0.000025
        self.gamma = 0.3
        self.model = None
        self.current_player = current_player
        self.build_model()

    def build_model(self):
        main_input = Input((1,8,8))
        flattened = Flatten(name='flatten')(main_input)
        dense = Dense(256, name='dense1')(flattened)
        d1 = Dense(128, activation='relu6', name='dense2')(dense)
        d3 = Dense(64, activation='linear', name='dense4')(d1)
        d4 = Dense(32, activation='linear', name='dense5')(d3)
        d5 = Dense(16, activation='linear', name='dense6')(d4)
        d2 = Dense(1, name='dense3')(d5)

        self.model = keras.models.Model(inputs=main_input, outputs=d2)

        self.model.compile(loss='mse', optimizer=Adam(learning_rate=self.learning_rate))
    # self.input_boards = Input(shape=(WIDTH, HEIGHT))
        # x_image = Reshape((WIDTH, HEIGHT, 1))(self.input_boards)  # batch_size  x board_x x board_y x 1
        # h_conv1 = Activation('relu')(BatchNormalization(axis=3)(
        #     Conv2D(15, 3, padding='same', use_bias=False)(
        #         x_image)))  # batch_size  x board_x x board_y x num_channels
        # h_conv2 = Activation('relu')(BatchNormalization(axis=3)(
        #     Conv2D(15, 3, padding='same', use_bias=False)(
        #         h_conv1)))  # batch_size  x board_x x board_y x num_channels
        # h_conv3 = Activation('relu')(BatchNormalization(axis=3)(
        #     Conv2D(15, 3, padding='valid', use_bias=False)(
        #         h_conv2)))  # batch_size  x (board_x-2) x (board_y-2) x num_channels
        # h_conv4 = Activation('relu')(BatchNormalization(axis=3)(
        #     Conv2D(15, 3, padding='valid', use_bias=False)(
        #         h_conv3)))  # batch_size  x (board_x-4) x (board_y-4) x num_channels
        # h_conv4_flat = Flatten()(h_conv4)
        # s_fc1 = Dropout(0.5)(Activation('relu')(
        #     BatchNormalization(axis=1)(Dense(1024, use_bias=False)(h_conv4_flat))))  # batch_size x 1024
        # s_fc2 = Dropout(0.5)(
        #     Activation('relu')(BatchNormalization(axis=1)(Dense(512, use_bias=False)(s_fc1))))  # batch_size x 1024
        # self.pi = Dense(65, activation='softmax', name='pi')(s_fc2)  # batch_size x self.action_size
        # self.v = Dense(1, activation='tanh', name='v')(s_fc2)  # batch_size x 1
        #
        # self.model = Model(inputs=self.input_boards, outputs=[self.pi, self.v])
        # self.model.compile(Adam(self.learning_rate), "mse")

    def calculate_q_value(self, board, player):
        to_binary = np.zeros((8, 8))
        for i in range(WIDTH):
            for j in range(HEIGHT):
                if board[i][j].player == Player.PLAYER_2:
                    to_binary[i][j] = 2.0
                elif board[i][j].player == Player.PLAYER_1:
                    to_binary[i][j] = 1.0
        # to_binary = np.array([to_binary]).astype(np.float)
        to_binary = np.array([to_binary])
        q_max = self.model.predict(np.array([to_binary]))
        q_func = self.heuristic(board, player) + self.gamma * q_max
        return q_func, to_binary



    def train(self, agent1, agent2, numGames, path):
        losses = []
        player_agent_dict = {Player.PLAYER_1.name: agent1, Player.PLAYER_2.name: agent2}
        for i in range(numGames):
            q_score = []
            boards = []
            curr_board = CREATE_BOARD_TYPE()
            curr_board.screen_update()
            while True:
                if curr_board.won:
                    break
                rand_float = np.random.rand()
                player_agent_dict[curr_board.player.name].board = curr_board
                if rand_float >= self.epsilon:

                    act, _ = player_agent_dict[curr_board.player.name].do_action()
                else:

                    act, _ = RandomAgent(curr_board, None, None, None).do_action()
                if act is not None:
                    x, y = act.loc
                    curr_board.move(x, y)
                    if curr_board.player == Player.PLAYER_1:
                        q_func, to_binary = self.calculate_q_value(curr_board.board, curr_board.player)
                        q_score.append(q_func)
                        boards.append(to_binary)
                else:
                    break
            q_score2 = np.array(q_score)
            boards2 = np.array(boards)
            loss = self.model.fit(boards2, q_score2, epochs = EPOCHS)
            losses.append(loss)
            self.epsilon = self.epsilon * self.decay_epsilon
        self.model.save_weights(path)
        return losses

# player0 = RandomAgent(None, None, None, 0)
# player1 = RandomAgent(None, None, None, 1)
# d = DeepQLearnerAgent(None, weight_place_heuristic, None, 0)
# d.train(player0, player1, 1, "player0_minmax_player1_random")
