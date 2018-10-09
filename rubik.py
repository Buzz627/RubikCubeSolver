from termcolor import colored
class Side():
	def __init__(self, symbol, size=3):
		self.face=[[symbol]*size for i in range (size)]
		self.size=size
		connections=[]
	

	def connect(self, conn):
		self.connections.append(conn)

	def connect(self, side, connection):
		if side==TOP:
			self.top=connection
			
		elif side==RIGHT:
			self.right=connection
			
		elif side==BOTTOM:
			self.bottom=connection
			
		elif side==RIGHT:
			self.right=connection
			
		else:
			return
	def setTopRow(self, lst):
		self.face[0]=lst

	def setBottomRow(self, lst):
		self.face[self.size-1]=lst

	def setLeftCol(self, lst):
		for i in range(len(lst)):
			self.face[i][0]=lst[i]

	def setRightCol(self, lst):
		for i in range(len(lst)):
			self.face[i][self.size-1]=lst[i]

	def getTopRow(self):
		return self.face[0]

	def getBottomRow(self):
		return self.face[self.size-1]

	def getLeftCol(self):
		return [self.face[i][0] for i in range(self.size)]
			

	def getRightCol(self):
		return [self.face[i][self.size-1] for i in range(self.size)]

	def printSide(self):
		for i in self.face:
			print i
		print ""


class Cube():

	def __init__(self, size=3):

	# 	self.top=Side('g')
	# 	self.down=Side('w')
	# 	self.front=Side('r')
	# 	self.right=Side('o')
	# 	self.back=Side('b')
	# 	self.left=Side('y')
	# 	self.sides=[self.top, self.down, self.front, self.right, self.back, self.left]
		self.sides={"t":Side('g'), "d":Side('w'), "f":Side('r'),"r":Side('o'),"b":Side('b'), "l":Side('y')}
	# 	# self.sides[0].connect(self.sides[])
	# 	self.top.connections=[self.front, self.right, self.back, self.left]
	# 	self.down.connections=[self.front, self.left, self.back, self.right]
	# 	self.front.connections=[self.right, self.top, self.left, self.down]
	# 	self.right.connections=
		self.size=size



	def printSide(self, n):

		self.sides[n].printSide()

	def printCube(self):
		for i in self.sides:
			print i+" ="
			self.sides[i].printSide()

	def prettyPrintCube(self):
		colors={"r":"red", "b":"blue","g":"green", "w":"white","y":"yellow","o":"magenta"}
		for i in self.sides["t"].face:
			for j in range(2*(self.size+1)):
				print " ",
			for k in i:
				print colored(k, colors[k]),
			for j in range(2*(self.size+1)):
				print " ",
			print ""
		for j in range(4*(self.size+1)):
			print "-",
		print ""
		for i in range(self.size):
			for j in self.sides["b"].face[i]:
				print colored(j, colors[j]),
			print "|",
			for j in self.sides["l"].face[i]:
				print colored(j, colors[j]),
			print "|",
			for j in self.sides["f"].face[i]:
				print colored(j, colors[j]),
			print "|",
			for j in self.sides["r"].face[i]:
				print colored(j, colors[j]),
			# print "|",
			print ""

		for j in range(4*(self.size+1)):
			print "-",
		print ""
		for i in self.sides["d"].face:
			for j in range(2*(self.size+1)):
				print " ",
			for k in i:
				print colored(k, colors[k]),
			print ""
		print "\n\n"

#
#     t
# b l f r
#     d
#
	def turnSides(self, n):
		if n=="t":
			temp=self.sides["f"].getTopRow()
			self.sides["f"].setTopRow(self.sides["r"].getTopRow())
			self.sides["r"].setTopRow(self.sides["b"].getTopRow())
			self.sides["b"].setTopRow(self.sides["l"].getTopRow())
			self.sides["l"].setTopRow(temp)

		elif n=="d":
			temp=self.sides["f"].getBottomRow()
			self.sides["f"].setBottomRow(self.sides["l"].getBottomRow())
			self.sides["l"].setBottomRow(self.sides["b"].getBottomRow())
			self.sides["b"].setBottomRow(self.sides["r"].getBottomRow())
			self.sides["r"].setBottomRow(temp)


		#need to fix the ordering
		elif n=="f":
			temp=self.sides["t"].getBottomRow()
			self.sides["t"].setBottomRow(self.sides["l"].getRightCol()[::-1])
			self.sides["l"].setRightCol(self.sides["d"].getTopRow())
			self.sides["d"].setTopRow(self.sides["r"].getLeftCol())
			self.sides["r"].setLeftCol(temp[::-1])

		elif n=="l":
			temp=self.sides["t"].getLeftCol()
			self.sides["t"].setLeftCol(self.sides["b"].getRightCol()[::-1])
			self.sides["b"].setRightCol(self.sides["d"].getLeftCol())
			self.sides["d"].setLeftCol(self.sides["f"].getLeftCol())
			self.sides["f"].setLeftCol(temp[::-1])

		elif n=="b":
			temp=self.sides["t"].getTopRow()
			self.sides["t"].setTopRow(self.sides["r"].getRightCol()[::-1])
			self.sides["r"].setRightCol(self.sides["d"].getBottomRow())
			self.sides["d"].setBottomRow(self.sides["l"].getLeftCol()[::-1])
			self.sides["l"].setLeftCol(temp)

		elif n=="r":
			temp=self.sides["t"].getRightCol()
			self.sides["t"].setRightCol(self.sides["f"].getRightCol()[::-1])
			self.sides["f"].setRightCol(self.sides["d"].getRightCol())
			self.sides["d"].setRightCol(self.sides["b"].getLeftCol()[::-1])
			self.sides["b"].setLeftCol(temp)





	def turnFace(self, side):
		mat=self.sides[side]
		temp=mat.getTopRow()
		if side=="b":
			
			mat.setTopRow(mat.getRightCol())
			mat.setRightCol(mat.getBottomRow())
			mat.setBottomRow(mat.getLeftCol())
			mat.setLeftCol(temp)

		else:
			mat.setTopRow(mat.getLeftCol())
			mat.setLeftCol(mat.getBottomRow())
			mat.setBottomRow(mat.getRightCol())
			mat.setRightCol(temp)
		self.sides[side]=mat

		self.turnSides(side)



# s=Side("g")
# s.printSide()
# s.setRightCol(["r"]*3)
# s.setTopRow(["w"]*3)

# print str(s.getLeftCol())+"\n"
# s.printSide()
c=Cube()
c.prettyPrintCube()
c.turnFace("r")
c.turnFace("r")
c.turnFace("l")
c.turnFace("l")
c.turnFace("f")
c.turnFace("f")
c.turnFace("b")
c.turnFace("b")
c.turnFace("t")
c.turnFace("t")
c.turnFace("d")
c.turnFace("d")
c.prettyPrintCube()
# c.printCube()


   #          """    g g g 
   #                 g g g 
   #                 g g g
   #                 ----- 
   # y y y | g g g | o o o | b b b 
   # b b b | y y y | r r r | o o o 
   # b b b | y y y | r r r | o o o 
   #                 -----
   #                 w w w 
   #                 w w w 
   #                 w w w """
