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


# =========================================================
# UC1 - Encapsulation
# =========================================================

def demonstrate_encapsulation(vehicle):
    """Demonstrate encapsulated access to vehicle state."""

    print("\n=== Encapsulation Demo ===")

    print(f"Vehicle ID: {vehicle.vehicle_id}")
    print(f"Model: {vehicle.model}")
    print(f"Initial battery: {vehicle.get_battery_percentage()}%")

    vehicle.set_battery_percentage(95)

    # Use valid status instead of 1
    vehicle.set_maintenance_status("On Trip")

    vehicle.set_rental_price(15000)

    print("\nAfter updates:")
    
    print(f"Battery: {vehicle.get_battery_percentage()}%")
    print(f"Maintenance status: {vehicle.get_maintenance_status()}")
    print(f"Rental price: INR {vehicle.get_rental_price()}")


# =========================================================
# UC4 + UC5 - Abstraction / Polymorphism
# =========================================================

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

        print(
            f"{vehicle.model}: "
            f"{distance_label} trip cost = INR {cost:.2f}"
        )


# =========================================================
# UC6 + UC7 - Hub Management / Duplicate Detection
# =========================================================

def demonstrate_hub_management(vehicles):
    """Add vehicles to hubs and show duplicate detection."""

    print("\n=== Hub Management Demo ===")

    hub_manager = Hub()

    # Add vehicles to hubs
    hub_manager.add_vehicle("Delhi", vehicles[0])
    hub_manager.add_vehicle("Mumbai", vehicles[1])
    hub_manager.add_vehicle("Delhi", vehicles[2])

    # Duplicate vehicle ID
    duplicate_ather = ElectricScooter(
        "S001",
        "Ather 450X Duplicate",
        75,
        90
    )

    hub_manager.add_vehicle("Delhi", duplicate_ather)

    # Set vehicle statuses
    vehicles[0].set_maintenance_status("On Trip")
    vehicles[1].set_maintenance_status("Under Maintenance")
    vehicles[2].set_maintenance_status("Available")

    hub_manager.display_hubs()

    return hub_manager


# =========================================================
# UC8 - Search
# =========================================================

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


# =========================================================
# UC9 - Search / Group by Vehicle Type
# =========================================================

def demonstrate_search_by_type(hub_manager, vehicle_type):
    """Demonstrate searching vehicles by type."""

    print(
        f"\n=== Search by Vehicle Type: "
        f"{vehicle_type.__name__} ==="
    )

    vehicles_of_type = hub_manager.search_by_type(vehicle_type)

    if vehicles_of_type:

        for vehicle in vehicles_of_type:

            print(
                f"Vehicle ID: {vehicle.vehicle_id}, "
                f"Model: {vehicle.model}, "
                f"Battery: {vehicle.get_battery_percentage()}%"
            )

    else:
        print(
            f"No vehicles of type "
            f"{vehicle_type.__name__} found."
        )


# =========================================================
# UC11 - Alphabetical Sorting
# =========================================================

def demonstrate_sorting(hub_manager):

    print("\n=== Alphabetical Sorting ===")

    hub_manager.sort_vehicles_by_model("Delhi")


# =========================================================
# UC10 - Fleet Analytics
# =========================================================

def demonstrate_status_analytics(hub_manager):

    print("\n=== Fleet Analytics ===")

    hub_manager.status_analytics()


# =========================================================
# UC12 - Advanced Sorting
# =========================================================

def demonstrate_advanced_sorting(hub_manager):

    print("\n=== Fleet Sorted By Battery ===")

    vehicles = hub_manager.sort_fleet_by_battery()

    for vehicle in vehicles:
        print(vehicle)

    print("\n=== Sort Delhi By Battery ===")

    hub_manager.sort_by_battery("Delhi")

    print("\n=== Sort Delhi By Fare ===")

    hub_manager.sort_by_fare("Delhi")


# =========================================================
# UC13 - CSV Persistence
# =========================================================

def demonstrate_csv_persistence(hub_manager):

    print("\n=== CSV Persistence ===")

    # Save fleet
    hub_manager.save_to_csv("fleet.csv")

    # Create a new Hub
    new_hub = Hub()

    # Load fleet
    new_hub.load_from_csv("fleet.csv")

    print("\nFleet loaded from CSV:")

    new_hub.display_hubs()


# =========================================================
# UC14 - JSON Persistence
# =========================================================

def demonstrate_json_persistence(hub_manager):

    print("\n=== JSON Persistence ===")

    # Save fleet
    hub_manager.save_to_json("fleet.json")

    # Create a new Hub
    new_hub = Hub()

    # Load fleet
    new_hub.load_from_json("fleet.json")

    print("\nFleet loaded from JSON:")

    new_hub.display_hubs()


# =========================================================
# MAIN
# =========================================================

def main():

    print("Welcome to Eco-Ride Urban Mobility System")
    print("Urban Mobility & Fleet Management System")
    print("=" * 56)

    # Create vehicles
    vehicles = create_vehicles()

    # UC1 - Encapsulation
    demonstrate_encapsulation(vehicles[0])

    # UC4 + UC5 - Abstraction + Polymorphism
    demonstrate_trip_costs(vehicles)

    # UC6 + UC7 - Hub + Duplicate Detection
    hub_manager = demonstrate_hub_management(vehicles)

    # UC8 - Search
    demonstrate_search(hub_manager)

    # UC9 - Search by Type
    demonstrate_search_by_type(
        hub_manager,
        ElectricCars
    )

    demonstrate_search_by_type(
        hub_manager,
        ElectricScooter
    )

    # UC10 - Fleet Analytics
    demonstrate_status_analytics(hub_manager)

    # UC11 - Alphabetical Sorting
    demonstrate_sorting(hub_manager)

    # UC12 - Advanced Sorting
    demonstrate_advanced_sorting(hub_manager)

    # UC13 - CSV
    demonstrate_csv_persistence(hub_manager)

    # UC14 - JSON
    demonstrate_json_persistence(hub_manager)


if __name__ == "__main__":
    main()