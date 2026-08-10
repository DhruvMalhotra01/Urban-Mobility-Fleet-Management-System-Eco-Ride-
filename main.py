from ElectricCars import ElectricCars
from ElectricScooter import ElectricScooter
from fleetHub import Hub


def create_vehicles():
    """Create demo vehicle instances for the Eco-Ride system."""
    return [
        ElectricScooter("S001", "Ather 450X", 90, 100),
        ElectricScooter("S002", "Ola S1 Pro", 80, 95),
        ElectricCars("C001", "BMW i4", 90, 4),
    ]


def demonstrate_encapsulation(vehicle):
    """Demonstrate encapsulated access to vehicle state."""
    print("\n=== Encapsulation Demo ===")
    print(f"Vehicle ID: {vehicle.vehicle_id}")
    print(f"Model: {vehicle.model}")
    print(f"Initial battery: {vehicle.get_battery_percentage()}%")

    vehicle.set_battery_percentage(95)
    vehicle.set_maintenance_status(1)
    vehicle.set_rental_price(15000)

    print("After updates:")
    print(f"Battery: {vehicle.get_battery_percentage()}%")
    print(f"Maintenance status: {vehicle.get_maintenance_status()}")
    print(f"Rental price: ₹{vehicle.get_rental_price()}")


def demonstrate_trip_costs(vehicles):
    """Calculate and print trip costs for demo vehicles."""
    print("\n=== Trip Cost Demo ===")

    for vehicle in vehicles:
        if isinstance(vehicle, ElectricCars):
            cost = vehicle.calculate_trip_cost(30)
            distance_label = "30 km"
        else:
            cost = vehicle.calculate_trip_cost(20)
            distance_label = "20 minutes"


        print(f"{vehicle.model}: {distance_label} trip cost = ₹{cost:.2f}")


def demonstrate_search(hub_manager):
    """Demonstrate searching vehicles by hub and battery."""

    print("\n=== Search by Hub ===")
    hub_manager.search_by_hub("Delhi")

    print("\n=== Vehicles with Battery > 80% ===")

    high_battery = hub_manager.search_by_battery()

    for vehicle in high_battery:
        print(
            f"Vehicle ID: {vehicle.vehicle_id}, "
            f"Model: {vehicle.model}, "
            f"Battery: {vehicle.get_battery_percentage()}%"
        )

def demonstrate_search_by_type(hub_manager, vehicle_type):
    """Demonstrate searching vehicles by type."""

    print(f"\n=== Search by Vehicle Type: {vehicle_type.__name__} ===")

    vehicles_of_type = hub_manager.search_by_type(vehicle_type)

    if vehicles_of_type:
        for vehicle in vehicles_of_type:
            print(
                f"Vehicle ID: {vehicle.vehicle_id}, "
                f"Model: {vehicle.model}, "
                f"Battery: {vehicle.get_battery_percentage()}%"
            )
    else:
        print(f"No vehicles of type {vehicle_type.__name__} found.")

def demonstrate_hub_management(vehicles):
    """Add vehicles to hubs and show duplicate detection."""

    print("\n=== Hub Management Demo ===")

    hub_manager = Hub()

    hub_manager.add_vehicle("Delhi", vehicles[0])
    hub_manager.add_vehicle("Mumbai", vehicles[1])
    hub_manager.add_vehicle("Delhi", vehicles[2])

    duplicate_ather = ElectricScooter("S001", "Ather 450X Duplicate", 75, 90)
    hub_manager.add_vehicle("Delhi", duplicate_ather)

    hub_manager.display_hubs()

    return hub_manager



def main():
    print("Welcome to Eco-Ride Urban Mobility System")
    print("Urban Mobility & Fleet Management System")
    print("=" * 56)

    vehicles = create_vehicles()
    demonstrate_encapsulation(vehicles[0])
    demonstrate_trip_costs(vehicles)
    hub_manager = demonstrate_hub_management(vehicles)

    demonstrate_search(hub_manager)

    demonstrate_search_by_type(hub_manager, ElectricCars)
    demonstrate_search_by_type(hub_manager, ElectricScooter)


if __name__ == "__main__":
    main()