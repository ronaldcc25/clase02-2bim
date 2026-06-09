from config import cadena_base_datos
from modelo import Base, Premio, Serie
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(cadena_base_datos)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

archivo_premios = open("data/premios.csv", "r", encoding="utf-8")
lineas_premios = archivo_premios.readlines()[1:]
contador = 0

for linea in lineas_premios:
    datos = [d.strip() for d in linea.split(",")]

    if not datos or datos[0] == "":
        continue

    serie = session.query(Serie).filter_by(titulo=datos[4]).first()

    premio = Premio(
        id=int(datos[0]),
        nombre_premio=datos[1],
        categoria=datos[2],
        anio=int(datos[3]),
        serie_id=serie.id if serie else None,
    )
    session.merge(premio)
    contador = contador + 1

session.commit()
archivo_premios.close()
print("Premios agregados:", contador)
