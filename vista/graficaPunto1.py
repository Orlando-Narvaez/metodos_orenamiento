import matplotlib.pyplot as plt

class Grafica:
    @staticmethod
    def generar_grafica(tiempos_ejecucion, metodos):

        fig, ax = plt.subplots(1, 2, figsize=(14, 6))

        ax[0].pie(tiempos_ejecucion, labels=metodos, autopct='%1.1f%%', startangle=140)
        ax[0].axis('equal')
        ax[0].set_title('Proporción del Tiempo de Ejecución por Método de Ordenamiento')

        ax[1].barh(range(len(metodos)), tiempos_ejecucion, color='maroon')
        ax[1].set_yticks(range(len(metodos)))
        ax[1].set_yticklabels(metodos)
        ax[1].set_xlabel('Tiempo de Ejecución (ns)')
        ax[1].set_title('Tiempo de Ejecución por Método de Ordenamiento')

        plt.show()
