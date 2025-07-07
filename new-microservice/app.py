from fastapi import FastAPI
import uvicorn

app = FastAPI(title="Nuevo Microservicio", version="1.0.0")

@app.get("/")
def leer_raiz():
    return {"mensaje": "Nuevo Microservicio esta ejecutandose"}

@app.get("/salud")
def verificar_salud():
    return {"estado": "saludable"}

@app.get("/api/comunicacion")
def comunicar_con_legacy():
    return {"mensaje": "Comunicacion con aplicacion legacy"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
