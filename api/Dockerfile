# 1. Usar una imagen base de Python liviana
FROM python:3.10-slim

# 2. Instalar dependencias del sistema necesarias para el conector de MariaDB
RUN apt-get update && apt-get install -y \
    gcc \
    libmariadb-dev \
    && rm -rf /var/lib/apt/lists/*

# 3. Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# 4. Copiar el archivo de dependencias e instalarlas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiar el resto del código (main.py y la carpeta templates)
COPY . .

# 6. Exponer el puerto donde corre FastAPI
EXPOSE 8000

# 7. Comando para arrancar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]