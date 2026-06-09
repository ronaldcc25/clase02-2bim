"""
Título de las series con promedio de edad de sus actores y el numero de premios que tiene cada serie
"""

# Usamos los modelos ya definidos en `modelo.py`
from modelo import Serie, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

# Obtenemos todas las series
series = session.query(Serie).all()

for serie in series:
    p = serie.obtener_edad_promedio()
    num_p = serie.obtener_numero_premios()

    if p is None:
        print(f"{serie.titulo}: No tiene actores registrados")
    else:
        print(f"Serie: {serie.titulo} - {p:.2f} promedio años - {num_p} premios")

session.close()
