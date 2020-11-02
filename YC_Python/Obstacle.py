from abc import ABC, abstractmethod

class Obstacle(ABC):

	name = " "

	def __init__(self, name):
		self.name = name

	def __str__(self):
		pass

	def getName(self):
		return self.name

class Into(ABC):

	def __init__(self, name):
		self.name = name

	def __str__(self):
		return "a"

