# importamos al framework fastapi a nuestro entorno de trabajo
# Importamos la libreria pydantic para manejar los datos y pandas para manejar los datos en formato de tabla
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import pandas as pd

# Creamos un objeto apartir de la clase FastApi
app = FastAPI()

# Importamos la base de datos con los datos de los estudiantes
df = pd.read_excel("Data50.xlsx")

# Definimos el modelo de datos utilizando Pydantic
class Students(BaseModel): # Este modelo representa la estructura de los datos que vamos a manejar
    NombreCompleto: str
    Matricula: int
    Edad: int
    Carrera: str
    Sexo: str
    Correo: str
    Facultad: str
    AñoExamen: int
    Compañero: bool
    Materia: str    

# ------------------------ Instancias de la función get api framework FastApi ------------------
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Endpoints con parametros de ruta >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Filtro por columna NombreCompleto
@app.get("/Estudiantes/NombreCompleto/{Nombre_Completo}")
def get_student(Nombre_Completo: str):
    filtred_dfp = df[df["NombreCompleto"] == Nombre_Completo]
    if not filtred_dfp.empty:
        return filtred_dfp.to_dict(orient="records")
    return {"error": "Estudiante no encontrado por su nombre completo"}

# Filtro por columna Matricula
@app.get("/Estudiantes/Matricula/{Matricula}")
def get_student_by_matricula(Matricula: int):
    filtred_dfp = df[df["Matricula"] == Matricula]
    if not filtred_dfp.empty:
        return filtred_dfp.to_dict(orient="records")
    return {"error": "Estudiante no encontrado por su matricula"}

# Filtro por columna Edad
@app.get("/Estudiantes/Edad/{Edad}")
def get_student_by_edad(Edad: int):
    filtred_dfp = df[df["Edad"] == Edad]
    if not filtred_dfp.empty:
        return filtred_dfp.to_dict(orient="records")
    return {"error": "Estudiante no encontrado por su edad"}

# Filtro por columna Carrera
@app.get("/Estudiantes/Carrera/{Carrera}")
def get_student_by_carrera(Carrera: str):
    filtred_dfp = df[df["Carrera"] == Carrera]
    if not filtred_dfp.empty:
        return filtred_dfp.to_dict(orient="records")
    return {"error": "Estudiante no encontrado por su carrera"}

# Filtro por columna Sexo
@app.get("/Estudiantes/Sexo/{Sexo}")
def get_student_by_sexo(Sexo: str):
    filtred_dfp = df[df["Sexo"] == Sexo]
    if not filtred_dfp.empty:
        return filtred_dfp.to_dict(orient="records")
    return {"error": "Estudiante no encontrado por su sexo"}

# Filtro por columna Correo
@app.get("/Estudiantes/Correo/{Correo}")
def get_student_by_correo(Correo: str):
    filtred_dfp = df[df["Correo"] == Correo]
    if not filtred_dfp.empty:
        return filtred_dfp.to_dict(orient="records")
    return {"error": "Estudiante no encontrado por su correo"}

# Filtro por columna Facultad
@app.get("/Estudiantes/Facultad/{Facultad}")
def get_student_by_facultad(Facultad: str):
    filtred_dfp = df[df["Facultad"] == Facultad]
    if not filtred_dfp.empty:
        return filtred_dfp.to_dict(orient="records")
    return {"error": "Estudiante no encontrado por su facultad"}

# Filtro por columna AñoExamen
@app.get("/Estudiantes/AñoExamen/{AñoExamen}")
def get_student_by_año_examen(AñoExamen: int):
    filtred_dfp = df[df["AñoExamen"] == AñoExamen]
    if not filtred_dfp.empty:
        return filtred_dfp.to_dict(orient="records")
    return {"error": "Estudiante no encontrado por su año de examen"}

# Filtro por columna Compañero
@app.get("/Estudiantes/Compañero/{Compañero}")
def get_student_by_compañero(Compañero: bool):
    filtred_dfp = df[df["Compañero"] == Compañero]
    if not filtred_dfp.empty:
        return filtred_dfp.to_dict(orient="records")
    return {"error": "Estudiante no encontrado por su compañero"}

# Filtro por columna Materia
@app.get("/Estudiantes/Materia/{Materia}")
def get_student_by_materia(Materia: str):
    filtred_dfp = df[df["Materia"] == Materia]
    if not filtred_dfp.empty:
        return filtred_dfp.to_dict(orient="records")
    return {"error": "Estudiante no encontrado por su materia"}

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Endpoints con parametros de consulta >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Filtros por columnas (2 parámetros)
@app.get("/filtro1")
def filtro1(NombreCompleto: str, Carrera: Optional[str] = None):
    filtred_dfq = df
    filtred_dfq = filtred_dfq[filtred_dfq["NombreCompleto"] == NombreCompleto]
    if Carrera:
        filtred_dfq = filtred_dfq[filtred_dfq["Carrera"] == Carrera]
    return filtred_dfq.to_dict(orient="records")

