"""
Título de las series con promedio de edad de sus actores
"""

# Usamos los modelos ya definidos en `modelo.py`
from modelo import Actor, Serie, engine
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

# Usamos outerjoin para incluir series sin actores (promedio será None)
resultados = (
    session.query(Serie.titulo, func.avg(Actor.edad).label("promedio_edad"))
    .outerjoin(Actor)
    .group_by(Serie.titulo)
    .all()
)

for t, p in resultados:
    if p is None:
        print(f"{t}: No tiene actores registrados")
    else:
        print(f"{t}: {p:.2f} años (promedio)")

session.close()
