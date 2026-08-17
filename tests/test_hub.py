from ElectricCars import ElectricCars
from ElectricScooter import ElectricScooter
from fleetHub import Hub


def create_test_hub():
    hub = Hub()
    car = ElectricCars("C001", "BMW i4", 90, 4)
    scooter = ElectricScooter("S001", "Ather 450X", 85, 100)

    hub.add_vehicle("Delhi", car)
    hub.add_vehicle("Delhi", scooter)

    return hub, car, scooter


def test_hub_starts_empty():
    hub = Hub()

    assert hub.hubs == {}


def test_add_hub_creates_new_hub():
    hub = Hub()

    hub.add_hub("Delhi")

    assert "Delhi" in hub.hubs
    assert hub.hubs["Delhi"] == []


def test_add_hub_does_not_duplicate_existing_hub():
    hub = Hub()

    hub.add_hub("Delhi")
    hub.add_hub("Delhi")

    assert list(hub.hubs.keys()) == ["Delhi"]


def test_add_vehicle_creates_hub_when_missing():
    hub = Hub()
    car = ElectricCars("C001", "BMW i4", 90, 4)

    hub.add_vehicle("Delhi", car)

    assert hub.hubs["Delhi"] == [car]


def test_add_vehicle_to_existing_hub():
    hub, car, scooter = create_test_hub()

    assert hub.hubs["Delhi"] == [car, scooter]


def test_duplicate_vehicle_not_added():
    hub = Hub()
    car = ElectricCars("C001", "BMW i4", 90, 4)
    duplicate_id = ElectricCars("C001", "Another BMW", 80, 5)

    hub.add_vehicle("Delhi", car)
    hub.add_vehicle("Delhi", duplicate_id)

    assert hub.hubs["Delhi"] == [car]


def test_search_by_hub_returns_matching_vehicles():
    hub, car, scooter = create_test_hub()

    result = hub.search_by_hub("Delhi")

    assert result == [car, scooter]


def test_search_by_missing_hub_returns_empty_list():
    hub = Hub()

    assert hub.search_by_hub("Unknown") == []


def test_search_by_battery_returns_vehicles_above_80_percent():
    hub = Hub()
    car = ElectricCars("C001", "BMW i4", 90, 4)
    scooter = ElectricScooter("S001", "Ather 450X", 70, 100)

    hub.add_vehicle("Delhi", car)
    hub.add_vehicle("Delhi", scooter)

    assert hub.search_by_battery() == [car]


def test_search_by_battery_excludes_low_battery_vehicles():
    hub = Hub()
    car = ElectricCars("C001", "BMW i4", 75, 4)
    scooter = ElectricScooter("S001", "Ather 450X", 85, 100)

    hub.add_vehicle("Delhi", car)
    hub.add_vehicle("Delhi", scooter)

    assert hub.search_by_battery() == [scooter]


def test_search_by_type_accepts_vehicle_class():
    hub, car, scooter = create_test_hub()

    assert hub.search_by_type(ElectricCars) == [car]
    assert hub.search_by_type(ElectricScooter) == [scooter]


def test_search_by_type_for_string_key_returns_matching_group():
    hub, _, _ = create_test_hub()

    assert hub.search_by_type("ElectricCars") == [hub.hubs["Delhi"][0]]
    assert hub.search_by_type("ElectricScooter") == [hub.hubs["Delhi"][1]]


def test_search_by_type_unknown_key_returns_empty_list():
    hub, _, _ = create_test_hub()

    assert hub.search_by_type("UnknownType") == []


def test_status_analytics_counts_each_status():
    hub, car, scooter = create_test_hub()
    car.set_maintenance_status("On Trip")
    scooter.set_maintenance_status("Available")

    assert hub.status_analytics() == {
        "Available": 1,
        "On Trip": 1,
        "Under Maintenance": 0,
    }


