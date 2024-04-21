from metodos1 import comb_sort, tim_sort, tree_sort, pigeonhole_sort, heap_sort, bitonic_sort, gnome_sort
from metodos1.tim_sort import Ordenamiento as TimSort
from metodos1.comb_sort import Ordenamiento as CombSort
from metodos1.tree_sort import Ordenamiento as TreeSort
from metodos1.pigeonhole_sort import Ordenamiento as PigeonholeSort
from metodos1.heap_sort import Ordenamiento as HeapSort
from metodos1.bitonic_sort import Ordenamiento as BitonicSort
from metodos1.gnome_sort import Ordenamiento as GnomeSort
from metodos2.radix1.radixSort1 import RadixSort1
from metodos2.radix2.radixSort2 import RadixSort2
from archivos import generar_archivos
from metodos2.radix1 import radixSort1
from metodos2.radix2 import radixSort2
from vista.graficaPunto1 import Grafica as Grafica1
import time
import tkinter as tk

def case_1(mientra, ordenador_tim):
    inicio = time.time()
    ordenador_tim.tim_sort(mientra)
    fin = time.time()
    tiempo_transcurrido = fin - inicio
    print("Tiempo transcurrido:", tiempo_transcurrido, "segundos")
    print("---------------------------------------\n")
    return tiempo_transcurrido

def case_2(mientra, ordenador_comb):
    inicio = time.time()
    ordenador_comb.comb_sort(mientra)
    fin = time.time()
    tiempo_transcurrido = fin - inicio
    print("Tiempo transcurrido:", tiempo_transcurrido, "segundos")
    print("---------------------------------------\n")
    return tiempo_transcurrido

def case_3(mientra, ordenador_tree):
    inicio = time.time()
    ordenador_tree.tree_sort(mientra)
    fin = time.time()
    tiempo_transcurrido = fin - inicio
    print("Tiempo transcurrido:", tiempo_transcurrido, "segundos")
    print("---------------------------------------\n")
    return tiempo_transcurrido

def case_4(mientra, ordenador_pigeonhole):
    inicio = time.time()
    ordenador_pigeonhole.pigeonhole_sort(mientra)
    fin = time.time()
    tiempo_transcurrido = fin - inicio
    print("Tiempo transcurrido:", tiempo_transcurrido, "segundos")
    print("---------------------------------------\n")
    return tiempo_transcurrido

def case_5(mientra, ordenador_heap):
    inicio = time.time()
    ordenador_heap.sort(mientra)
    fin = time.time()
    tiempo_transcurrido = fin - inicio
    print("Tiempo transcurrido:", tiempo_transcurrido, "segundos")
    print("---------------------------------------\n")
    return tiempo_transcurrido

def case_6(mientra, ordenador_bitonic):
    inicio = time.time()
    ordenador_bitonic.sort(mientra, 1)
    fin = time.time()
    tiempo_transcurrido = fin - inicio
    print("Tiempo transcurrido:", tiempo_transcurrido, "segundos")
    print("---------------------------------------\n")
    return tiempo_transcurrido

def case_7(mientra, ordenador_gnome):
    inicio = time.time()
    ordenador_gnome.gnome_sort(mientra)
    fin = time.time()
    tiempo_transcurrido = fin - inicio
    print("Tiempo transcurrido:", tiempo_transcurrido, "segundos")
    print("---------------------------------------\n")
    return tiempo_transcurrido

def case_radix_sort(mientra, metodo):
    inicio = time.time() 
    metodo(mientra)
    fin = time.time() 
    tiempo_transcurrido = fin - inicio  
    print("Tiempo transcurrido:", tiempo_transcurrido, "segundos") 
    print("---------------------------------------\n")
    return tiempo_transcurrido


def case_radix_sort2(mientra, metodo):
    inicio = time.time() 
    metodo(RadixSort2(), mientra)  # Pasar el arreglo como argumento
    fin = time.time() 
    tiempo_transcurrido = fin - inicio  
    print("Tiempo transcurrido:", tiempo_transcurrido, "segundos") 
    print("---------------------------------------\n")
    return tiempo_transcurrido


def obtenerArreglo(i, arreglo1, arreglo2):
    if i > 0:
        return arreglo1.copy()
    
    return arreglo2.copy()

