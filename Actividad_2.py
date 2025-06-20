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
# Filtro por 2 parametros de consulta (query) NombreCompleto y Carrera
@app.get("/Estudiantes/filtro1")
def filtro1(Edad: int, Carrera: str):
    filtred_dfq = df[(df["Edad"] == Edad) & (df["Carrera"] == Carrera)]
    return filtred_dfq.to_dict(orient="records")

# Filtro por 2 parametros de consulta (query) Edad y Sexo
@app.get("/Estudiantes/filtro2")
def filtro2(Edad: int, Sexo: Optional[str] = None):
    filtred_dfq = df[df["Edad"] == Edad]
    if Sexo:
        filtred_dfq = filtred_dfq[filtred_dfq["Sexo"] == Sexo]
    return filtred_dfq.to_dict(orient="records")

# Filtro por 3 parametros de consulta (query) Carrera, Sexo y AñoExamen
@app.get("/Estudiantes/filtro3")
def filtro3(Carrera: str, Sexo: str, AñoExamen: int):
    filtred_dfq = df[(df["Carrera"] == Carrera) & (df["Sexo"] == Sexo) & (df["AñoExamen"] == AñoExamen)]
    return filtred_dfq.to_dict(orient="records")

# Filtro por 3 parametros de consulta (query)Materia, Edad y Compañero
@app.get("/Estudiantes/filtro4")
def filtro4(Materia: str, Edad: int, Compañero: Optional[bool] = None):
    filtred_dfq = df[df["Materia"] == Materia]
    if Compañero is not None:
        filtred_dfq = filtred_dfq[filtred_dfq["Compañero"] == Compañero]
    filtred_dfq = filtred_dfq[filtred_dfq["Edad"] == Edad]
    return filtred_dfq.to_dict(orient="records")

# Filtro por 4 parametros de consulta (query) Edad, Carrera, Compañero y Materia
@app.get("/Estudiantes/filtro5")
def filtro5(Edad: int, Carrera: str, Compañero: bool, Materia: str):
    filtred_dfq = df[(df["Edad"] == Edad) & (df["Carrera"] == Carrera) & (df["Compañero"] == Compañero) & (df["Materia"] == Materia)]
    return filtred_dfq.to_dict(orient="records")

@app.get("/Estudiantes/filtro6")
def filtro6(Edad: int, Carrera: str, Compañero: bool, Sexo: Optional[str] = None):
    filtred_dfq = df[(df["Edad"] == Edad) & (df["Carrera"] == Carrera) & (df["Compañero"] == Compañero)]
    if Sexo:
        filtred_dfq = filtred_dfq[filtred_dfq["Sexo"] == Sexo]
    return filtred_dfq.to_dict(orient="records")

# Filtro por 5 parametros de consulta (query) Matricula, Edad, Carrera, Compañero y Materia
@app.get("/Estudiantes/filtro7")
def filtro7(Matricula: int, Edad: int, Carrera: str, Compañero: bool, Materia: str):
    filtred_dfq = df[(df["Matricula"] == Matricula) & (df["Edad"] == Edad) & (df["Carrera"] == Carrera) & (df["Compañero"] == Compañero) & (df["Materia"] == Materia)]
    return filtred_dfq.to_dict(orient="records")

# Filtro por 5 parametros de consulta (query) NombreCompleto, Edad, Sexo, Compañero y Materia
@app.get("/Estudiantes/filtro8")
def filtro8(NombreCompleto: str, Edad: int, Sexo: Optional[str] = None, Compañero: bool = None, Materia: str = None):
    filtred_dfq = df[(df["NombreCompleto"] == NombreCompleto) & (df["Edad"] == Edad)]
    if Sexo:
        filtred_dfq = filtred_dfq[filtred_dfq["Sexo"] == Sexo]
    if Compañero is not None:
        filtred_dfq = filtred_dfq[filtred_dfq["Compañero"] == Compañero]
    if Materia:
        filtred_dfq = filtred_dfq[filtred_dfq["Materia"] == Materia]
    return filtred_dfq.to_dict(orient="records")

# Filtro por 6 parametros de consulta (query) NombreCompleto, Edad, Carrera, Sexo, Compañero y SoloCampos (Retorna solo los campos especificados)
@app.get("/Estudiantes/filtro9")
def filtro9(NombreCompleto: str, Edad: int, Carrera: str, Sexo: Optional[str] = None, Compañero: Optional[bool] = None, SoloCampos: bool = False):
    filtred_dfq = df[(df["NombreCompleto"] == NombreCompleto) & (df["Edad"] == Edad) & (df["Carrera"] == Carrera)]
    if Sexo:
        filtred_dfq = filtred_dfq[filtred_dfq["Sexo"] == Sexo]
    if Compañero is not None:
        filtred_dfq = filtred_dfq[filtred_dfq["Compañero"] == Compañero]
    
    if SoloCampos:
        return filtred_dfq[["NombreCompleto", "Edad", "Carrera", "Sexo", "Compañero"]].to_dict(orient="records")
    else:
        return filtred_dfq.to_dict(orient="records")
    
# Filtro por 6 parametros de consulta (query) Edad, Carrera, Sexo, AñoExamen, Contar(Solo devolver cantidad de registros en los campos) y SoloCampos (Retorna solo los campos especificados)
@app.get("/Estudiantes/filtro10")
def filtro10(Edad: int, Carrera: str, Sexo: str, AñoExamen: int, Contar: bool = False, SoloCampos: bool = False):
    filtred_dfq = df[(df["Edad"] == Edad) & (df["Carrera"] == Carrera)]
    filtred_dfq = filtred_dfq[filtred_dfq["Sexo"] == Sexo]
    filtred_dfq = filtred_dfq[filtred_dfq["AñoExamen"] == AñoExamen]
        
    if Contar and SoloCampos:
        result = list()
        result.append(filtred_dfq["Edad"].value_counts().to_dict())
        result.append(filtred_dfq["Carrera"].value_counts().to_dict())
        result.append(filtred_dfq["Sexo"].value_counts().to_dict())
        result.append(filtred_dfq["AñoExamen"].value_counts().to_dict())
        return result
    elif Contar:
        result = list()
        result.append(filtred_dfq["NombreCompleto"].value_counts().to_dict())
        result.append(filtred_dfq["Matricula"].value_counts().to_dict())
        result.append(filtred_dfq["Edad"].value_counts().to_dict())
        result.append(filtred_dfq["Carrera"].value_counts().to_dict())
        result.append(filtred_dfq["Sexo"].value_counts().to_dict())
        result.append(filtred_dfq["Correo"].value_counts().to_dict())
        result.append(filtred_dfq["Facultad"].value_counts().to_dict())
        result.append(filtred_dfq["AñoExamen"].value_counts().to_dict())
        result.append(filtred_dfq["Compañero"].value_counts().to_dict())
        result.append(filtred_dfq["Materia"].value_counts().to_dict())
        return result
    elif SoloCampos:
        return filtred_dfq[["Edad", "Carrera", "Sexo", "AñoExamen"]].to_dict(orient="records")
    
    return filtred_dfq.to_dict(orient="records")
