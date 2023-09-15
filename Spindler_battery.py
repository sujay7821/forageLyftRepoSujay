from abc import ABC
from Battery import Battery
from datetime import datetime


class SpindlerBattery(Battery, ABC):
    def __init__(self, last_service_date, current_mileage, last_service_mileage, warning_light_is_on):
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 3)
        if service_threshold_date < datetime.today().date() or self.need_service():
            return True
        else:
            return False