TOP=0
RIGHT=1
BOTTOM=2
LEFT=3

class Side():
	def __init__(self, symbol):
		self.face=[[symbol]*3 for i in range (3)]
		connections=[]
		# self.top=None
		# self.right=None
		# self.bottom=None
		# self.left=None
	def connect(self, conn):
		self.connections.append(conn)

	def connect(self, side, connection):
		if side==TOP:
			self.top=connection
			# connection.bottom=self
		elif side==RIGHT:
			self.right=connection
			# connecton.left=self
		elif side==BOTTOM:
			self.bottom=connection
			# connection.top=self
		elif side==RIGHT:
			self.right=connection
			# connection.left=self
		else:
			return

class Cube():

	def __init__(self):
		self.top=Side('g')
		self.down=Side('w')
		self.front=Side('r')
		self.right=Side('o')
		self.back=Side('b')
		self.left=Side('y')
		self.sides=[self.top, self.down, self.front, self.right, self.back, self.left]
		# self.sides=[Side('g'), Side('w'), Side('r'),Side('o'),Side('b'), Side('y')]
		# self.sides[0].connect(self.sides[])
		self.top.connections=[self.front, self.right, self.back, self.left]
		self.down.connections=[self.front, self.left, self.back, self.right]
		self.front.connections=[self.right, self.top, self.left, self.down]
		


	# def turnFace(self, )
s=Side('g')
c=Cube()
for i in c.sides:

	print(i.face)