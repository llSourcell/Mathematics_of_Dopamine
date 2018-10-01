import sys
import time
import numpy as np
if sys.version_info.major == 2:
	import Tkinter as tk
else:
	import tkinter as tk

class Visualiser(tk.Tk, object):
	def __init__(self, height, width, scale, hells, goal, enemy):
		super(Visualiser, self).__init__()
		self.width = (width+1)*scale
		self.height = (height+1)*scale
		self.scale = scale
		self.title('qmaze')
		self.geometry('{0}x{1}'.format(self.width, self.height))

		self.hells = hells
		self.goal = goal
		self.enemy = enemy
		
		self.build_maze()

	def build_maze(self):
		self.canvas = tk.Canvas(self, bg='white',
						   height=self.height*self.scale,
						   width=self.width*self.scale)
		# make grid
		#rows
		for r in range(0, self.width, self.scale):
			x0, y0, x1, y1 = 0, r, self.width, r
			self.canvas.create_line(x0, y0, x1, y1)
		# columns
		for c in range(0, self.height, self.scale):
			x0, y0, x1, y1 = c, 0, c, self.height
			self.canvas.create_line(x0, y0, x1, y1)

		#hells 
		for h in self.hells:
			self.canvas.create_rectangle(
			h[0]*self.scale, h[1]*self.scale,
			h[0]*self.scale + self.scale, h[1]*self.scale + self.scale,
			fill='black')

		#goal
		self.canvas.create_oval(
			self.goal[0]*self.scale, self.goal[1]*self.scale,
			self.goal[0]*self.scale + self.scale, self.goal[1]*self.scale + self.scale,
			fill='yellow')

		#actor
		self.actor_ref = self.canvas.create_rectangle(
			0, 0,
			self.scale, self.scale,
			fill='green')

		# enemy
		self.enemy_ref = self.enemy = self.canvas.create_rectangle(
			self.enemy[0]*self.scale, self.enemy[1]*self.scale,
			self.enemy[0]*self.scale + self.scale, self.enemy[1]*self.scale + self.scale,
			fill='red')
		self.canvas.pack()

	def update_canvas(self, actor, enemy):
		time.sleep(0.2)
		self.canvas.delete(self.actor_ref)
		self.canvas.delete(self.enemy_ref)
		self.actor_ref = self.canvas.create_rectangle(
			actor[0]*self.scale, actor[1]*self.scale,
			actor[0]*self.scale+self.scale, actor[1]*self.scale+self.scale,
			fill='green')
		self.enemy_ref = self.canvas.create_rectangle(
			enemy[0]*self.scale, enemy[1]*self.scale,
			enemy[0]*self.scale+self.scale, enemy[1]*self.scale+self.scale,
			fill='red')
		self.update()
		
