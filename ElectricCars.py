from Vehicle import Vehicles

class ElectricCars(Vehicles):
    def __init__(self, vehicle_id, model, battery_percentage, seating_capacity):
    
            super().__init__(vehicle_id = vehicle_id, model = model, battery_percentage = battery_percentage)
    
            self.seating_capacity = seating_capacity
    

    def get_seating_capacity(self):
          print(f"Seating Capacity: {self.seating_capacity}")