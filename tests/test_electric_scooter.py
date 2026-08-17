from ElectricScooter import ElectricScooter


def test_electric_scooter_creation():
    scooter = ElectricScooter("S001", "Ather 450X", 90, 100)

    assert scooter.vehicle_id == "S001"
    assert scooter.model == "Ather 450X"
    assert scooter.get_battery_percentage() == 90
    assert scooter.get_max_speed_limit() == 100
    assert scooter.max_speed_limit == 100


def test_electric_scooter_battery_can_be_updated():
    scooter = ElectricScooter("S001", "Ather 450X", 90, 100)

    scooter.set_battery_percentage(80)

    assert scooter.get_battery_percentage() == 80


def test_electric_scooter_invalid_battery_is_ignored():
    scooter = ElectricScooter("S001", "Ather 450X", 90, 100)

    scooter.set_battery_percentage(200)

    assert scooter.get_battery_percentage() == 90


def test_electric_scooter_max_speed_setter_updates_value():
    scooter = ElectricScooter("S001", "Ather 450X", 90, 100)

    scooter.set_max_speed_limit(80)

    assert scooter.get_max_speed_limit() == 80
    assert scooter.max_speed_limit == 80


def test_electric_scooter_trip_cost_positive_minutes():
    scooter = ElectricScooter("S001", "Ather 450X", 90, 100)

    assert scooter.calculate_trip_cost(20) == 4


def test_electric_scooter_trip_cost_zero_minutes():
    scooter = ElectricScooter("S001", "Ather 450X", 90, 100)

    assert scooter.calculate_trip_cost(0) == 1


def test_electric_scooter_trip_cost_negative_minutes():
    scooter = ElectricScooter("S001", "Ather 450X", 90, 100)

    assert scooter.calculate_trip_cost(-10) == -0.5


def test_electric_scooter_rental_price_assignment():
    scooter = ElectricScooter("S001", "Ather 450X", 90, 100)

    scooter.set_rental_price(70)

    assert scooter.get_rental_price() == 70


def test_electric_scooter_negative_rental_price_is_ignored():
    scooter = ElectricScooter("S001", "Ather 450X", 90, 100)

    scooter.set_rental_price(70)
    scooter.set_rental_price(-10)

    assert scooter.get_rental_price() == 70


def test_electric_scooter_maintenance_status_update():
    scooter = ElectricScooter("S001", "Ather 450X", 90, 100)

    scooter.set_maintenance_status("Available")

    assert scooter.get_maintenance_status() == "Available"


def test_electric_scooter_invalid_maintenance_status_is_ignored():
    scooter = ElectricScooter("S001", "Ather 450X", 90, 100)

    scooter.set_maintenance_status("Broken")

    assert scooter.get_maintenance_status() == 0


def test_electric_scooter_string_contains_key_details():
    scooter = ElectricScooter("S001", "Ather 450X", 90, 100)

    string_value = str(scooter)

    assert "S001" in string_value
    assert "Ather 450X" in string_value
    assert "90%" in string_value
    assert "0" in string_value or "Available" in string_value


def test_electric_scooter_equality_uses_vehicle_id():
    scooter1 = ElectricScooter("S001", "Ather 450X", 90, 100)
    scooter2 = ElectricScooter("S001", "Ola S1", 80, 90)

    assert scooter1 == scooter2


def test_electric_scooter_inequality_for_different_ids():
    scooter1 = ElectricScooter("S001", "Ather 450X", 90, 100)
    scooter2 = ElectricScooter("S002", "Ather 450X", 90, 100)

    assert scooter1 != scooter2
