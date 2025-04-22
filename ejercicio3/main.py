
from NaveEspacial import NaveEspacial
from Lanzador import Lanzador

if __name__ == "__main__":
    naves = [
        NaveEspacial("Cometa Veloz", 50, 10, 20),
        NaveEspacial("Titán del Cosmos", 100, 15, 50),
        NaveEspacial("GX-1", 70, 8, 6),
        NaveEspacial("GX-2", 60, 12, 10),
        NaveEspacial("Estrella Fugaz", 40, 5, 4),
        NaveEspacial("Nebulosa", 90, 20, 30),
    ]

    lanzador = Lanzador(naves)

    print("Ordenando naves por nombre ascendente y longitud descendente:")
    lanzador.ordenar_por_nombre_y_longitud()
    for nave in naves:
        print(nave)

    print("\nInformación de las naves 'Cometa Veloz' y 'Titán del Cosmos':")
    lanzador.mostrar_informacion_naves(["Cometa Veloz", "Titán del Cosmos"])

    print("\nCinco naves con mayor cantidad de pasajeros:")
    lanzador.cinco_mayor_pasajeros()

    print("\nNave que requiere mayor cantidad de tripulación:")
    lanzador.nave_mayor_tripulacion()

    print("\nNaves cuyo nombre comienza con 'GX':")
    lanzador.naves_comienzan_con("GX")

    print("\nNaves que pueden llevar seis o más pasajeros:")
    lanzador.naves_con_seis_o_mas_pasajeros()

    print("\nNave más pequeña y más grande:")
    lanzador.nave_mas_pequena_y_grande()