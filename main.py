from ElectricScooter import ElectricScooter
from ElectricCars import ElectricCars
from Vehicle import Vehicles
from fleetHub import Hub









if __name__ == "__main__" :
    
    hub_manager = Hub()

    ather = ElectricScooter(123,"ather",90,100)
    ola = ElectricScooter(124,"ola",80,100)
    car = ElectricCars(125,"bmw",90,4)
    hub_manager.add_vehicle("Delhi", ather)
    hub_manager.add_vehicle("Mumbai", ola)
    hub_manager.add_vehicle("Delhi", car)

    hub_manager.display_hubs()
    
