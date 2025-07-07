from fastapi import FastAPI

app = FastAPI(title="Aplicacion Legacy", version="1.0.0")

@app.get("/")
def leer_raiz():
    return {"mensaje": "Aplicacion Legacy esta ejecutandose"}

@app.get("/salud")
def verificar_salud():
    return {"estado": "saludable"}

@app.get("/api/datos")
def obtener_datos():
    return {"datos": "datos legacy desde postgresql"}