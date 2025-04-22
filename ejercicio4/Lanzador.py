from polinomio import Polinomio
class Lanzador:
    def ejecutar(self):
        p1 = Polinomio({3: 4, 2: 3, 0: -5})  # 4x^3 + 3x^2 - 5
        p2 = Polinomio({1: 2, 0: 1})         # 2x + 1

        print("Polinomio 1:", p1)
        print("Polinomio 2:", p2)

        print("\nRestar Polinomios:")
        resta = p1.restar(p2)
        print("Resultado:", resta)

        print("\nDividir Polinomios:")
        try:
            division = p1.dividir(p2)
            print("Resultado:", division)
        except ValueError as e:
            print("Error:", e)

        print("\nEliminar término (x^2) del Polinomio 1:")
        p1.eliminar_termino(2)
        print("Polinomio 1 después de eliminar término:", p1)

        print("\nVerificar si existe el término (x^3) en Polinomio 1:")
        existe = p1.existe_termino(3)
        print("¿Existe x^3 en Polinomio 1?:", existe)
