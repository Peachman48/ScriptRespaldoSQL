import os
import datetime

# Ruta a la carpeta de respaldos
backup_path = "c:\Respaldos_sql"

# Fecha actual
now = datetime.datetime.now()

# Borrar los respaldos que tengan más de 7 días
for file in os.listdir(backup_path):
    (filename, extension) = os.path.splitext(file)
    if extension == ".sql":
        last_modified = datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join(backup_path, file)))
        if (now - last_modified).days > 10:
            os.remove(os.path.join(backup_path, file))
            print("Los respaldos han sido borrados exitosamente")


