![q-learning td error](https://raw.githubusercontent.com/PierpaoloLucarelli/QLearningMaze/master/qlearn2.gif)

Goal: Reaching the yellow oval while avoiding black blocks and moving enemy (red block)

# QLearningMaze

Implementation of Q-Learning usind TD error for optimally navigating a maze while avoiding a moving enemy.

# To run:
```sh
$ pip install numpy pandas
$ python main.py
```
Project comes with trained Qtable in pickled file **action** 
You may run in the following ways
### Importing Q-table and running optimal policy
```sh
$ python main.py
```
### Training 
```sh
$ python main.py --test
```
### Training + GUI
(slow, mostly for debugging)
```sh
$ python main.py --test --vis
```
### Algorithm used
Q-values are updated based on the following formula:
![q-learning td error](http://i.imgur.com/ZtDdzFm.png)

## pseudo formula

newVal = oldVal + learningRate * (reward + discount_val * maxValOfNextState - oldVal)
