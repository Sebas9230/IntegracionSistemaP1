import os
import shutil

def mover_archivos(directorio_origen, directorio_destino, archivo):
    ruta_origen = os.path.join(directorio_origen, archivo)
    ruta_destino = os.path.join(directorio_destino, archivo)
    shutil.move(ruta_origen, ruta_destino)
    print(f"Archivo {archivo} movido a {directorio_destino}")

def main():
    directorio_origen = "D:/Users/Sebas/Documents/Udla/Octavo semestre/Integración de sistemas/Progreso 1/datos_csv"
    directorio_destino = "D:/Users/Sebas/Documents/Udla/Octavo semestre/Integración de sistemas/Progreso 1/Respaldo"
    archivos_despues = os.listdir(directorio_origen)
    for archivo in archivos_despues:
        if archivo.endswith('.csv'):
            print("ENTRO A LA TRANSFERENCIA DE ARCHIVO")
            mover_archivos(directorio_origen, directorio_destino, archivo)

main()
