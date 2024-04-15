import matplotlib.pyplot as plt

class Grafica:
    @staticmethod
    def generar_grafica(tiempos_ejecucion):
        # Métodos de ordenamiento disponibles
        metodos = list(range(1, len(tiempos_ejecucion) + 1))

        # Generar la gráfica
        plt.bar(metodos, tiempos_ejecucion, color='maroon')
        plt.xlabel('Método de Ordenamiento')
        plt.ylabel('Tiempo de Ejecución (ns)')
        plt.title('Tiempo de Ejecución por Método de Ordenamiento')
        plt.xticks(metodos, tiempos_ejecucion)  # Corrección aquí
        plt.show()