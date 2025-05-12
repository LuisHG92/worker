FROM python:3.11.11-slim-bullseye

WORKDIR /app

# Instalar dependencias
RUN apt-get update && apt-get install -y python3-pip && rm -rf /var/lib/apt/lists/*

# Copiar archivos
COPY . .

# Instalar paquetes
RUN pip install --no-cache-dir -r requirements.txt

# Ejecutar el script del worker
CMD ["python", "translate_worker.py"]
