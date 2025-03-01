from PIL import Image
import os
from pathlib import Path

# Carpeta de imágenes a optimizar
CARPETA_ENTRADA = Path(
    "assets/img/masonry-portfolio"
)  # Aquí es donde están las imágenes
CARPETA_SALIDA = Path("assets/img_optimizadas")  # Guardar imágenes optimizadas
CALIDAD = 80  # Calidad de compresión (0-100)
MAX_ANCHO = 1200  # Ancho máximo permitido
MAX_ALTO = 1200  # Alto máximo permitido

# Crear carpeta de salida si no existe
CARPETA_SALIDA.mkdir(parents=True, exist_ok=True)

# Procesar imágenes
for archivo in CARPETA_ENTRADA.iterdir():
    if archivo.suffix.lower() in (".jpg", ".jpeg", ".png"):
        ruta_salida = CARPETA_SALIDA / f"{archivo.stem}.webp"

        with Image.open(archivo) as img:
            # Redimensionar si es muy grande
            img.thumbnail((MAX_ANCHO, MAX_ALTO))

            # Guardar en WebP optimizado
            img.save(ruta_salida, "WEBP", quality=CALIDAD)

            print(f"✅ {archivo.name} → {ruta_salida}")

print("🚀 ¡Optimización completada!")
