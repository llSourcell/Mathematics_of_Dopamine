## Overview


This is the code for [this](https://youtu.be/-vhYoS3751g) video on Youtube by Siraj Raval on the Mathematics of Dopamine. Credit for the q learning + TD Error code go to [pierpaolo](https://github.com/PierpaoloLucarelli/QLearningMaze). The other 2 scripts i hacked together myself. Enjoy!


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
<a href="http://www.codecogs.com/eqnedit.php?latex=Q(s,a)\leftarrow&space;Q(s,a)&plus;\alpha\[r&space;&plus;&space;\gamma&space;\max_{a'}&space;Q(s',a')-Q(s,a)&space;\]" target="_blank"><img src="http://latex.codecogs.com/gif.latex?Q(s,a)\leftarrow&space;Q(s,a)&plus;\alpha\[r&space;&plus;&space;\gamma&space;\max_{a'}&space;Q(s',a')-Q(s,a)&space;\]" title="Q(s,a)\leftarrow Q(s,a)+\alpha\[r + \gamma \max_{a'} Q(s',a')-Q(s,a) \]" /></a>

## pseudo formula

newVal = oldVal + learningRate * (reward + discount_val * maxValOfNextState - oldVal)
