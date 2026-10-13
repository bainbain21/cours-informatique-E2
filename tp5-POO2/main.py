from Rport import *

Aeroport = Airport()

sabre = MilitaryAircraft("F86 Sabre")
beluga = CargoAircraft("Beluga")
a320 = CivilAircraft("A320")

Aeroport.add_military(sabre)
Aeroport.add_cargo(beluga)
Aeroport.add_civil(a320)

a320.passengers_enter(150)
a320.take_off()

euf = MilitaryAircraft("EuroFighter Typhoon","hostages rescue")
euf.take_off()

Aeroport.add_military(euf)

print(Aeroport)

