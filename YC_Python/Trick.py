from Obstacle import Obstacle, Into
from Obstacles import Box, Manualpad, Rail, Flatground, Kicker

class FlatTrick:

	def __init__(self, name, yr, xr, br):
		self.name = name
		self.yr = yr
		self.xr = xr
		self.br = br
		self.type = "gaptrick"

	def __str__(self):
		return self.name

	def getname(self):
		return self.name


	def trickDescription(self):
		if(self.yr < 0): self.flips = " to the left"
		elif(self.yr > 0): self.flips = " to the right"
		else: self.flips = ""

		if(self.xr < 0): self.rotates = " frontside"
		elif(self.xr > 0): self.rotates = " backside"
		else: self.rotates = ""

		if(self.br > 0): self.body = "backside"
		elif(self.br < 0): self.body = "frontside"

		string = "Your board flips %s time(s)%s and rotates %s degrees%s. " %(abs(self.yr), self.flips, (abs(self.xr) * 180), self.rotates)
		if(self.br != 0):
			s = "Your body also rotates %s degrees %s." %(abs(self.br) * 180, self.body)
			string = string + s
		return string


class GrindTrick(Into):

	def __init__(self, name):
		self.name = name
		self.type = "grindtrick"

	def getname(self):
		return self.name

	def __str__(self):
		return self.name

	def grind(self, Obstacle):
		print("You do a %s on %s" % (self.name, Obstacle.getName()))

class SlideTrick(Into):

	def __init__(self, name):
		self.name = name
		self.type = "slidetrick"

	def getname(self):
		return self.name

	def __str__(self):
		return self.name

	def slide(self, Obstacle):
		print("You do a %s on %s" % (self.name, Obstacle.getName))

class ManualTrick(Into):

	def __init__(self, name):
		self.name = name
		self.type = "manualtrick"

	def getname(self):
		return self.name

	def __str__(self):
		return self.name

	def manual(self, Obstacle):
		print("You %s on %s" % (self.name, Obstacle.getName))

class CombinationTrick:


	def __init__(self, FlatTrick, Obstacle, Into):
		self.flattrick = FlatTrick
		self.obstacle = Obstacle
		if(Into != None):
			self.trickInto = Into
		else:
			self.trickInto = None


	def doTrick(self):

		if(self.trickInto == None):
			if(isinstance(self.obstacle, Kicker)):
				print("You did %s off a %s!" %(str(self.flattrick), self.obstacle.name))
			elif(isinstance(self.obstacle, Flatground)):
				print("You did %s on %s!" % (str(self.flattrick), self.obstacle.name))
			else:
				print("You did %s off a %s!" % (str(self.flattrick), self.obstacle.name))

		elif(self.trickInto != None):
			print("You did %s into %s on a %s!" % (str(self.flattrick), str(self.trickInto), self.obstacle.name))


	def __str__(self):
		if (self.trickInto == None):
			a = "You did %s on %s!" % (str(self.flattrick), self.obstacle.name)
			return a
		elif (self.trickInto != None):
			a = "You did %s into %s on a %s!" % (str(self.flattrick), str(self.trickInto), self.obstacle.name)
			return a

