class Matriz:
    def __init__(self, matriz):
        if len(matriz) != 3 or any(len(fila) != 3 for fila in matriz):
            raise ValueError("La matriz debe ser cuadrada de 3x3.")
        self.matriz = matriz

    def determinante_recursivo(self, matriz=None):
        if matriz is None:
            matriz = self.matriz
        
        if len(matriz) == 2:  # Caso base: matriz 2x2
            return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
        
        determinante = 0
        for i in range(len(matriz)):
            submatriz = [fila[:i] + fila[i+1:] for fila in matriz[1:]]
            signo = (-1) ** i
            determinante += signo * matriz[0][i] * self.determinante_recursivo(submatriz)
        return determinante

    def determinante_iterativo(self):
        a, b, c = self.matriz[0]
        d, e, f = self.matriz[1]
        g, h, i = self.matriz[2]
        
        return (a * (e * i - f * h) -
                b * (d * i - f * g) +
                c * (d * h - e * g))


def main():
    # Ejemplo de uso
    matriz = [
        [2, 4, 3],
        [1, 5, 7],
        [6, 8, 9]
    ]
    
    matriz_obj = Matriz(matriz)
    
    print("Determinante (recursivo):", matriz_obj.determinante_recursivo())
    print("Determinante (iterativo):", matriz_obj.determinante_iterativo())


if __name__ == "__main__":
    main()