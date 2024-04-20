from metodos import comb_sort, tim_sort, tree_sort, pigeonhole_sort, heap_sort, bitonic_sort, gnome_sort
from metodos.tim_sort import Ordenamiento as TimSort
from metodos.comb_sort import Ordenamiento as CombSort
from metodos.tree_sort import Ordenamiento as TreeSort
from metodos.pigeonhole_sort import Ordenamiento as PigeonholeSort
from metodos.heap_sort import Ordenamiento as HeapSort
from metodos.bitonic_sort import Ordenamiento as BitonicSort
from metodos.gnome_sort import Ordenamiento as GnomeSort
from archivos import generar_archivos
from vista.graficaTorta import Grafica as GraficaTorta
from vista.graficaBarras import Grafica as GraficaBarras
import time

def case_1(mientra):
    inicio = time.time_ns()
    ordenador_tim.tim_sort(mientra)
    fin = time.time_ns()
    #print("\nArreglo ordenado:", mientra)
    tiempo_transcurrido = fin - inicio
    print("Tiempo transcurrido:", tiempo_transcurrido, "segundos")
    print("---------------------------------------\n")
    
    return tiempo_transcurrido

def case_2(mientra):
    inicio = time.time_ns()
    ordenador_comb.comb_sort(mientra)
    fin = time.time_ns()
    #print("\nArreglo ordenado:", mientra)
    tiempo_transcurrido = fin - inicio
    print("Tiempo transcurrido:", tiempo_transcurrido, "segundos")
    print("---------------------------------------\n")
 
    return tiempo_transcurrido

def case_3(mientra):
    inicio = time.time_ns()
    ordenador_tree.tree_sort(mientra)
    fin = time.time_ns()
    #print("\nArreglo ordenado:", mientra)
    tiempo_transcurrido = fin - inicio
    print("Tiempo transcurrido:", tiempo_transcurrido, "segundos")
    print("---------------------------------------\n")
    return tiempo_transcurrido

def case_4(mientra):
    inicio = time.time_ns()
    ordenador_pigeonhole.pigeonhole_sort(mientra)
    fin = time.time_ns()
    #print("\nArreglo ordenado:", mientra)
    tiempo_transcurrido = fin - inicio
    print("Tiempo transcurrido:", tiempo_transcurrido, "segundos")
    print("---------------------------------------\n")
    return tiempo_transcurrido

def case_5(mientra):
    inicio = time.time_ns()
    ordenador_heap.sort(mientra)
    fin = time.time_ns()
    #print("\nArreglo ordenado:", mientra)
    tiempo_transcurrido = fin - inicio
    print("Tiempo transcurrido:", tiempo_transcurrido, "segundos")
    print("---------------------------------------\n")
    return tiempo_transcurrido

def case_6(mientra):
    inicio = time.time_ns()
    ordenador_bitonic.sort(mientra, 1)
    fin = time.time_ns()
    #print("\nArreglo ordenado:", mientra)
    tiempo_transcurrido = fin - inicio
    print("Tiempo transcurrido:", tiempo_transcurrido, "segundos")
    print("---------------------------------------\n")
    return tiempo_transcurrido

def case_7(mientra):
    inicio = time.time_ns()
    ordenador_gnome.gnome_sort(mientra)
    fin = time.time_ns()
    #print("\nArreglo ordenado:", mientra)
    tiempo_transcurrido = fin - inicio
    print("Tiempo transcurrido:", tiempo_transcurrido, "segundos")
    print("---------------------------------------\n")
    return tiempo_transcurrido

def obtenerArreglo(i):
    if i > 0:
        return arregloNum1.copy()
    
    return arreglo2.copy()

if __name__ == "__main__":

    # Generar los archivos con arreglos de 1000 y 10000 números aleatorios
    generar_archivos.GenerarArchivos.generar_arreglo_1000()
    generar_archivos.GenerarArchivos.generar_arreglo_10000()

    tiempos_ejecucion = []

    # Leer los arreglos de los archivos generados}
    arregloNum1 = []
    with open("archivos/arreglo1", 'r') as archivo:
        for linea in archivo:
            valor = int(linea.strip())
            arregloNum1.append(valor)
        #arreglo1 = [int(line.strip()) for line in f]
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
            mientra = obtenerArreglo(i)
            print(f"Método: {nombre_metodo}")
            #print("Arreglo original:", arregloNum1)
            if nombre_metodo == "Tim Sort":
                 tiempo += case_1(mientra)
            if nombre_metodo =="Comb Sort":
                tiempo += case_2(mientra)
            if nombre_metodo == "Tree Sort":
                tiempo += case_3(mientra)
            if nombre_metodo == "Pigeonhole Sort":
                tiempo += case_4(mientra)
            if nombre_metodo == "Heap Sort":
                tiempo += case_5(mientra)
            if nombre_metodo == "Bitonic Sort":
                tiempo += case_6(mientra)
            if nombre_metodo == "Gnome Sort":
                tiempo += case_7(mientra)
        
        tiempos_ejecucion.append(tiempo/2)
    print(tiempos_ejecucion)

    #tiempos_ejecucion.sort()
    tiempos_ordenados, metodos_ordenados = zip(*sorted(zip(tiempos_ejecucion, metodos_ordenamiento.keys())))


    graficaTorta = GraficaTorta()


    # Generar la gráfica de torta con leyenda
    graficaTorta.generar_grafica(tiempos_ordenados, metodos_ordenados)
