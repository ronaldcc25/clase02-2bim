from config import cadena_base_datos
from modelo import Base, Pais, Plataforma, Serie
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(cadena_base_datos)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

archivo_series = open("data/series.csv", "r", encoding="utf-8")
lineas_series = archivo_series.readlines()[1:]
contador = 0

for linea in lineas_series:
    datos = [d.strip() for d in linea.split(",")]

    if not datos or datos[0] == "":
        continue

    plataforma = session.query(Plataforma).filter_by(nombre=datos[5]).first()
    pais = session.query(Pais).filter_by(nombre=datos[6]).first()

    serie = Serie(
        id=int(datos[0]),
        titulo=datos[1],
        genero=datos[2],
        anio_estreno=int(datos[3]),
        temporadas=int(datos[4]),
        plataforma_id=plataforma.id if plataforma else None,
        pais_id=pais.id if pais else None,
    )
    session.merge(serie)
    contador = contador + 1

session.commit()
archivo_series.close()
print("Series agregadas:", contador)
