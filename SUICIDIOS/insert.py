import sqlite3

conn = sqlite3.connect("suicidios.db")

cursor = conn.cursor()

_SQL= """
CREATE TABLE if not exists SUICIDIOS(
NombreMunicipio TEXT,
CodigoMunicipio TEXT,
Ubicación TEXT,
NombreRegion TEXT,
CodigoRegion TEXT,
Anio TEXT,
CausaMortalidad TEXT,
TipoPoblacionObjetivo TEXT,
NumeroPoblacionObjetivo TEXT,
NumeroCasos TEXT);
"""

cursor.execute(_SQL)


with open('sql.sql', 'r',encoding="UTF-8") as f:
    cursor.executescript(f.read())

conn.commit()

conn.close()