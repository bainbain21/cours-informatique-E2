class Airplane :
    
    def __init__(self, name : str):
        self.fly = False
        self.name = name

    def take_off(self):
        self.fly = True
        return f"{self.name} take off"

    def land(self):
        self.fly = False
        return f"{self.name} land"

    def __str__(self):
        status = "flying" if self.fly else "grounding"
        return f"avion : {self.name} - status : {status}"

class MilitaryAircraft(Airplane):

    def __init__(self, name : str, mission : str = "no mission"):
        super().__init__(name)
        self.mission = mission

    def __str__(self):
        return f"Military Aircraft {super().__str__()} - {self.mission}"

class CargoAircraft(Airplane):

    def __init__(self, name : str, shipment :str = "no shipment"):
        super().__init__(name)
        self.shipment = shipment

    def __str__(self):
        return f"Cargo Aircraft {super().__str__()} - {self.shipment}"

class CivilAircraft(Airplane):

    def __init__(self, name : str, passenger : int = 0):
        super().__init__(name)
        self.passenger = passenger

    def passengers_enter(self, nb : int):
        self.passenger+= nb
        return f"{nb} passengers onboarded {self.name}"

    def passengers_leave(self, nb : int):
        if self.passenger>= nb:
            self.passenger -= nb
            return f"{nb} passengers leaved {self.name}"
        else :
            return f"there is not this many passengers on board"

    def __str__(self):
        return f"Civil Aircraft {super().__str__()} - {self.passenger} passengers"

class Airport :

    def __init__(self):
        self.militaryPlanes = []
        self.cargoPlanes = []
        self.civilPlanes = []

    def add_military(self, plane):
        self.militaryPlanes.append(plane)

    def add_cargo(self, plane):
        self.cargoPlanes.append(plane)

    def add_civil(self, plane):
        self.civilPlanes.append(plane)

    def __str__(self):
        result = "Airport\n"
        result += ("\n".join(str(p) for p in self.militaryPlanes) or "None") + "\n"
        result += ("\n".join(str(p) for p in self.cargoPlanes) or "None") + "\n"
        result += ("\n".join(str(p) for p in self.civilPlanes) or "None")
        return result

