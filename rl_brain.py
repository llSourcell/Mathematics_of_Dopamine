import numpy as np
import pandas as pd
import cPickle as pickle

class QLearn:
	def __init__(self, actions, learning_rate=0.01, reward_decay=0.9, e_greedy=0.9):
		self.actions = actions  # a list
		self.lr = learning_rate
		self.gamma = reward_decay
		self.epsilon = e_greedy
		self.q_table = pd.DataFrame(columns=self.actions, dtype=np.float64)

	# chose the next action to take based on the observation (position of actor)
	def choose_action(self, observation):
		self.check_state_exist(observation)
		# print(self.q_table)
		# based on epsilon, chose either the best action or a random action (eploration vs exploitation)
		if np.random.uniform() < self.epsilon:
			# chose best action epsilon % of the time
			# based on the 4 coordinates of the actor
			state_action = self.q_table.ix[observation, :]
			# this returns a labbelled array where label is action and val is Qval of the action
			state_action = state_action.reindex(np.random.permutation(state_action.index)) # make sure to not pick always the first value
			# pick action with max Qval
			action = state_action.idxmax()
		else:
			#pick a random val
			action = np.random.choice(self.actions)
		return action

	def learn(self, s, a, r, s_, done):
		self.check_state_exist(s_)
		# get the Q value of the action a at state s
		q_predict = self.q_table.ix[s, a]
		
		if done == False:
			q_target = r + self.gamma * self.q_table.ix[s_, :].max()  # next state is not terminal
		else:
			q_target = r  # next state is terminal
		self.q_table.ix[s, a] += self.lr * (q_target - q_predict)

	def check_state_exist(self, state):
		if state not in self.q_table.index:
			# append new state to q table
			self.q_table = self.q_table.append(
				pd.Series(
					[0]*len(self.actions),
					index=self.q_table.columns,
					name=state,
				)
			)
	def save_Qtable(self):
		self.q_table.to_pickle("actions")

	def load_Qtable(self):
		self.q_table = pd.read_pickle("actions")