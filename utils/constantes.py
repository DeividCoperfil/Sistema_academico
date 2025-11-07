import os

# Ruta base donde se guardarán los CSV
RUTA_BASE_CSV = r"C:\Users\dafet\Desktop\sistema_academico\utils/csvs"

# Verifica que exista
if not os.path.exists(RUTA_BASE_CSV):
    os.makedirs(RUTA_BASE_CSV, exist_ok=True)
