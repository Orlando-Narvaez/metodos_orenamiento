import random

class GenerarArchivos:
    @staticmethod
    def generar_arreglo_1000():
        # Generar un arreglo con 1000 números enteros aleatorios de 8 dígitos
        arreglo = [random.randint(10000000, 99999999) for _ in range(1000)]
        # Escribir el arreglo en un archivo txt llamado "arreglo1.txt"
        with open("archivos/arreglo1.txt", "w") as f:
            for num in arreglo:
                f.write(str(num) + "\n")

    @staticmethod
    def generar_arreglo_10000():
        # Generar un arreglo con 10000 números enteros aleatorios de 8 dígitos
        arreglo = [random.randint(10000000, 99999999) for _ in range(10000)]
        # Escribir el arreglo en un archivo txt llamado "arreglo2.txt"
        with open("archivos/arreglo2.txt", "w") as f:
            for num in arreglo:
                f.write(str(num) + "\n")