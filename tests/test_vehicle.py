from Vehicle import Vehicles


class DummyVehicle(Vehicles):
    def calculate_trip_cost(self, distance):
        return distance


def test_vehicle_creation():
    vehicle = DummyVehicle("V001", "Test Vehicle", 80)

    assert vehicle.vehicle_id == "V001"
    assert vehicle.model == "Test Vehicle"
    assert vehicle.get_battery_percentage() == 80


def test_battery_update():
    vehicle = DummyVehicle("V001", "Test Vehicle", 80)

    vehicle.set_battery_percentage(90)

    assert vehicle.get_battery_percentage() == 90


def test_invalid_battery_does_not_update():
    vehicle = DummyVehicle("V001", "Test Vehicle", 80)

    vehicle.set_battery_percentage(120)

    assert vehicle.get_battery_percentage() == 80


def test_valid_maintenance_status_update():
    vehicle = DummyVehicle("V001", "Test Vehicle", 80)

    vehicle.set_maintenance_status("On Trip")

    assert vehicle.get_maintenance_status() == "On Trip"


def test_invalid_maintenance_status_does_not_update():
    vehicle = DummyVehicle("V001", "Test Vehicle", 80)

    vehicle.set_maintenance_status("Broken")

    assert vehicle.get_maintenance_status() == 0


def test_negative_rental_price_does_not_update():
    vehicle = DummyVehicle("V001", "Test Vehicle", 80)

    vehicle.set_rental_price(15000)
    vehicle.set_rental_price(-5)

    assert vehicle.get_rental_price() == 15000


def test_vehicles_are_equal_when_ids_match():
    first = DummyVehicle("V001", "First Model", 80)
    second = DummyVehicle("V001", "Second Model", 50)

    assert first == second
