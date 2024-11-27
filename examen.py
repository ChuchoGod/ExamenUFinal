import csv

def pedir_datos_archivos():
    """Pide al usuario los datos para los archivos A1, A2, A3, cada uno con un solo registro."""
    archivos = ["A1.csv", "A2.csv", "A3.csv"]
    datos_archivos = {}

    for archivo in archivos:
        print(f"\n--- Ingresando datos para {archivo} ---")
        nombre = input("Nombre del cantante u orquesta: ")
        presentaciones = int(input("Número de presentaciones: "))
        fechas = input("Fechas de las presentaciones (separadas por '|'): ")
        
        with open(archivo, 'w', newline='') as archivo_csv:
            escritor = csv.writer(archivo_csv)
            escritor.writerow([nombre, presentaciones, fechas])
        
        print(f"Archivo {archivo} creado exitosamente con los datos ingresados.")

    return datos_archivos

def leer_archivo(nombre_archivo):
    """Lee un archivo CSV y devuelve una lista de registros como diccionarios."""
    registros = []
    try:
        with open(nombre_archivo, 'r') as archivo:
            lector = csv.reader(archivo)
            for linea in lector:
                if len(linea) < 3:
                    continue
                registros.append({
                    'nombre': linea[0].strip(),
                    'presentaciones': int(linea[1].strip()),
                    'fechas': linea[2].strip()
                })
    except FileNotFoundError:
        print(f"Error: El archivo {nombre_archivo} no existe.")
    return registros

def ordenar_burbuja_con_pasos(registros):
    """Ordena una lista de registros usando el método de burbuja y muestra los pasos."""
    n = len(registros)
    for i in range(n):
        for j in range(0, n - i - 1):
            print(f"\nComparando: {registros[j]['nombre']} y {registros[j + 1]['nombre']}")
            if registros[j]['nombre'] > registros[j + 1]['nombre']:
                registros[j], registros[j + 1] = registros[j + 1], registros[j]
                print(f"Intercambiando: {registros[j]['nombre']} y {registros[j + 1]['nombre']}")
            
            print("Estado actual de los registros:")
            for registro in registros:
                print(f"- {registro['nombre']}")
    return registros

def intercalar_archivos_burbuja(*archivos):
    """Intercala múltiples listas de registros y ordena con el método de burbuja."""
    registros_totales = []
    for archivo in archivos:
        registros_totales.extend(archivo)
    
    return ordenar_burbuja_con_pasos(registros_totales)

def escribir_archivo(nombre_archivo, registros):
    """Escribe los registros en un archivo CSV."""
    with open(nombre_archivo, 'w', newline='') as archivo:
        escritor = csv.writer(archivo)
        for registro in registros:
            escritor.writerow([
                registro['nombre'],
                registro['presentaciones'],
                registro['fechas']
            ])

if __name__ == "__main__":
    pedir_datos_archivos()

    print("\nIntercalando archivos A1, A2, y A3 en el archivo RECITALES (usando burbuja)...")

    A1 = leer_archivo("A1.csv")
    A2 = leer_archivo("A2.csv")
    A3 = leer_archivo("A3.csv")

    registros_intercalados = intercalar_archivos_burbuja(A1, A2, A3)

    escribir_archivo("RECITALES.csv", registros_intercalados)

    print("\nIntercalación completada. Archivo generado: RECITALES.csv")
