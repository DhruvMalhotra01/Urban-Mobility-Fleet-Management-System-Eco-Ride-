from ElectricScooter import ElectricScooter


def test_electric_scooter_creation():
    scooter = ElectricScooter("S001", "Ather 450X", 90, 100)

    assert scooter.vehicle_id == "S001"
    assert scooter.model == "Ather 450X"
    assert scooter.get_battery_percentage() == 90
    assert scooter.get_max_speed_limit() == 100
    assert scooter.max_speed_limit == 100


def test_electric_scooter_trip_cost():
    scooter = ElectricScooter("S001", "Ather 450X", 90, 100)

    assert scooter.calculate_trip_cost(20) == 4
