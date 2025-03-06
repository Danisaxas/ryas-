FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos del proyecto al contenedor
COPY . /app/

# Crea un entorno virtual en /opt/venv
RUN python -m venv /opt/venv

# Instala las dependencias desde requirements.txt en el entorno virtual
RUN /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

# Usa el entorno virtual por defecto para ejecutar tu aplicación
ENV PATH="/opt/venv/bin:$PATH"

# Comando para ejecutar tu bot (ajustar según sea necesario)
CMD ["python", "bot.py"]
