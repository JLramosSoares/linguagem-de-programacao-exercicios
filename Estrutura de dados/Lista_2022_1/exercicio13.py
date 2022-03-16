"""
13) Faça uma função que receba a temperatura em graus Celsius e retorne o valor correspondente em graus Fahrenheit.
"""

def convertFarenheit(ce:float) -> float:
    return ce * 1.8 + 32

celciusTemp = 32
fahrenheitTemp = round(convertFarenheit(celciusTemp), 2)

print("Celcius: {} °C\nFahrenheit: {} °F".format(celciusTemp, fahrenheitTemp))

