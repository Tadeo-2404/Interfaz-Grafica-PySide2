class Vuelo:
    def __init__(self, id="", origen="", destino="", peso=0):
        self.__id = id
        self.__origen = origen
        self.__destino = destino
        self.__peso = peso
    
    def __str__(self):
        return (
            "ID: " + self.__id + "\n" +
            "Origen: " + self.__origen + "\n" +
            "Destino: " + self.__destino + "\n" +
            "Peso: " + str(self.__peso) + "\n" 
        )

vuelo1 = Vuelo(id="0", origen="TORREON", destino="CDMX", peso=30)
print(vuelo1) #Direccion de memoria del obejto
vuelo2 = Vuelo(id="1", origen="CDMX", destino="MTY", peso=30)
print(vuelo2) 