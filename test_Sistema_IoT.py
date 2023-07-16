import re
import pytest 
from Sistema_IoT import *

def test_collect_sensor_data():
    resultado1 = Sistema_IoT.collect_sensor_data()

    assert isinstance(resultado1, list), "El resultado no es una lista"

    if resultado1:  # Verificar si la lista no está vacía
        assert isinstance(resultado1[0], str), "El valor 'formatted_date' no es una cadena"

        # Verificar el formato de fecha y hora usando una expresión regular
        formato_esperado = r"\d{1,2}/\d{1,2}/\d{4}/\d{1,2}:\d{1,2}:\d{1,2}"
        assert re.match(formato_esperado, resultado1[0]), "El valor 'formatted_date' no tiene el formato esperado"

        assert all(isinstance(valor, (int, float)) for valor in resultado1[1:4]), "Los valores 'temp', 'hum' y 'light_intensity' no son números"

if __name__ == '__main__':
  test_collect_sensor_data()