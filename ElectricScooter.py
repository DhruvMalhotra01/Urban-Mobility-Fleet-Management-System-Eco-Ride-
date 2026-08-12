from Vehicle import Vehicles


class ElectricScooter(Vehicles):
    BASE_FARE = 1
    COST_PER_MINUTE = 0.15

    def __init__(self, vehicle_id, model, battery_percentage, max_speed_limit):
        super().__init__(vehicle_id, model, battery_percentage)
        self.__max_speed_limit = max_speed_limit
        self.max_speed_limit = max_speed_limit

    def get_max_speed_limit(self):
        return self.__max_speed_limit

    def calculate_trip_cost(self, minutes):
        return self.BASE_FARE + minutes * self.COST_PER_MINUTE
