class Vehicles:
    def __init__(self,vehicle_id,model,battery_percentage):
        self.vehicle_id = vehicle_id
        self.model = model
        #self.__battery_percentage = battery_percentage
        self.set_battery_percentage(battery_percentage)
        self.__maintenance_status = 0# where to initialize the maintenance status??
        self.__rental_price = 0# where to initialize the rental price??
        

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
    def set_maintenance_status(self,status):
        self.__maintenance_status = status

    #getter for Rental_Price
    def get_rental_price(self):  # function to get the rental price
        return self.__rental_price

    def set_rental_price(self,price):
        if price < 0:
            print("Rental price cannot be negative")
        else:
            self.__rental_price = price