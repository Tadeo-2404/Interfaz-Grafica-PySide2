from Vuelo import Vuelo

class Aeropuerto:
    def __init__(self):
        self.__vuelos = []

    def agregar_final(self, vuelo:Vuelo):
        self.__vuelos.append(vuelo)

    def agregar_inicio(self, vuelo:Vuelo):
        self.__vuelos.insert(0, vuelo)

    def mostrar(self):
        for v in self.__vuelos:
            print(v)

    def __str__(self):
        return "".join(
            str(vuelo) + "\n" for vuelo in self.__vuelos
        )

# vuelo1 = Vuelo(id="0", origen="TORREON", destino="CDMX", peso=30)
# vuelo2 = Vuelo(id="1", origen="CDMX", destino="MTY", peso=30)
# aeropuerto = Aeropuerto()
# aeropuerto.agregar_final(vuelo1)
# aeropuerto.agregar_inicio(vuelo2)
# aeropuerto.mostrar()