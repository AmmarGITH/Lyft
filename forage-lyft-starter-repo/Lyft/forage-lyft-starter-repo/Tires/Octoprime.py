class Octoprime():
    def __init__(self, tires):
        self.tires = tires
    #Used to check if an item in the list is 0.9
    def needs_service(self):
        return any(wear >= 0.9 for wear in self.tires)

