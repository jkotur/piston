import sys

import math as m
import numpy as np
import transformations as tr

import random as rand

from OpenGL.GL import *
from OpenGL.GLU import *

from drawable import Drawable

class Piston( Drawable ) :
	def __init__( self ) :
		self.l1 = 1.0
		self.l2 = 2.0

		self.w = 0.0

		self.mu = 0.0
		self.sg = 0.0

		self.v1 = np.array((1,0),np.float32)
		self.v2 = np.array((self.l2,0),np.float32)

	def set_w( self , w ) :
		self.w = w
	def set_L( self , L ) :
		self.l2 = L
	def set_R( self , R ) :
		self.l1 = R
	def set_eps( self , eps ) :
		self.sg = eps

	def get_p1( self ) : return self.v1
	def get_p2( self ) : return self.v1 * self.l1 + self.v2

	def draw( self ) :
		r = self.v1 * self.l1
		v = r + self.v2
		glColor3f(1,1,1)
		glBegin(GL_LINE_STRIP)
		glVertex3f( 0 , 0 , 0 )
		glVertex3f( r[0] , r[1] , 0 )
		glVertex3f( v[0] , v[1] , 0 )
		glEnd()

	def step( self , dt ) :
		rot = tr.rotation_matrix( dt * self.w , (0,0,1) )

		self.v1 = np.resize( np.dot( rot , np.resize( self.v1 , 4 ) ) , 2 )
		R = self.v1 * self.l1
		self.v2[1] = -R[1]
		L = self.l2 + rand.normalvariate(self.mu,self.sg) 
		self.v2[0] = m.sqrt(L**2-self.v2[1]**2)

