
from datetime import date

class NubbinBattery():
    def __init__(self, battery_year, last_service_date):
        self.battery_year = date.fromisoformat(battery_year)
        self.last_service_date = date.fromisoformat(last_service_date)

    def needs_service(self):
        difference_days = (self.battery_year - self.last_service_date).days
        number_of_years = difference_days / 365

        if number_of_years>4:
            return True
        else:
            return False
