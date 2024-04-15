import matplotlib.pyplot as plt

class Grafica:
    @staticmethod
    def generar_grafica(tiempos_ejecucion):
        # Métodos de ordenamiento disponibles
        metodos = list(range(1, len(tiempos_ejecucion) + 1))

        # Generar la gráfica
        plt.pie(tiempos_ejecucion, labels=metodos, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')  # Asegura que el gráfico sea un círculo en lugar de una elipse
        plt.title('Proporción del Tiempo de Ejecución por Método de Ordenamiento')
        plt.show()