def punto1():
    # Leer los arreglos de los archivos generados
    arregloNum1 = []
    with open("archivos/arreglo1", 'r') as archivo:
        for linea in archivo:
            valor = int(linea.strip())
            arregloNum1.append(valor)

    arreglo2 = []
    with open("archivos/arreglo2") as f:
        arreglo2 = [int(line.strip()) for line in f]

    # Métodos de ordenamiento
    metodos_ordenamiento = {
        "Tim Sort": tim_sort.Ordenamiento.tim_sort,
        "Comb Sort": comb_sort.Ordenamiento.comb_sort,
        "Tree Sort": tree_sort.Ordenamiento.tree_sort,
        "Pigeonhole Sort": pigeonhole_sort.Ordenamiento.pigeonhole_sort,
        "Heap Sort": heap_sort.Ordenamiento.sort,
        "Bitonic Sort": bitonic_sort.Ordenamiento.sort,
        "Gnome Sort": gnome_sort.Ordenamiento.gnome_sort
    }

    # Ordenar y mostrar resultados para el arreglo1
    print("Arreglo1 (1000 elementos):\n")
    tiempos_ejecucion = []
    for nombre_metodo, metodo in metodos_ordenamiento.items():
        tiempo = 0
        for i in range(2):
            ordenador_tim = TimSort()
            ordenador_comb = CombSort()
            ordenador_tree = TreeSort()
            ordenador_pigeonhole = PigeonholeSort()
            ordenador_heap = HeapSort()
            ordenador_bitonic = BitonicSort()
            ordenador_gnome = GnomeSort()
            mientra = obtenerArreglo(i, arregloNum1, arreglo2)
            print(f"Método: {nombre_metodo}")
            if nombre_metodo == "Tim Sort":
                 tiempo += case_1(mientra, ordenador_tim)
            if nombre_metodo =="Comb Sort":
                tiempo += case_2(mientra, ordenador_comb)
            if nombre_metodo == "Tree Sort":
                tiempo += case_3(mientra, ordenador_tree)
            if nombre_metodo == "Pigeonhole Sort":
                tiempo += case_4(mientra, ordenador_pigeonhole)
            if nombre_metodo == "Heap Sort":
                tiempo += case_5(mientra, ordenador_heap)
            if nombre_metodo == "Bitonic Sort":
                tiempo += case_6(mientra, ordenador_bitonic)
            if nombre_metodo == "Gnome Sort":
                tiempo += case_7(mientra, ordenador_gnome)
        
        tiempos_ejecucion.append(tiempo/2)
    print(tiempos_ejecucion)

    #tiempos_ejecucion.sort()
    tiempos_ordenados, metodos_ordenados = zip(*sorted(zip(tiempos_ejecucion, metodos_ordenamiento.keys())))

    graficaTorta = Grafica1()

    # Generar la gráfica de torta con leyenda
    graficaTorta.generar_grafica(tiempos_ordenados, metodos_ordenados)

def punto2():
    # Leer los arreglos de los archivos generados
    arregloNum1 = []
    with open("archivos/arreglo1", 'r') as archivo:
        for linea in archivo:
            valor = int(linea.strip())
            arregloNum1.append(valor)

    arreglo2 = []
    with open("archivos/arreglo2") as f:
        arreglo2 = [int(line.strip()) for line in f]

    # Métodos de ordenamiento
    metodos_ordenamiento2 = {
        "Radix Sort 1": radixSort1.RadixSort1.radixSort,
        "Radix Sort 2": radixSort2.RadixSort2.sort_arreglo
    }

    tiempos_ejecucion = []
    for nombre_metodo, metodo in metodos_ordenamiento2.items():
        tiempo = 0
        for i in range(2):
            mientra = obtenerArreglo(i, arregloNum1, arreglo2)
            print(f"Método: {nombre_metodo}")
            if nombre_metodo == "Radix Sort 1":
                 tiempo += case_radix_sort(mientra, metodo)
            if nombre_metodo == "Radix Sort 2":
                    tiempo += case_radix_sort2(mientra, metodo)
        tiempos_ejecucion.append(tiempo/2)
    print(tiempos_ejecucion)

    #tiempos_ejecucion.sort()
    tiempos_ordenados, metodos_ordenados = zip(*sorted(zip(tiempos_ejecucion, metodos_ordenamiento2.keys())))

    graficaTorta = Grafica1()

    # Generar la gráfica de torta con leyenda
    graficaTorta.generar_grafica(tiempos_ordenados, metodos_ordenados)

if __name__ == "__main__":
    # Generar los archivos con arreglos de 1000 y 10000 números aleatorios
    generar_archivos.GenerarArchivos.generar_arreglo_1000()
    generar_archivos.GenerarArchivos.generar_arreglo_10000()

    ventana_principal = tk.Tk()
    ventana_principal.title("Ejemplo de Pantallas")

    boton_punto1 = tk.Button(ventana_principal, text="Punto 1 del taller", command=punto1)
    boton_punto1.pack(pady=10)

    boton_punto2 = tk.Button(ventana_principal, text="Punto 2 del taller", command=punto2)
    boton_punto2.pack(pady=10)

    ventana_principal.mainloop()