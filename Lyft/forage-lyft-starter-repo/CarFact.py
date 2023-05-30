from Battery.NubbinBattery import NubbinBattery
from Battery.SpinderBattery import SpinderBattery
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
#Since i do not know which care uses which tires we need to remove this to gain access to tires
#from Tires.Carrigan import  Carrigan
#from Tires.Octoprime import Octoprime
class CarFact:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tires):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpinderBattery(current_date, last_service_date)
        car = Car(engine, battery, tires)
        return car

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tires):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpinderBattery(current_date, last_service_date)
        car = Car(engine, battery, tires)
        return car

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_is_on, tires):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpinderBattery(current_date, last_service_date)
        car = Car(engine, battery, tires)
        return car

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tires):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        car = Car(engine, battery, tires)
        return car

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tires):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        car = Car(engine, battery, tires)
        return car


c1 = CarFact.create_calliope("2020-05-30","2019-04-30", 23466, 0, [0.8, 0.7, 0.95, 0.6])

print(c1.needs_service())