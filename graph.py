import sys

import numpy as np

from OpenGL.GL import *
from OpenGL.GLU import *

from drawable import Drawable

class Graph( Drawable ) :
	def __init__( self , f , t , c = (1,1,1) ) :
		if f.shape != t.shape :
			raise ValueError('from and to vectors shape must agree')
		self.f = f
		self.t = t
		self.color = c
		self.dim = f.shape[0]
		self.curr_num = 0
		self.pts = np.zeros( (0,self.dim) , np.float32 )
		self.resize(1)

	def resize( self , num ) :
		self.pts = np.resize( self.pts , (num,self.dim) )
		self.max_num = num

	def add( self , p ) :
		if p.shape[0] != self.dim :
			raise ValueError('Incorect point dimentsion')
		self.curr_num += 1
		if self.curr_num >= self.max_num :
			self.resize( self.max_num * 2 )
		self.pts[self.curr_num] = p

	def draw( self ) :
		glDisable(GL_LIGHTING)
		glMatrixMode(GL_PROJECTION)
		glPushMatrix()
		glLoadIdentity()
		glOrtho( self.f[0] , self.t[0] , self.f[1] , self.t[1] , -1 , 1 )
		glMatrixMode(GL_MODELVIEW)
		glPushMatrix()
		glLoadIdentity()
		glEnableClientState(GL_VERTEX_ARRAY)
		glColor3f(*self.color)
		glVertexPointer( self.dim , GL_FLOAT , 0 , self.pts )
		glDrawArrays( GL_LINE_STRIP , 0 , self.curr_num )
		glDisableClientState(GL_VERTEX_ARRAY)
		glPopMatrix()
		glMatrixMode(GL_PROJECTION)
		glPopMatrix()
		glMatrixMode(GL_MODELVIEW)
		glEnable(GL_LIGHTING)

