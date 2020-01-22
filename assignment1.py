from abc import ABC

class Vehicle(ABC):
	def __init__(self, model, make):
		pass
	def setName(self, name):
		pass
	def getName(self):
		pass
	def pedal(self):
		pass
	def getWheels(self):
		pass
	def getEngine(self):
		pass

class Car(Vehicle):
	def __init__(self, model, make):
		self.model = model
		self.make = make
		self.setName("Wayne")
		self.wheels = Wheels(4)
		self.engine = Engine(True)

	def setName(self, name):
		self.__name = name

	def getName(self):
		return self.__name
	def start(self):
		print("Car is starting")
	def getWheels(self):
		return self.wheels.number
	def getEngine(self):
		return self.engine.hasEngine

class Bike(Vehicle):
	def __init__(self, model, make):
		self.model = model
		self.make = make
		self.setName("Garth")
		self.wheels = Wheels(2)
		self.engine = Engine(False)

	def setName(self, name):
		self.__name = name
    
	def getName(self):
		return self.__name

	def pedal(self):
		print("Bike is pedalling")
	def getWheels(self):
		return self.wheels.number
	def getEngine(self):
		return self.engine.hasEngine

class Wheels:
	def __init__(self, number):
		self.number = number

class Engine:
	def __init__(self, engine=False):
		self.hasEngine = engine


