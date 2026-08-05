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

        self.hubs[hub_name].append(vehicle)

        print(f"Vehicle added to {hub_name}")

    def display_hubs(self):

        for hub_name, vehicles in self.hubs.items():

            print(f"\nHub: {hub_name}")

            for vehicle in vehicles:
                print(f"Vehicle ID: {vehicle.vehicle_id}")
                print(f"Model: {vehicle.model}")