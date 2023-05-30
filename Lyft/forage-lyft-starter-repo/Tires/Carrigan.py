class Carrigan():
    def __init__(self, tires):
        self.tires = tires
    #Used to check the sum of the tires
    def needs_service(self):
        return sum(self.tires) >= 3
