
from datetime import datetime
class SpinderBattery():
    def __init__(self, last_service_date, battery_year):
        self.battery_year = battery_year
        self.last_service_date = last_service_date

    def needs_service(self):
        difference_days = (self.battery_year - self.last_service_date).days
        number_of_years = difference_days / 365
        if number_of_years>2:
            return True
        else:
            return False

