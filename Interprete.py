import time
import tracemalloc
import csv
import os

# Factorial recursivo
def factorial_recursivo(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursivo(n-1)

# Factorial iterativo
def factorial_iterativo(n):
    resultado = 1
    for i in range(2, n+1):
        resultado *= i
    return resultado

def medir(funcion, n):
    tracemalloc.start()
    inicio = time.perf_counter()
    funcion(n)
    fin = time.perf_counter()
    memoria = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    return fin - inicio, memoria

def generar_csv(nombre, funcion):
    # Obtener la ruta completa del directorio donde está el script
    directorio_script = os.path.dirname(os.path.abspath(__file__))
    ruta_completa = os.path.join(directorio_script, nombre)
    
    with open(ruta_completa, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["n", "tiempo", "memoria"])
        for n in range(1, 500):  # rango ajustable
            t, m = medir(funcion, n)
            writer.writerow([n, t, m])
        f.flush()  # Forzar escritura inmediata
    
    # Verificar que el archivo se creó
    if os.path.exists(ruta_completa):
        print(f"✓ Archivo {nombre} creado en: {ruta_completa}")
    else:
        print(f"✗ Error: No se pudo crear {nombre}")

if __name__ == "__main__":
    print(f"Directorio de trabajo: {os.getcwd()}")
    print(f"Directorio del script: {os.path.dirname(os.path.abspath(__file__))}")
    
    generar_csv("factorial_recursivo_python.csv", factorial_recursivo)
    generar_csv("factorial_iterativo_python.csv", factorial_iterativo)

