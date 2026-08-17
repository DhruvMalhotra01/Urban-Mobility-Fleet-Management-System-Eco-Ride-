from ElectricCars import ElectricCars


def test_electric_car_creation():
    car = ElectricCars("C001", "BMW i4", 90, 4)

    assert car.vehicle_id == "C001"
    assert car.model == "BMW i4"
    assert car.get_battery_percentage() == 90
    assert car.get_seating_capacity() == 4
    assert car.seating_capacity == 4


def test_electric_car_battery_can_be_updated():
    car = ElectricCars("C001", "BMW i4", 90, 4)

    car.set_battery_percentage(75)

    assert car.get_battery_percentage() == 75


def test_electric_car_battery_invalid_value_is_ignored():
    car = ElectricCars("C001", "BMW i4", 90, 4)

    car.set_battery_percentage(120)

    assert car.get_battery_percentage() == 90


def test_electric_car_seating_capacity_setter_updates_value():
    car = ElectricCars("C001", "BMW i4", 90, 4)

    car.set_seating_capacity(5)

    assert car.get_seating_capacity() == 5
    assert car.seating_capacity == 5


def test_electric_car_trip_cost_positive_distance():
    car = ElectricCars("C001", "BMW i4", 90, 4)

    assert car.calculate_trip_cost(30) == 20


def test_electric_car_trip_cost_zero_distance():
    car = ElectricCars("C001", "BMW i4", 90, 4)

    assert car.calculate_trip_cost(0) == 5


def test_electric_car_trip_cost_negative_distance_is_allowed():
    car = ElectricCars("C001", "BMW i4", 90, 4)

    assert car.calculate_trip_cost(-10) == 0


def test_electric_car_rental_price_can_be_set():
    car = ElectricCars("C001", "BMW i4", 90, 4)

    car.set_rental_price(120)

    assert car.get_rental_price() == 120


def test_electric_car_negative_rental_price_is_ignored():
    car = ElectricCars("C001", "BMW i4", 90, 4)

    car.set_rental_price(120)
    car.set_rental_price(-5)

    assert car.get_rental_price() == 120


def test_electric_car_maintenance_status_can_be_updated():
    car = ElectricCars("C001", "BMW i4", 90, 4)

    car.set_maintenance_status("On Trip")

    assert car.get_maintenance_status() == "On Trip"


def test_electric_car_invalid_maintenance_status_is_ignored():
    car = ElectricCars("C001", "BMW i4", 90, 4)

    car.set_maintenance_status("Broken")

    assert car.get_maintenance_status() == 0


def test_electric_car_string_contains_key_details():
    car = ElectricCars("C001", "BMW i4", 90, 4)

    string_value = str(car)

    assert "C001" in string_value
    assert "BMW i4" in string_value
    assert "90%" in string_value


def test_electric_car_equality_uses_vehicle_id():
    car1 = ElectricCars("C001", "BMW i4", 90, 4)
    car2 = ElectricCars("C001", "Tesla Model 3", 80, 5)

    assert car1 == car2


def test_electric_car_inequality_for_different_ids():
    car1 = ElectricCars("C001", "BMW i4", 90, 4)
    car2 = ElectricCars("C002", "BMW i4", 90, 4)

    assert car1 != car2
