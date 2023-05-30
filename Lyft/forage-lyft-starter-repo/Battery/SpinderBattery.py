from battery import battery
from datetime import datetime
class SpinderBattery(battery):
    def __init__(self, last_service_date, battery_year):
        self.battery_year = battery_year
        self.last_service_date = last_service_date

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < datetime.today().date():
            return True
        else:
            return False

