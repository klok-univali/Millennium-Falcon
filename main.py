from Drone import Drone
from voo.Decolar import Decolar
from voo.Voo import Voo
from voo.Pousar import Pousar
from voo.EspacoAereo import EspacoAereo

import math

import kloklibs.klibmov
k = kloklibs.klibmov

espaco = EspacoAereo()
droneKA = Drone("Millenium Falcon")

decola = Decolar()

decola.verificarAbastecimento(droneKA, espaco)

decola.configurar(droneKA, espaco)
decola.iniciar(droneKA, espaco, 80.0)

voo = Voo()
voo.iniciar(droneKA, espaco)

pousa = Pousar()
pousa.iniciar(droneKA, espaco)


