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
		self.l1 = 1
		self.l2 = 2

		self.v1 = np.array((self.l1,0),np.float32)
		self.v2 = np.array((self.l2,0),np.float32)

	def get_p1( self ) : return self.v1
	def get_p2( self ) : return self.v1 + self.v2

	def draw( self ) :
		v = self.v1 + self.v2
		glColor3f(1,1,1)
		glBegin(GL_LINE_STRIP)
		glVertex3f( 0 , 0 , 0 )
		glVertex3f( self.v1[0] , self.v1[1] , 0 )
		glVertex3f( v[0] , v[1] , 0 )
		glEnd()

	def step( self , dt ) :
		mu = 0
		sg = 0.000005
		rot = tr.rotation_matrix( dt , (0,0,1) )

		self.v1 = np.resize( np.dot( rot , np.resize( self.v1 , 4 ) ) , 2 )
		self.v2[1] = -self.v1[1]
		L = self.l2 + rand.normalvariate(mu,sg) 
		self.v2[0] = m.sqrt(L**2-self.v2[1]**2)