@app.get("/filtro2")
def filtro2(Sexo: str, Edad: Optional[int] = None):
    filtred_dfq = df[df["Sexo"] == Sexo]
    if Edad:
        filtred_dfq = filtred_dfq[filtred_dfq["Edad"] == Edad]
    return filtred_dfq.to_dict(orient="records")

# Filtro con 2 parámetros (uno opcional)
@app.get("/filtro3")
def filtro3(Facultad: str, AñoExamen: Optional[int] = None):
    filtred_dfq = df[df["Facultad"] == Facultad]
    if AñoExamen:
        filtred_dfq = filtred_dfq[filtred_dfq["AñoExamen"] == AñoExamen]
    return filtred_dfq.to_dict(orient="records")

@app.get("/filtro4")
def filtro4(Matricula: str, Materia: Optional[str] = None):
    filtred_dfq = df[df["Matricula"] == Matricula]
    if Materia:
        filtred_dfq = filtred_dfq[filtred_dfq["Materia"] == Materia]
    return filtred_dfq.to_dict(orient="records")

# Filtro con 2 parámetros (ambos opcionales)
@app.get("/filtro5")
def filtro5(NombreCompleto: Optional[str] = None, Compañero: Optional[str] = None):
    filtred_dfq = df
    if NombreCompleto:
        filtred_dfq = filtred_dfq[filtred_dfq["NombreCompleto"] == NombreCompleto]
    if Compañero:
        filtred_dfq = filtred_dfq[filtred_dfq["Compañero"] == Compañero]
    return filtred_dfq.to_dict(orient="records")

@app.get("/filtro6")
def filtro6(Correo: Optional[str] = None, Edad: Optional[int] = None):
    filtred_dfq = df
    if Correo:
        filtred_dfq = filtred_dfq[filtred_dfq["Correo"] == Correo]
    if Edad:
        filtred_dfq = filtred_dfq[filtred_dfq["Edad"] == Edad]
    return filtred_dfq.to_dict(orient="records")

# Filtro con 3 parámetros
@app.get("/filtro7")
def filtro7(Carrera: str, Sexo: Optional[str] = None, Materia: Optional[str] = None):
    filtred_dfq = df[df["Carrera"] == Carrera]
    if Sexo:
        filtred_dfq = filtred_dfq[filtred_dfq["Sexo"] == Sexo]
    if Materia:
        filtred_dfq = filtred_dfq[filtred_dfq["Materia"] == Materia]
    return filtred_dfq.to_dict(orient="records")

@app.get("/filtro8")
def filtro8(NombreCompleto: Optional[str] = None, Facultad: Optional[str] = None, AñoExamen: Optional[int] = None):
    filtred_dfq = df
    if NombreCompleto:
        filtred_dfq = filtred_dfq[filtred_dfq["NombreCompleto"] == NombreCompleto]
    if Facultad:
        filtred_dfq = filtred_dfq[filtred_dfq["Facultad"] == Facultad]
    if AñoExamen:
        filtred_dfq = filtred_dfq[filtred_dfq["AñoExamen"] == AñoExamen]
    return filtred_dfq.to_dict(orient="records")

# Filtro con 3 parámetros (uno obligatorio)
@app.get("/filtro9")
def filtro9(Matricula: str, Compañero: Optional[str] = None, Edad: Optional[int] = None):
    filtred_dfq = df[df["Matricula"] == Matricula]
    if Compañero:
        filtred_dfq = filtred_dfq[filtred_dfq["Compañero"] == Compañero]
    if Edad:
        filtred_dfq = filtred_dfq[filtred_dfq["Edad"] == Edad]
    return filtred_dfq.to_dict(orient="records")

# Filtro con 4 parámetros (uno obligatorio)
@app.get("/filtro10")
def filtro10(Carrera: str, Facultad: Optional[str] = None, Sexo: Optional[str] = None, AñoExamen: Optional[int] = None):
    filtred_dfq = df[df["Carrera"] == Carrera]
    if Facultad:
        filtred_dfq = filtred_dfq[filtred_dfq["Facultad"] == Facultad]
    if Sexo:
        filtred_dfq = filtred_dfq[filtred_dfq["Sexo"] == Sexo]
    if AñoExamen:
        filtred_dfq = filtred_dfq[filtred_dfq["AñoExamen"] == AñoExamen]
    return filtred_dfq.to_dict(orient="records")