from fastapi import FastAPI, Body  # Agregamos Body para el JSON
import uvicorn

# Crear la instancia de FastAPI
app = FastAPI()

# Lista simple de usuarios (simulada)
asistencias_db = [
    {"id": 1, "fecha": "2023-01-01", "nombre": "Esteban", "estado": "asiste"},
    {"id": 2, "fecha": "2023-01-02", "nombre": "Jefri", "estado": "falta"},
    {"id": 3, "fecha": "2023-01-03", "nombre": "Yohall", "estado": "asiste"}
]

# Variable para generar IDs únicos
contador_id = 4

# Rutas GET
@app.get("/")
def root():
    return {"mensaje": "¡Bienvenido a mi API con FastAPI!"}

@app.get("/asistencias")
def obtener_asistencias():
    return {"asistencias": asistencias_db}

@app.get("/asistencias/{asistencia_id}")
def obtener_asistencia(asistencia_id: int):
    for asistencia in asistencias_db:
        if asistencia["id"] == asistencia_id:
            return {"asistencia": asistencia}
    return {"error": f"Asistencia con ID {asistencia_id} no encontrada"}

# Rutas POST 
@app.post("/asistencia")
def crear_asistencia(request: dict = Body(...)):  # Captura el JSON como dict
    global contador_id
    
    # Chequeo manual: verificar si faltan campos
    if "nombre" not in request or "estado" not in request:
        return {"error": "Faltan campos: nombre y estado son requeridos"}
    
    nombre = request["nombre"]
    estado = request["estado"]

    # Verificar si el estado ya existe
    for u in asistencias_db:
        if u["estado"] == estado:
            return {"error": "El estado ya está registrado"}

    # Crear nueva asistencia
    nueva_asistencia = {
        "id": contador_id,
        "nombre": nombre,
        "estado": estado
    }

    asistencias_db.append(nueva_asistencia)
    contador_id += 1

    return {"mensaje": "Asistencia creada exitosamente", "asistencia": nueva_asistencia}

# Rutas PUT 
@app.put("/asistencias/{asistencia_id}")
def actualizar_asistencia(asistencia_id: int, request: dict = Body(...)):
    # Chequeo manual: verificar si faltan campos
    if "nombre" not in request or "estado" not in request:
        return {"error": "Faltan campos: nombre y estado son requeridos"}
    
    nombre = request["nombre"]
    estado = request["estado"]

    for i, u in enumerate(asistencias_db):
        if u["id"] == asistencia_id:
            # Verificar si el nuevo estado ya existe (excepto en el mismo usuario)
            for otro_u in asistencias_db:
                if otro_u["estado"] == estado and otro_u["id"] != asistencia_id:
                    return {"error": "El estado ya está registrado por otro usuario"}

            asistencias_db[i] = {
                "id": asistencia_id,
                "nombre": nombre,
                "estado": estado
            }
            return {"mensaje": "Asistencia actualizada", "asistencia": asistencias_db[i]}

    return {"error": f"Asistencia con ID {asistencia_id} no encontrada"}

# Rutas DELETE
@app.delete("/asistencias/{asistencia_id}")
def eliminar_asistencia(asistencia_id: int):
    for i, asistencia in enumerate(asistencias_db):
        if asistencia["id"] == asistencia_id:
            asistencia_eliminada = asistencias_db.pop(i)
            return {"mensaje": "Asistencia eliminada", "asistencia": asistencia_eliminada}

    return {"error": f"Asistencia con ID {asistencia_id} no encontrada"}

# Ejecutar la aplicación
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
