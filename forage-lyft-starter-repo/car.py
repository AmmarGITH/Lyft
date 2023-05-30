from Serviceable import Serviceable_car


class Car(Serviceable_car):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery


    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()




