class car:

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("VRUUUUUUUUUUUUM!!!!!!!!!!!!!")

    def stop(self):
        print("CREEEEEEEEEEEEEEEECH (stoping sound)")


firstCar = car()

firstCar.color