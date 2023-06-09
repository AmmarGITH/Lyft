import unittest

from engine import capulet_engine
cap = capulet_engine.CapuletEngine

class TestCapuletEngine(unittest.TestCase):
    def test_needs_service_true(self):
        current_mileage = 30001
        last_service_mileage = 0
        engine = cap(current_mileage, last_service_mileage)
        self.assertTrue(engine.engine_should_be_serviced())

    def test_needs_service_false(self):
        current_mileage = 24357
        last_service_mileage = 0
        engine = cap(current_mileage, last_service_mileage)
        self.assertFalse(engine.engine_should_be_serviced())


from engine import sternman_engine
stern = sternman_engine.SternmanEngine
class TestSternmanEngine(unittest.TestCase):
    def test_needs_service_true(self):
        light = True
        engine = stern(light)
        self.assertTrue(engine.engine_should_be_serviced())


    def test_needs_service_false(self):
        light = False
        engine = stern(light)
        self.assertFalse(engine.engine_should_be_serviced())
from engine import willoughby_engine
will = willoughby_engine.WilloughbyEngine
class willoughbhy(unittest.TestCase):
    def test_needs_service_true(self):
        current_mileage = 86900
        last_service_mileage = 0
        engine = will(current_mileage, last_service_mileage)
        self.assertTrue(engine.engine_should_be_serviced())

    def test_needs_service_false(self):
        current_mileage = 24357
        last_service_mileage = 0
        engine = cap(current_mileage, last_service_mileage)
        self.assertFalse(engine.engine_should_be_serviced())

from Battery import NubbinBattery
nub = NubbinBattery.NubbinBattery
class Nubbin(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = "2020-05-30"
        last_service_date = "2016-04-30"
        battery = nub(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = "2023-05-30"
        last_service_date = "2022-04-25"
        battery = nub(current_date, last_service_date)
        self.assertFalse(battery.needs_service())


from Battery import SpinderBattery
spid = SpinderBattery.SpinderBattery
class Spinder(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = "2020-05-30"
        last_service_date = "2016-04-30"
        battery = nub(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = "2023-05-30"
        last_service_date = "2022-04-25"
        battery = nub(current_date, last_service_date)
        self.assertFalse(battery.needs_service())

from Tires import Octoprime
octo = Octoprime.Octoprime
class Octoprime(unittest.TestCase):

    def test_needs_service_true(self):
        tires = [0.5, 0.5, 0.5, 3]
        self.assertTrue(octo(tires).needs_service())
    def test_needs_service_false(self):
        tires = [0.5, 0.5, 0.5, 0.5]
        self.assertFalse(octo(tires).needs_service())


from Tires import Carrigan
carri = Carrigan.Carrigan
class Carrigan(unittest.TestCase):

    def test_needs_service_true(self):
        tires = [0.8, 0.7, 0.95, 0.6]
        self.assertTrue(carri(tires).needs_service())
    def test_needs_service_false(self):
        tires = [0.8, 0.7, 0.8, 0.6]
        self.assertFalse(carri(tires).needs_service())
