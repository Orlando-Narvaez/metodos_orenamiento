import matplotlib.pyplot as plt

class Grafica:
    @staticmethod
    def generar_grafica(tiempos_ejecucion, metodos):

        # Generar la gráfica de torta con leyenda
        fig, ax = plt.subplots(1, 2, figsize=(14, 6))

        # Grafica de torta
        ax[0].pie(tiempos_ejecucion, labels=metodos, autopct='%1.1f%%', startangle=140)
        ax[0].axis('equal')
        ax[0].set_title('Proporción del Tiempo de Ejecución por Método de Ordenamiento')

        # Lista de métodos
        ax[1].barh(range(len(metodos)), tiempos_ejecucion, color='maroon')
        ax[1].set_yticks(range(len(metodos)))
        ax[1].set_yticklabels(metodos)
        ax[1].set_xlabel('Tiempo de Ejecución (ns)')
        ax[1].set_title('Tiempo de Ejecución por Método de Ordenamiento')

        plt.show()
        """
        # Métodos de ordenamiento disponibles
        metodos = list(range(1, len(tiempos_ejecucion) + 1))

        # Generar la gráfica
        plt.pie(tiempos_ejecucion, labels=metodos, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')  # Asegura que el gráfico sea un círculo en lugar de una elipse
        plt.title('Proporción del Tiempo de Ejecución por Método de Ordenamiento')
        plt.show()"""
