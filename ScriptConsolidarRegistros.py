import os
import pandas as pd
import pyodbc

# Configuración de la conexión a la base de datos
server = 'DESKTOP-V7UJ9OR'
database = 'IntegracionSistemaP1'
trusted_connection = 'yes'
driver = '{SQL Server}'

# Ruta de la carpeta donde se encuentran los archivos CSV
csv_folder = r'D:/Users/Sebas/Documents/Udla/Octavo semestre/Integración de sistemas/Progreso 1/datos_csv'

# Función para obtener el nombre del archivo sin la extensión
def get_file_name_without_extension(file_path):
    return os.path.splitext(os.path.basename(file_path))[0]

# Función para cargar los datos de un archivo CSV a la base de datos
def load_csv_to_database(csv_file_path, cursor):
    # Leer el archivo CSV omitiendo la primera fila (encabezados)
    df = pd.read_csv(csv_file_path, skiprows=1)
    # Obtener el nombre del archivo sin extensión (que se utilizará como idLocal)
    idlocal = get_file_name_without_extension(csv_file_path)
    # Agregar el idlocal a los datos del DataFrame
    df['idlocal'] = idlocal
    # Convertir el DataFrame a una lista de tuplas
    data = [tuple(row) for row in df.values]
    # Consulta SQL para insertar los datos en la base de datos
    query = f"INSERT INTO Ventas_Consolidadas (idTransaccion, idlocal, fecha, idCategoria, idProducto, cantidad, precioUnitario, totalVenta) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
    # Ejecutar la consulta para insertar los datos en lotes
    cursor.executemany(query, data)
    # Confirmar los cambios en la base de datos
    cursor.commit()
    print(f"Datos del archivo {csv_file_path} cargados correctamente a la base de datos.")

try:
    # Establecer la conexión con la base de datos
    conn = pyodbc.connect(f'DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection={trusted_connection}')
    cursor = conn.cursor()

    # Iterar sobre los archivos CSV en la carpeta
    for csv_file in os.listdir(csv_folder):
        if csv_file.endswith('.csv'):
            csv_file_path = os.path.join(csv_folder, csv_file)
            # Cargar los datos del archivo CSV a la base de datos
            load_csv_to_database(csv_file_path, cursor)

    # Cerrar el cursor y la conexión
    cursor.close()
    conn.close()
    print("Proceso completado exitosamente.")

except Exception as e:
    print(f"Se produjo un error: {str(e)}")
