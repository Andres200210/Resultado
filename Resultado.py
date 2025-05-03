class Equipo:
    def __init__(self, Nombre):
        self.nombre = Nombre
        self.partidosGanados = 0
        self.partidosPerdidos = 0
        self.setGanados = 0

    def registra_set(self, equipos, ganador):
        equipos[ganador].setGanados += 1
        if equipos[ganador].setGanados == 3:
            equipos[ganador].partidosGanados += 1
            perdedor = 1 if ganador == 0 else 0
            equipos[perdedor].partidosPerdidos += 1
            equipos[0].setGanados = 0
            equipos[1].setGanados = 0

def jugar_partido(equipos):
    for set_num in range(5):  
        print(f"Set {set_num + 1}")
        puntos1 = int(input(f"Ingrese puntos de {equipos[0].nombre}: "))
        puntos2 = int(input(f"Ingrese puntos de {equipos[1].nombre}: "))

        if puntos1 > puntos2:
            equipos[0].registra_set(equipos, 0)
        else:
            equipos[1].registra_set(equipos, 1)

        if equipos[0].setGanados == 3 or equipos[1].setGanados == 3:
            break

def resultado_torneo(equipos):
    for eq in equipos:
        print(f"\nEquipo: {eq.nombre}")
        print(f"Partidos Ganados: {eq.partidosGanados}")
        print(f"Partidos Perdidos: {eq.partidosPerdidos}")

nombre1 = input("Ingrese el nombre del Equipo 1: ")
nombre2 = input("Ingrese el nombre del Equipo 2: ")
equipo1 = Equipo(nombre1)
equipo2 = Equipo(nombre2)
equipos = [equipo1, equipo2]

partidos = int(input("¿Cuántos partidos deben jugar?: "))

for _ in range(partidos):
    print(f"\n--- Partido {_ + 1} ---")
    jugar_partido(equipos)

resultado_torneo(equipos)

