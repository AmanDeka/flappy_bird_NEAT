import pygame as pg
import numpy as np
import neat
import os
class bird:
	def __init__(self,x,y,img,s):
		self.x = x
		self.y = y
		self.img = pg.image.load(img)
		self.img = pg.transform.scale(self.img,(60,60))
		self.vel = 0
		self.hitbox = pg.Rect(x+15,y+20,30,20)
		self.scr = s
		self.score = 0
		self.allow = True
	def show(self):
		self.scr.blit(self.img,(self.x,self.y))
	def apply_gravity(self):
		self.vel += 0.009
	def update(self):
		self.y += self.vel 
		self.hitbox.y = self.y+20
	def jump(self):
		self.vel = -0.99