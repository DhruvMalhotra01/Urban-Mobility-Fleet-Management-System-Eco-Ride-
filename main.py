from ElectricScooter import ElectricScooter
from Vehicle import Vehicles

def main():
    print("Urban Mobility & Fleet Management System")
    print()
    print("-" * 56)
    print("-" * 56)

    # vehicle1 = Vehicles("V001", "Maruti 800", 85)
    # print(f"Vehicle ID: {vehicle1.vehicle_id}, Model: {vehicle1.model}, Battery Percentage: {vehicle1.get_battery_percentage}%")
    # print(f"vehicle1.get_battery_percentage(): {vehicle1.get_battery_percentage()}% \n vehicle1.get_maintenance_status(): {vehicle1.get_maintenance_status()} \n vehicle1.get_rental_price(): {vehicle1.get_rental_price()}")

    # vehicle1.set_battery_percentage(90)
    # vehicle1.set_maintenance_status(1)
    # vehicle1.set_rental_price(10000)

    # print(f"After updating vehicle1's attributes:")
    # print(f"Vehicle ID: {vehicle1.vehicle_id}\n Model: {vehicle1.model} \nBattery Percentage: {vehicle1.get_battery_percentage()}%  \nMaintenance Status: {vehicle1.get_maintenance_status()} \nRental Price: {vehicle1.get_rental_price()}")

    scooter1 = ElectricScooter(
    "10x5",
    "Ather 450X",
    90,
    25
)
    scooter1.get_max_speed_limit()
    scooter1.set_battery_percentage(95)
    
    print(f"After updating scooter1's battery percentage: {scooter1.get_battery_percentage()}")
main()