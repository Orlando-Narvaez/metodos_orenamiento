from .nodoEntero import NodoEntero

class ColaEnlazada:
    def __init__(self):
        self.inicio = None
        self.fin = None
        self.tamano = 0

    def encolar(self, num):
        self.tamano += 1
        temp = NodoEntero(num)
        if self.inicio is None:
            self.inicio = temp
            self.fin = self.inicio
        else:
            self.fin.siguiente = temp
            self.fin = temp

    def decolar(self):
        self.tamano -= 1
        temp = self.inicio.valor
        nodo_temp = self.inicio
        self.inicio = self.inicio.siguiente
        nodo_temp = None
        return temp

    def esta_vacia(self):
        return self.tamano == 0