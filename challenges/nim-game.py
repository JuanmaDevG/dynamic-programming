# p004.py

from typing import Dict


class P004:
    '''
     Autor: Juan R. Rico
     
     Descripción: P004 es una solución propuesta al juego del Nim para 2 jugadores con N fichas totales 
     y M a retirar por jugada. El programa devuelve la primera jugada ganadora, o bien, -1 en 
     caso de no tener estrategia ganadora.
     
     Está resulto por:
       - programación dinámica (PD) recursiva (pura);
       - PD con almacén (memoization); 
       - PD iterativa.
     
     
     Advertencia: Este código contiene algún error para que el alumno lo rectifique y pueda probarlo 
     en el sistema de corrección de problemas de la asignatura llamado pyvaluador 
     (http://pyvaluador.dlsi.ua.es/) el usuario y la contraseña es el mismo que el usado en los
     servicios de UACloud. Este sistema automático testea el programa con una batería de test y 
     devuelve el porcentaje de tests superador correctamente.
    '''

    def __init__(self):
        self.N = 0      # Número total de fichas
        self.M = 0      # Máximo número de fichas a retirar por jugada
        self.A: Dict[int, int] = {}  # Almacenamiento para memoization

    def init(self, data: str):
        """Inicializa los valores desde una cadena de entrada."""
        tokens = data.split()
        self.N = int(tokens[0])  # Fichas totales
        self.M = int(tokens[1])  # Máximo a retirar
        self.A = {}  # Reiniciar almacenamiento

    def pdr(self, n: int) -> int:
        """
        Programación dinámica recursiva pura.
        Encuentra la primera jugada ganadora si existe.

        NOTA:
            Asumiendo que tengo el primer turno, una jugada buena para mi, es en la que mi
            opnente me deveulva -1, para ganar yo.
            Habiendo mas de una jugada buena, devuelvo la primera.

            Esta recursion hace que el oponente también nos busque la ruina, y aun con esas
            podamos elegir la jugada en la que pierde.

            Por eso, si me quedo sin fichas en la mesa, devuelvo -1, porque asumo que he
            perdido.
        """
        if n <= 0:
            return -1

        for k in range(1, min(n, self.M) + 1):
            if self.pdr(n - k) < 0:
                return k
        return -1

    def pdr_a(self, n: int) -> int:
        """
        Programación dinámica recursiva con memoization.
        """
        if n <= 0:
            return -1

        if n in self.A:
            return self.A[n]

        res = -1
        for k in range(1, min(n, self.M) + 1):
            if self.pdr_a(n - k) < 0:
                res = k
                break

        self.A[n] = res
        return res

    def pdi(self, n: int) -> int:
        """
        Programación dinámica iterativa.
        """
        A = {0: -1}

        for i in range(1, n + 1):
            res = -1
            for k in range(1, min(i, self.M) + 1):
                if A[i - k] < 0:
                    res = k
                    break
            A[i] = res

        return A[n]

    def best(self, s: str) -> int:
        """
        Método principal: recibe una cadena e invoca al método elegido.
        Por defecto, hay que usar un método: recursivo (pdr), recursivo con almacén (pdr_a) o iterativo (pdi).
        """
        self.init(s)
        #return self.pdr(self.N)
        #return self.pdr_a(self.N)
        return self.pdi(self.N)


# Prueba desde línea de comandos
if __name__ == "__main__":
    p = P004()
    data = "8 4" # Salida: 3
    print(f'data: {data} best:', p.best(data))

    data = "5 4" #Salida: -1
    print(f'data: {data} best:', p.best(data))


