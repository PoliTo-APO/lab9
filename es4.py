class RentalException(Exception):
    pass


class VehicleException(RentalException):
    pass


class VehicleUnavailableException(VehicleException):
    pass


class VehicleMissingException(VehicleException):
    pass


class LicenceException(RentalException):
    pass


class LicenceMissingException(LicenceException):
    pass


class LicenceCategoryException(LicenceException):
    pass


class Licence:
    def __init__(self, name: str, categories: set[str]):
        self._name = name
        self._categories = categories

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def categories(self) -> set[str]:
        return self._categories
    

class Vehicle:
    def __init__(self, plate: str, category: str):
        self._plate = plate
        self._category = category

    @property
    def plate(self) -> str:
        return self._plate
    
    @property
    def category(self) -> str:
        return self._category
    

class VehicleRental:
    def __init__(self):
        self._vehicles = {}
        self._licenses = {}
        self._rented = set()

    def add_vehicle(self, vehicle) -> None:
        self._vehicles[vehicle.plate] = vehicle

    def add_licence(self, licence) -> None:
        self._licenses[licence.name] = licence
        print(licence.categories)

    def rent_vehicle(self, plate, name) -> None:
        if plate not in self._vehicles:
            raise VehicleMissingException("Vehicle with plate {} not preset".format(plate))
        if name not in self._licenses:
            raise LicenceMissingException("Licence for {} not uploaded".format(name))
        if plate in self._rented:
            raise VehicleUnavailableException("Vehicle with plate {} is not available".format(plate))        
        vehicle = self._vehicles[plate]
        licence = self._licenses[name]
        if vehicle.category not in licence.categories:
            raise LicenceCategoryException("Licence category {} required".format(vehicle.category))
        self._rented.add(plate)
        

def rent_vehicle_check(rental, plate, name):
    try:
        rental.rent_vehicle(plate, name)
        print("vehicle rented")
    except LicenceMissingException as e:
        print(str(e))
    except LicenceCategoryException as e:
        print(str(e))
    except VehicleException:
        print("problem with vehicle")


def main():
    rental = VehicleRental()
    rental.add_licence(Licence("Marco", {"A", "B"}))
    rental.add_licence(Licence("Simone", {"B", "C"}))
    
    rental.add_vehicle(Vehicle("A1234", "A"))
    rental.add_vehicle(Vehicle("B1234", "B"))
    rental.add_vehicle(Vehicle("C1234", "C"))

    rent_vehicle_check(rental, "B1234", "Simone")   # noleggio ok
    rent_vehicle_check(rental, "C1234" , "Marco")   # categoria sbagliata
    rent_vehicle_check(rental, "A1234", "Gianluca") # pantente non vehicleicata
    rent_vehicle_check(rental, "D1234", "Simone")   # auto non esiste
    rent_vehicle_check(rental, "B1234", "Marco")    # auto non disponibile


if __name__ == "__main__":
    main()
    