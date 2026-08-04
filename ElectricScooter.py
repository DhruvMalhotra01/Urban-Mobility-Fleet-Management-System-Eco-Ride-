from Vehicle import Vehicles


class ElectricScooter(Vehicles):

    def __init__(self, vehicle_id, model, battery_percentage, max_speed_limit):

        super().__init__(vehicle_id = vehicle_id, model = model, battery_percentage = battery_percentage)

        self.max_speed_limit = max_speed_limit

    def get_max_speed_limit(self):
        print(f"Max Speed Limit: {self.max_speed_limit} km/h")