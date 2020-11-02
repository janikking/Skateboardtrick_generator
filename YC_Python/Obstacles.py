from abc import ABC, abstractmethod
from Able import Grindable, Slidable, Gapable, Manualable
from Obstacle import Obstacle as Obstacle
import math
import Saved

class Box(Slidable, Grindable, Obstacle):

	name = "Box"
	tricktypes = ["slidetrick", "grindtrick"]
	def __init__(self, height, width, length):
		super().__init__(self.name)
		self.height = height
		self.width = width
		self.length = length


	def grind(self):
		self.grind()

	def slide(self):
		self.slide()

	def getName(self):
		return self.name

class Manualpad(Manualable, Obstacle):

	name = "Manualpad"
	tricktypes = ["manualtrick"]

	def __init__(self, height, width, length):
		super().__init__(self.name)
		self.height = height
		self.width = width
		self.length = length

	def manual(self):
		self.manual()

	def getName(self):
		return self.name

class Kicker(Gapable, Obstacle):

	name = "Kicker"
	tricktypes = ["gaptrick"]
	def __init__(self, height, length):
		super().__init__(self.name)
		self.height = height
		self.length = length
		self.angle = math.tan(height/length)

	def gap(self):
		self.gap()

class Rail(Slidable, Grindable, Obstacle):

	name = "Rail"
	tricktypes = ["slidetrick", "grindtrick"]
	def __init__(self, height, length):
		super().__init__(self.name)
		self.height = height
		self.length = length

class Flatground(Gapable, Manualable, Obstacle):

	name = "Flatground"
	tricktypes = ["gaptrick", "manualtrick"]
	def __init__(self):
		super().__init__(self.name)

	def getName(self):
		return self.name
