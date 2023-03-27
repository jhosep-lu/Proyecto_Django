# Utiliza una imagen base de Python con una versión específica
FROM python:3.9

# Establece variables de entorno
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Crea un directorio de trabajo 
WORKDIR /app

# Instala las dependencias del proyecto
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copia el proyecto al contenedor
COPY . /app/

# Expone el puerto en el que se ejecutará
EXPOSE 8000

# Ejecuta el servidor de Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
