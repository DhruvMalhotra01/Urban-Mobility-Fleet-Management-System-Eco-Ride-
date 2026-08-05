from Vehicle import Vehicles


class ElectricScooter(Vehicles):

    def __init__(self, vehicle_id, model, battery_percentage, max_speed_limit):

        super().__init__(vehicle_id = vehicle_id, model = model, battery_percentage = battery_percentage)

        self.max_speed_limit = max_speed_limit

    def get_max_speed_limit(self):
        print(f"Max Speed Limit: {self.max_speed_limit} km/h")

    def calculate_trip_cost(self, minutes):
        cost_per_minute = 0.15  # Assuming a cost is 0.15 ruppees per minute
        total_cost = 1 + minutes * cost_per_minute
        return total_cost