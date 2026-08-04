from Vehicle import Vehicles

def main():
    print("Urban Mobility & Fleet Management System")

    vehicle1 = Vehicles("V001", "Maruti 800", 85)
    print(f"Vehicle ID: {vehicle1.vehicle_id}, Model: {vehicle1.model}, Battery Percentage: {vehicle1.battery_percentage}%")

# if __name__ == "__main__":
main()