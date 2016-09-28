global TOP=0, RIGHT=1, BOTTOM=2, LEFT=4

class Side():
	def __init__(self, symbol):
		self.face=[[symbol]*3 for i in range (3)]
		self.top=None
		self.right=None
		self.bottom=None
		self.left=None
	
	def connect(self, side, connection):
		if side==TOP:
			self.top=connection
			connection.bottom=self
		elif side==RIGHT:
			self.right=connection
			connecton.left=self
		elif side==BOTTOM:
			self.bottom=connection
			connection.top=self
		elif side==RIGHT:
			self.right=connection
			connection.left=self
		else:
			return

class Cube():

	def __init__(self):
		self.sides=[]

s=Side('g')

print(s.face)