import shutil
import os
import schedule
import time

def move_csv_files():
    source_folder = r'D:/Users/Sebas/Documents/Udla/Octavo semestre/Integración de sistemas/Progreso 1/datos_csv'
    target_folder = r'D:/Users/Sebas/Documents/Udla/Octavo semestre/Integración de sistemas/Progreso 1/Respaldo'

    # Lista todos los archivos en la carpeta de origen
    files = os.listdir(source_folder)

    # Filtra solo los archivos .csv
    csv_files = [file for file in files if file.endswith('.csv')]

    # Mueve cada archivo .csv a la carpeta de destino
    for file in csv_files:
        shutil.move(os.path.join(source_folder, file), os.path.join(target_folder, file))
        print(f"Archivo {file} movido correctamente.")

# Programa la tarea para ejecutarse a las 8pm todos los días
schedule.every().day.at("20:00").do(move_csv_files)

while True:
    # Ejecuta la tarea programada
    schedule.run_pending()
    # Espera 1 minuto antes de volver a verificar si hay tareas programadas
    time.sleep(60)
