# Etapa de compilacion
FROM python:3.9-slim AS builder

WORKDIR /app

# Instalar herramientas necesarias para pyinstaller
RUN apt-get update && apt-get install -y binutils && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install pyinstaller

COPY app.py .

# Creamos binario estatico
RUN pyinstaller --onefile --distpath /app/dist app.py

# Etapa de ejecucion
FROM alpine:latest

WORKDIR /app

# Copiamos solo el binario compilado
COPY --from=builder /app/dist/app .

EXPOSE 8001

CMD ["./app"]