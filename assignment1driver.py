import assignment1 as one

# waynes car
c1 = one.Car("Pinto", "Ford")
print(c1.model)
print(c1.make)
print(c1.getName())
c1.start()
print(c1.getWheels())
print("Car has engine?: " + str(c1.getEngine()))

#garth's bike
b1 = one.Bike("Mode 100", "Mongoose")
print(b1.model)
print(b1.make)
print(b1.getName())
b1.pedal()
print(b1.getWheels())
print("Bike has engine?: " + str(b1.getEngine()))
