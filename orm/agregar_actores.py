from config import cadena_base_datos
from modelo import Actor, Base, Pais, Serie
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(cadena_base_datos)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

archivo_actores = open("data/actores.csv", "r", encoding="utf-8")
lineas_actores = archivo_actores.readlines()[1:]
contador = 0

for linea in lineas_actores:
    datos = [d.strip() for d in linea.split(",")]

    if not datos or datos[0] == "":
        continue

    pais = session.query(Pais).filter_by(nombre=datos[3]).first()
    serie = session.query(Serie).filter_by(titulo=datos[4]).first()

    actor = Actor(
        id=int(datos[0]),
        nombre=datos[1],
        edad=int(datos[2]),
        pais_id=pais.id if pais else None,
        serie_id=serie.id if serie else None,
    )
    session.merge(actor)
    contador = contador + 1

session.commit()
archivo_actores.close()
print("Actores agregados:", contador)
