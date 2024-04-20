import matplotlib.pyplot as plt

class Graficas:
    @staticmethod
    def generar_graficas(tiempos_ejecucion_barras, tiempos_ejecucion_torta):
        # Métodos de ordenamiento disponibles
        metodos = list(range(1, len(tiempos_ejecucion_barras) + 1))

        # Generar la gráfica de barras
        plt.subplot(1, 2, 1)
        plt.bar(metodos, tiempos_ejecucion_barras, color='maroon')
        plt.xlabel('Método de Ordenamiento')
        plt.ylabel('Tiempo de Ejecución (ns)')
        plt.title('Tiempo de Ejecución por Método de Ordenamiento (Barras)')
        plt.xticks(metodos, tiempos_ejecucion_barras)  # Corrección aquí

        # Generar la gráfica de torta
        plt.subplot(1, 2, 2)
        plt.pie(tiempos_ejecucion_torta, labels=metodos, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')  # Asegura que el gráfico sea un círculo en lugar de una elipse
        plt.title('Proporción del Tiempo de Ejecución por Método de Ordenamiento (Torta)')

        plt.tight_layout()  # Ajusta los espacios entre las gráficas para que no se superpongan
        plt.show()