from config import cadena_base_datos
from modelo import Base, Pais
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(cadena_base_datos)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

archivo_paises = open("data/paises.csv", "r", encoding="utf-8")
lineas_paises = archivo_paises.readlines()[1:]
contador = 0

for linea in lineas_paises:
    datos = [d.strip() for d in linea.split(",")]

    if not datos or datos[0] == "":
        continue

    pais = Pais(
        id=int(datos[0]),
        nombre=datos[1],
        continente=datos[2],
    )
    session.merge(pais)
    contador = contador + 1

session.commit()
archivo_paises.close()
print("Paises agregados:", contador)
