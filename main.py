from ElectricScooter import ElectricScooter
from ElectricCars import ElectricCars
from Vehicle import Vehicles
from fleetHub import Hub









if __name__ == "__main__" :
    
    hub_manager = Hub()

    ather = ElectricScooter(123,"ather",90,100)
    ola = ElectricScooter(124,"ola",80,100)
    car = ElectricCars(125,"bmw",90,4)
    hub_manager.add_vehicle("Delhi", ather)
    hub_manager.add_vehicle("Mumbai", ola)
    hub_manager.add_vehicle("Delhi", car)

    duplicate_ather = ElectricScooter(123, "another ather", 75, 90)
    hub_manager.add_vehicle("Delhi", duplicate_ather)


    hub_manager.display_hubs()
    








# from ElectricScooter import ElectricScooter
# from ElectricCars import ElectricCars
# from Vehicle import Vehicles






# class EcoRideMain :
#     def greet():
#         print("Welcome to Eco-Ride Urban Mobility System")

# if __name__ == "__main__" :
#     # calculate the cost of the trip for ElectricScooter and ElectricCars
#     # ElectricScooter: 20 km, cost per km = 5 ruppees
#     EcoRideMain.greet()

#     ather = ElectricScooter(123,"ather",90,100)
#     ola = ElectricScooter(124,"ola",80,100)
#     car = ElectricCars(125,"bmw",90,4)
#     lst = [ather,car,ola]
#     for i in lst:
#         print(i.calculate_trip_cost(50))
    # e = ElectricScooter(
    #     123,"ather",90,100
    #     )
    # print(e.calculate_trip_cost(20))

    # # ElectricCars: 30 km, cost per km = 10 ruppees
    # c = ElectricCars(
    #     1,"bmw",90,4
    #     )
    # print(c.calculate_trip_cost(30))

# def main():
#     print("Urban Mobility & Fleet Management System")
#     print()
#     print("-" * 56)
#     print("-" * 56)

#     # vehicle1 = Vehicles("V001", "Maruti 800", 85)
#     # print(f"Vehicle ID: {vehicle1.vehicle_id}, Model: {vehicle1.model}, Battery Percentage: {vehicle1.get_battery_percentage}%")
#     # print(f"vehicle1.get_battery_percentage(): {vehicle1.get_battery_percentage()}% \n vehicle1.get_maintenance_status(): {vehicle1.get_maintenance_status()} \n vehicle1.get_rental_price(): {vehicle1.get_rental_price()}")

#     # vehicle1.set_battery_percentage(90)
#     # vehicle1.set_maintenance_status(1)
#     # vehicle1.set_rental_price(10000)

#     # print(f"After updating vehicle1's attributes:")
#     # print(f"Vehicle ID: {vehicle1.vehicle_id}\n Model: {vehicle1.model} \nBattery Percentage: {vehicle1.get_battery_percentage()}%  \nMaintenance Status: {vehicle1.get_maintenance_status()} \nRental Price: {vehicle1.get_rental_price()}")

#     scooter1 = ElectricScooter(
#     "10x5",
#     "Ather 450X",
#     90,
#     25
# )
#     # scooter1.get_max_speed_limit()
#     scooter1.set_battery_percentage(95)
    
# #     print(f"After updating scooter1's battery percentage: {scooter1.get_battery_percentage()}")
# print(scooter1.calculate_trip_cost(10))
# main()