def test_sort_vehicles_by_model_orders_hub_vehicles_alphabetically():
    hub = Hub()
    car = ElectricCars("C001", "BMW i4", 90, 4)
    scooter = ElectricScooter("S001", "Ather 450X", 85, 100)

    hub.add_vehicle("Delhi", car)
    hub.add_vehicle("Delhi", scooter)
    hub.sort_vehicles_by_model("Delhi")

    assert hub.hubs["Delhi"] == [scooter, car]


def test_sort_by_battery_orders_hub_by_descending_charge():
    hub = Hub()
    car = ElectricCars("C001", "BMW i4", 80, 4)
    scooter = ElectricScooter("S001", "Ather 450X", 95, 100)

    hub.add_vehicle("Delhi", car)
    hub.add_vehicle("Delhi", scooter)
    hub.sort_by_battery("Delhi")

    assert hub.hubs["Delhi"] == [scooter, car]


def test_sort_by_fare_orders_hub_by_descending_rental_price():
    hub = Hub()
    car = ElectricCars("C001", "BMW i4", 80, 4)
    scooter = ElectricScooter("S001", "Ather 450X", 95, 100)

    car.set_rental_price(50)
    scooter.set_rental_price(100)
    hub.add_vehicle("Delhi", car)
    hub.add_vehicle("Delhi", scooter)
    hub.sort_by_fare("Delhi")

    assert hub.hubs["Delhi"] == [scooter, car]


def test_sort_fleet_by_battery_returns_all_vehicles_descending():
    hub = Hub()
    car = ElectricCars("C001", "BMW i4", 80, 4)
    scooter = ElectricScooter("S001", "Ather 450X", 95, 100)

    hub.add_vehicle("Delhi", car)
    hub.add_vehicle("Mumbai", scooter)

    assert hub.sort_fleet_by_battery() == [scooter, car]


def test_save_to_csv_writes_rows_to_temp_file(tmp_path):
    hub = Hub()
    car = ElectricCars("C001", "BMW i4", 90, 4)
    scooter = ElectricScooter("S001", "Ather 450X", 85, 100)
    hub.add_vehicle("Delhi", car)
    hub.add_vehicle("Delhi", scooter)

    file_path = tmp_path / "fleet.csv"
    hub.save_to_csv(file_path)

    assert file_path.exists()
    assert "hub_name" in file_path.read_text(encoding="utf-8")


def test_load_from_csv_populates_hub_from_saved_data(tmp_path):
    hub = Hub()
    car = ElectricCars("C001", "BMW i4", 90, 4)
    scooter = ElectricScooter("S001", "Ather 450X", 85, 100)
    hub.add_vehicle("Delhi", car)
    hub.add_vehicle("Delhi", scooter)

    file_path = tmp_path / "fleet.csv"
    hub.save_to_csv(file_path)

    new_hub = Hub()
    new_hub.load_from_csv(file_path)

    assert new_hub.hubs["Delhi"][0].vehicle_id == "C001"
    assert new_hub.hubs["Delhi"][1].vehicle_id == "S001"


def test_save_to_json_writes_hub_data(tmp_path):
    hub = Hub()
    car = ElectricCars("C001", "BMW i4", 90, 4)
    scooter = ElectricScooter("S001", "Ather 450X", 85, 100)
    hub.add_vehicle("Delhi", car)
    hub.add_vehicle("Delhi", scooter)

    file_path = tmp_path / "fleet.json"
    hub.save_to_json(file_path)

    assert file_path.exists()
    assert "Delhi" in file_path.read_text(encoding="utf-8")


def test_load_from_json_restores_hub_data(tmp_path):
    hub = Hub()
    car = ElectricCars("C001", "BMW i4", 90, 4)
    scooter = ElectricScooter("S001", "Ather 450X", 85, 100)
    hub.add_vehicle("Delhi", car)
    hub.add_vehicle("Delhi", scooter)

    file_path = tmp_path / "fleet.json"
    hub.save_to_json(file_path)

    new_hub = Hub()
    new_hub.load_from_json(file_path)

    assert new_hub.hubs["Delhi"][0].vehicle_id == "C001"
    assert new_hub.hubs["Delhi"][1].vehicle_id == "S001"
