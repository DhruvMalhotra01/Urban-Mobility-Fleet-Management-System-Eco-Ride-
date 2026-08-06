from ElectricScooter    import ElectricScooter
from ElectricCars  import ElectricCars

class Hub:

    def __init__(self):
        self.hubs = {}

    def add_hub(self, hub_name):
        if hub_name not in self.hubs:
            self.hubs[hub_name] = []
            print(f"Hub '{hub_name}' created")
        else:
            print(f"Hub '{hub_name}' already exists")

    def add_vehicle(self, hub_name, vehicle):

        if hub_name not in self.hubs:
            self.add_hub(hub_name)

        existing_vehicles = self.hubs[hub_name]

        duplicates = [i for i in existing_vehicles if i == vehicle]

        if duplicates:
            print(
                f"A vehicle with {vehicle.vehicle_id} id "
                f"already exists in the {hub_name} hub"
            )
            return

        self.hubs[hub_name].append(vehicle)

        print(f"Vehicle added to {hub_name}")

    def display_hubs(self):

        for hub_name, vehicles in self.hubs.items():

            print(f"\nHub: {hub_name}")

            for vehicle in vehicles:
                print(f"Vehicle ID: {vehicle.vehicle_id}")
                print(f"Model: {vehicle.model}")


     # Search vehicles by Hub
    def search_by_hub(self, hub_name):

        if hub_name in self.hubs:

            vehicles = self.hubs[hub_name]

            for vehicle in vehicles:
                print(f"Vehicle ID: {vehicle.vehicle_id}")
                print(f"Model: {vehicle.model}")
                print(f"Battery: {vehicle.get_battery_percentage()}%")

        else:
            print(f"Hub '{hub_name}' not found")


    # Search vehicles with battery > 80
    def search_by_battery(self):

        all_vehicles = [
            vehicle
            for vehicles in self.hubs.values()
            for vehicle in vehicles
        ]

        result = list(
            filter(
                lambda vehicle: vehicle.get_battery_percentage() > 80,
                all_vehicles
            )
        )

        return result

    def search_by_type(self, vehicle_type):

        all_vehicles = [
            vehicle
            for vehicles in self.hubs.values()
            for vehicle in vehicles
        ]

        result = list(
            filter(
                lambda vehicle: isinstance(vehicle, vehicle_type),
                all_vehicles
            )
        )

        return result

    
