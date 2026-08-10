from collections import defaultdict
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

    def search_by_type(self, vehicle_type=None):
        

        grouped_vehicles = defaultdict(list)

        for hub_name, vehicles in self.hubs.items():
            for vehicle in vehicles:
                if isinstance(vehicle, ElectricCars):
                    grouped_vehicles['ElectricCars'].append((hub_name, vehicle))
                elif isinstance(vehicle, ElectricScooter):
                    grouped_vehicles['ElectricScooter'].append((hub_name, vehicle))
                else:
                    grouped_vehicles['Other'].append((hub_name, vehicle))

        # If caller passed a class, return list of matching vehicle objects
        if isinstance(vehicle_type, type):
            result = []
            for _, vehicles in self.hubs.items():
                for v in vehicles:
                    if isinstance(v, vehicle_type):
                        result.append(v)
            if not result:
                print(f"No vehicles of type {vehicle_type.__name__} found.")
            return result

        # If caller passed a string key, show that group
        if vehicle_type:
            items = grouped_vehicles.get(vehicle_type, [])
            if not items:
                print(f"No vehicles of type '{vehicle_type}' found.")
                return []
            print(f"\nVehicles of type '{vehicle_type}':")
            for hub_name, v in items:
                print(f"Hub: {hub_name} - ID: {v.vehicle_id}, Model: {v.model}, Battery: {v.get_battery_percentage()}%")
            return [v for _, v in items]

        # Default: print full categorized view
        print("\n=== Vehicles grouped by type ===")
        for k in ('ElectricCars', 'ElectricScooter', 'Other'):
            if grouped_vehicles.get(k):
                print(f"\n{k}:")
                for hub_name, v in grouped_vehicles[k]:
                    print(f"Hub: {hub_name} - ID: {v.vehicle_id}, Model: {v.model}, Battery: {v.get_battery_percentage()}%")

        return grouped_vehicles

    def sort_vehicles_by_model(self, hub_name):

        if hub_name not in self.hubs:
            print(f"Hub '{hub_name}' not found")
            return

        self.hubs[hub_name].sort(key=lambda vehicle: vehicle.model)

        print(f"\nVehicles in {hub_name} sorted alphabetically:")
        
        for vehicle in self.hubs[hub_name]:
            print(vehicle)

    def sort_by_battery(self, hub_name):

        if hub_name not in self.hubs:
            print(f"Hub '{hub_name}' not found")
            return

        self.hubs[hub_name].sort(
            key=lambda vehicle: vehicle.get_battery_percentage(),
            reverse=True
        )

        print(f"\nVehicles in {hub_name} sorted by battery:")

        for vehicle in self.hubs[hub_name]:
            print(vehicle)

    def sort_by_fare(self, hub_name):

        if hub_name not in self.hubs:
            print(f"Hub '{hub_name}' not found")
            return

        self.hubs[hub_name].sort(
            key=lambda vehicle: vehicle.get_rental_price(),
            reverse=True
        )

        print(f"\nVehicles in {hub_name} sorted by fare:")

        for vehicle in self.hubs[hub_name]:
            print(vehicle)

    def sort_fleet_by_battery(self):

        all_vehicles = [
            vehicle
            for vehicles in self.hubs.values()
            for vehicle in vehicles
        ]

        return sorted(
            all_vehicles,
            key=lambda vehicle: vehicle.get_battery_percentage(),
            reverse=True
        )
    def status_analytics(self):

        status_count = {
            "Available": 0,
            "On Trip": 0,
            "Under Maintenance": 0
        }

        for vehicles in self.hubs.values():
            for vehicle in vehicles:

                status = vehicle.get_maintenance_status()

                if status in status_count:
                    status_count[status] += 1

        print("\n===== Fleet Status Analytics =====")

        print(f"Available vehicles         : {status_count['Available']}")
        print(f"On Trip vehicles           : {status_count['On Trip']}")
        print(f"Under Maintenance vehicles : {status_count['Under Maintenance']}")
    
