
from datetime import date
class SpinderBattery():
    def __init__(self, battery_year, last_service_date):
        self.battery_year = date.fromisoformat(battery_year)
        self.last_service_date = date.fromisoformat(last_service_date)

    def needs_service(self):
        print(self.battery_year)
        print(self.last_service_date)
        difference_days = (self.battery_year - self.last_service_date).days
        number_of_years = difference_days / 365
        print(number_of_years)
        if number_of_years>3:
            return True
        else:
            return False

