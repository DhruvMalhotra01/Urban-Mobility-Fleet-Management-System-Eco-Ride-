from ElectricCars import ElectricCars


def test_electric_car_creation():
    car = ElectricCars("C001", "BMW i4", 90, 4)

    assert car.vehicle_id == "C001"
    assert car.model == "BMW i4"
    assert car.get_battery_percentage() == 90
    assert car.get_seating_capacity() == 4
    assert car.seating_capacity == 4


def test_electric_car_trip_cost():
    car = ElectricCars("C001", "BMW i4", 90, 4)

    assert car.calculate_trip_cost(30) == 20
