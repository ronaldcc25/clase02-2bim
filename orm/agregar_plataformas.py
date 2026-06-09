from config import cadena_base_datos
from modelo import Base, Pais, Plataforma
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(cadena_base_datos)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

archivo_plataformas = open("data/plataformas.csv", "r", encoding="utf-8")
lineas_plataformas = archivo_plataformas.readlines()[1:]
contador = 0

for linea in lineas_plataformas:
    datos = [d.strip() for d in linea.split(",")]

    if not datos or datos[0] == "":
        continue

    pais = session.query(Pais).filter_by(nombre=datos[2]).first()

    plataforma = Plataforma(
        id=int(datos[0]),
        nombre=datos[1],
        pais_id=pais.id if pais else None,
        suscriptores_millones=int(float(datos[3])),
    )
    session.merge(plataforma)
    contador = contador + 1

session.commit()
archivo_plataformas.close()
print("Plataformas agregadas:", contador)
