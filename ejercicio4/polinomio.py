class Polinomio:
    def __init__(self, terminos=None):
        # terminos es un diccionario donde la clave es el exponente y el valor es el coeficiente
        self.terminos = terminos if terminos else {}

    def restar(self, otro):
        resultado = Polinomio(self.terminos.copy())
        for exponente, coeficiente in otro.terminos.items():
            if exponente in resultado.terminos:
                resultado.terminos[exponente] -= coeficiente
                if resultado.terminos[exponente] == 0:
                    del resultado.terminos[exponente]
            else:
                resultado.terminos[exponente] = -coeficiente
        return resultado

    def dividir(self, otro):
        if not otro.terminos:
            raise ValueError("No se puede dividir por un polinomio vacío.")
        resultado = Polinomio()
        dividendo = Polinomio(self.terminos.copy())
        while dividendo.terminos and max(dividendo.terminos) >= max(otro.terminos):
            exp_dividendo = max(dividendo.terminos)
            exp_divisor = max(otro.terminos)
            coef_dividendo = dividendo.terminos[exp_dividendo]
            coef_divisor = otro.terminos[exp_divisor]
            nuevo_exp = exp_dividendo - exp_divisor
            nuevo_coef = coef_dividendo / coef_divisor
            resultado.terminos[nuevo_exp] = nuevo_coef
            subtrahendo = Polinomio({nuevo_exp: nuevo_coef}).multiplicar(otro)
            dividendo = dividendo.restar(subtrahendo)
        return resultado

    def eliminar_termino(self, exponente):
        if exponente in self.terminos:
            del self.terminos[exponente]

    def existe_termino(self, exponente):
        return exponente in self.terminos

    def multiplicar(self, otro):
        resultado = Polinomio()
        for exp1, coef1 in self.terminos.items():
            for exp2, coef2 in otro.terminos.items():
                nuevo_exp = exp1 + exp2
                nuevo_coef = coef1 * coef2
                if nuevo_exp in resultado.terminos:
                    resultado.terminos[nuevo_exp] += nuevo_coef
                else:
                    resultado.terminos[nuevo_exp] = nuevo_coef
        return resultado

    def __str__(self):
        if not self.terminos:
            return "0"
        terminos_str = []
        for exponente, coeficiente in sorted(self.terminos.items(), reverse=True):
            if exponente == 0:
                terminos_str.append(f"{coeficiente}")
            elif exponente == 1:
                terminos_str.append(f"{coeficiente}x")
            else:
                terminos_str.append(f"{coeficiente}x^{exponente}")
        return " + ".join(terminos_str).replace("+ -", "- ")