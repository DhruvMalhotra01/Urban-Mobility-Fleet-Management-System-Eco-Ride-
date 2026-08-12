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


def test_add_vehicle_creates_hub_when_missing():
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


def test_search_by_type_accepts_vehicle_class():
    hub, car, scooter = create_test_hub()

    assert hub.search_by_type(ElectricCars) == [car]
    assert hub.search_by_type(ElectricScooter) == [scooter]


def test_status_analytics_counts_each_status():
    hub, car, scooter = create_test_hub()
    car.set_maintenance_status("On Trip")
    scooter.set_maintenance_status("Available")

    assert hub.status_analytics() == {
        "Available": 1,
        "On Trip": 1,
        "Under Maintenance": 0,
    }


def test_sort_by_model_orders_hub_vehicles_alphabetically():
    hub, car, scooter = create_test_hub()

    hub.sort_vehicles_by_model("Delhi")

    assert hub.hubs["Delhi"] == [scooter, car]


def test_sort_fleet_by_battery_returns_descending_order():
    hub = Hub()
    car = ElectricCars("C001", "BMW i4", 80, 4)
    scooter = ElectricScooter("S001", "Ather 450X", 95, 100)

    hub.add_vehicle("Delhi", car)
    hub.add_vehicle("Mumbai", scooter)

    assert hub.sort_fleet_by_battery() == [scooter, car]
