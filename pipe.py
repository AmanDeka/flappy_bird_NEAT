import pygame as pg
import numpy as np
import neat
import os
SCR_WIDTH = 1200
SCR_HEIGHT = 600
class pipe:
	GAP = 150
	VEL = -0.3
	def __init__(self,x,h,s):
		self.x = x
		self.height = h
		self.image = pg.image.load('pillar.png')
		self.hitbox1 = pg.Rect(x,SCR_HEIGHT-h,50,h)
		self.hitbox2 = pg.Rect(x,0,50,SCR_HEIGHT-(self.height+self.GAP))
		self.scr = s
	def show(self):
		img = pg.transform.scale(self.image,(50,self.height))
		self.scr.blit(img,(self.x,SCR_HEIGHT-self.height))
		img = pg.transform.flip(self.image,False,True)
		height = SCR_HEIGHT-(self.height+self.GAP)
		img = pg.transform.scale(img,(50,height))
		self.scr.blit(img,(self.x,0))
	def update(self):
		self.x += self.VEL
		self.hitbox1.x = self.x
		self.hitbox2.x = self.x