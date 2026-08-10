from abc import ABC, abstractmethod

class Vehicles(ABC):
    def __init__(self,vehicle_id,model,battery_percentage):
        self.vehicle_id = vehicle_id
        self.model = model
        #self.__battery_percentage = battery_percentage
        self.set_battery_percentage(battery_percentage)
        self.__maintenance_status = 0# where to initialize the maintenance status??
        self.__rental_price = 0# where to initialize the rental price??

    def __str__(self):
        return (
            f"Vehicle ID: {self.vehicle_id}, "
            f"Model: {self.model}, "
            f"Battery: {self.get_battery_percentage()}%, "
            f"Status: {self.get_maintenance_status()}"
        )
        

    #Getter battery
    def get_battery_percentage(self):
        return self.__battery_percentage

    #Setter battery
    def set_battery_percentage(self,battery_percentage):
        if battery_percentage < 0 or battery_percentage > 100:
            print("battery_percentage cannot be more than 100 or less than 0")
        else:
            self.__battery_percentage = battery_percentage

    #getter for maintenance 
    def get_maintenance_status(self):
        return self.__maintenance_status
    #setter for maintenance
    def set_maintenance_status(self, status):
        valid_statuses = ["Available", "On Trip", "Under Maintenance"]

        if status in valid_statuses:
            self.__maintenance_status = status
        else:
            print("Invalid vehicle status")

    #getter for Rental_Price
    def get_rental_price(self):  # function to get the rental price
        return self.__rental_price

    def set_rental_price(self,price):
        if price < 0:
            print("Rental price cannot be negative")
        else:
            self.__rental_price = price



    # dunder method __eq__
    def __eq__(self, other):
        if isinstance(other, Vehicles):
            return self.vehicle_id == other.vehicle_id
        return False


    @abstractmethod
    def calculate_trip_cost(self, distance):
        pass