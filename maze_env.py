import numpy as np
from random import randint

WIDTH = 4
HEIGHT = 4
SCALE = 1

class Maze(object):

	def __init__(self):
		self.actions = ['u', 'r', 'd', 'l']
		self.n_actions = len(self.actions)
		self.hell_blocks = np.array([np.array([2,2]),np.array([3,2]),np.array([1,3])])
		self.goal = np.array([2,3])
		self.actor = np.array([0,0])
		self.enemy = np.array([2,4])
		self.win_count = 0

	def reset(self):
		self.actor = np.array([0,0])
		self.enemy = np.array([2,4])
		return np.append(self.actor, self.enemy)

	def step(self, action):
		s = self.actor
		enemy_s = self.enemy
		base_action = self.action_outcome(action, s)
		enemy_action = self.action_outcome(randint(0,3), enemy_s)
		self.actor = self.actor + base_action
		self.enemy = self.enemy + enemy_action
		reward, done = self.reward()
		return np.append(self.actor, self.enemy), reward, done

	def action_outcome(self, action, s):
		base_action = np.array([0,0])
		if action == 0: #up
			if s[1] > 0:
				base_action[1] -= SCALE
		elif action == 1: #right
			if s[0] < WIDTH:
				base_action[0] += SCALE
		elif action == 2: #down
			if s[1] < HEIGHT:
				base_action[1] += SCALE
		elif action == 3: #left
			if s[0] > 0:
				base_action[0] -= SCALE
		return base_action

	def reward(self):
		if(np.array_equal(self.actor, self.goal)):
			r = 1
			done = True
			self.win_count += 1
		elif np.array_equal(self.actor, self.enemy):
			r = -1
			done = True
		elif(self.actor_is_in_hell(self.actor)):
			r = -1
			done = True
		else:
			r = 0
			done = False
		return r, done

	def actor_is_in_hell(self, state):
		for i in range(len(self.hell_blocks)):
			if(state[0] == self.hell_blocks[i][0] and state[1] == self.hell_blocks[i][1]):
				return True
		return False

	def get_info(self):
		return "actor pos: " + str(self.actor) + " enemy pos: " + str(self.enemy)

	def display_env(self):
		output = ""
		for col in range(WIDTH+1):
			for row in range(HEIGHT+1):
				if(row == self.actor[0] and col == self.actor[1]):
					output += "X "
				elif(row == self.enemy[0] and col == self.enemy[1]):
					output += "E "
				elif(self.actor_is_in_hell(np.array([row,col]))):
					output += "H "
				elif(row == self.goal[0] and col == self.goal[1]):
					output += "G "
				
				else:
					output += "O "
			output += "\n"
		return output

# if __name__ == '__main__':
# 	env = Maze()
# 	print(env.get_info())
# 	print(env.display_env())
# 	# print(env.get_info())
# 	print(env.display_env())







