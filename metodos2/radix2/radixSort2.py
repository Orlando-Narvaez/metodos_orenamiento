from .colaEnlazada import ColaEnlazada

class RadixSort2:
    def __init__(self):
        self.Q = [ColaEnlazada() for _ in range(10)]

    def obtener_radical(self, numero, radical):
        return (numero // (10 ** (radical - 1))) % 10

    def sort(self, a, numero_digitos):
        for i in range(1, numero_digitos):
            pos_arreglo = 0
            for j in range(len(a)):
                self.Q[self.obtener_radical(a[j], i)].encolar(a[j])
            for j in range(len(self.Q)):
                while not self.Q[j].esta_vacia():
                    a[pos_arreglo] = self.Q[j].decolar()
                    pos_arreglo += 1

    def sort_arreglo(self, a):
        maximo = max(a)
        numero_digitos = len(str(maximo))
        self.sort(a, numero_digitos)