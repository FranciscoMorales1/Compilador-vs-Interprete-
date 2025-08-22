import pandas as pd
import matplotlib.pyplot as plt
import os

# Obtener el directorio donde está este script
directorio_script = os.path.dirname(os.path.abspath(__file__))

# Construir las rutas completas a los archivos CSV
ruta_rec_py = os.path.join(directorio_script, "factorial_recursivo_python.csv")
ruta_ite_py = os.path.join(directorio_script, "factorial_iterativo_python.csv")
ruta_rec_c = os.path.join(directorio_script, "factorial_recursivo_c.csv")
ruta_ite_c = os.path.join(directorio_script, "factorial_iterativo_c.csv")

# Verificar que los archivos existen
archivos = [ruta_rec_py, ruta_ite_py, ruta_rec_c, ruta_ite_c]
for archivo in archivos:
    if not os.path.exists(archivo):
        print(f"ERROR: No se encuentra el archivo {archivo}")
        exit(1)
    else:
        print(f"✓ Encontrado: {os.path.basename(archivo)}")

# Cargar CSVs
rec_py = pd.read_csv(ruta_rec_py)
ite_py = pd.read_csv(ruta_ite_py)
rec_c = pd.read_csv(ruta_rec_c)
ite_c = pd.read_csv(ruta_ite_c)

# Graficas de comparación
def comparar(metric, titulo, py, c, nombre):
    plt.figure()
    plt.plot(py["n"], py[metric], label="Python (interpretado)")
    plt.plot(c["n"], c[metric], label="C (compilado)")
    plt.xlabel("n")
    plt.ylabel(metric)
    plt.title(titulo)
    plt.legend()
    
    # Guardar en el mismo directorio del script
    ruta_imagen = os.path.join(directorio_script, nombre)
    plt.savefig(ruta_imagen)
    print(f"✓ Gráfica guardada: {nombre}")

# 4 comparaciones
comparar("tiempo", "Factorial recursivo - Tiempo", rec_py, rec_c, "recursivo_tiempo.png")
comparar("memoria", "Factorial recursivo - Memoria", rec_py, rec_c, "recursivo_memoria.png")
comparar("tiempo", "Factorial iterativo - Tiempo", ite_py, ite_c, "iterativo_tiempo.png")
comparar("memoria", "Factorial iterativo - Memoria", ite_py, ite_c, "iterativo_memoria.png")

print("Gráficas generadas exitosamente.")
