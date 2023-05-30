from Serviceable import Serviceable_car


class Car(Serviceable_car):
    def __init__(self, engine, battery, tires):
        self.engine = engine
        self.battery = battery
        self.tire = tires


    def needs_service(self):
        print(self.engine.engine_should_be_serviced())
        print(self.battery.needs_service())
        return self.engine.engine_should_be_serviced() or self.battery.needs_service() #or self.tire.needs_service()






