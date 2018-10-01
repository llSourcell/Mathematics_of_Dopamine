import argparse
from maze_env import Maze
from visualiser import Visualiser
from rl_brain import QLearn
import time

VIS = False
N_EPISODES = 5000
def test(vis_):
	start_time = time.time()
	for episode in range(N_EPISODES):
		# initial observation
		observation = env.reset()
		if(episode % 500 == 0):
			print(str(float(episode) / N_EPISODES * 100) + "%")
		while True:
			if(vis_):
				vis.update_canvas(env.actor, env.enemy)
			# RL choose action based on observation
			action = RL.choose_action(str(observation))

			# RL take action and get next observation and reward
			observation_, reward, done = env.step(action)

			# RL learn from this transition
			RL.learn(str(observation), action, reward, str(observation_), done)

			# swap observation
			observation = observation_

			# break while loop when end of this episode
			if done:
				break
	# end of game
	print "My program took", time.time() - start_time, "to run"
	print('game over')
	RL.save_Qtable()

def run_optimal():
	RL.load_Qtable()
	for episode in range(20):
		observation = env.reset()
		vis.update_canvas(env.actor, env.enemy)
		while(True):
			action = RL.choose_action(str(observation))
			observation_, reward, done = env.step(action)
			observation = observation_
			vis.update_canvas(env.actor, env.enemy)
			if done:
				break
	print("Games won: " + str(env.win_count))
	vis.destroy()

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='QMaze options')
	parser.add_argument('--test', dest='test', action='store_true',
                   help='if you wish to re-train')
	parser.add_argument('--vis', dest='vis', action='store_true',
                   help='if you wish to see the GUI')
	args = parser.parse_args()
	print(args)
	if(args.test):
		env = Maze()
		RL = QLearn(actions=list(range(env.n_actions)))
		if(args.vis):
			vis = Visualiser(4,4,80, env.hell_blocks, env.goal, env.enemy)
		test(args.vis)
	else:
		env = Maze()
		vis = Visualiser(4,4,80, env.hell_blocks, env.goal, env.enemy)
		RL = QLearn(actions=list(range(env.n_actions)), e_greedy=1.0)
		run_optimal()



