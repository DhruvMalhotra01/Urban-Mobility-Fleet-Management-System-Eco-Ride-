
from Vehicle import Vehicles


class ElectricCars(Vehicles):
    BASE_FARE = 5
    COST_PER_KM = 0.50

    def __init__(self, vehicle_id, model, battery_percentage, seating_capacity):
        super().__init__(vehicle_id, model, battery_percentage)
        self.set_seating_capacity(seating_capacity)

    def get_seating_capacity(self):
        return self.__seating_capacity

    def set_seating_capacity(self, seating_capacity):
        if seating_capacity <= 0:
            raise ValueError("Seating capacity must be greater than 0")
        self.__seating_capacity = seating_capacity
        self.seating_capacity = seating_capacity

    def calculate_trip_cost(self, distance):
        return self.BASE_FARE + distance * self.COST_PER_KM
