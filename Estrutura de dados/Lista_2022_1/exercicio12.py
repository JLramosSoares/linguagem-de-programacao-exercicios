"""
12) Faça uma função que receba a temperatura em graus Fahrenheit e retorne o valor correspondente em graus Celsius.
"""

def convertCelcius(fa:float) -> float:
    return (fa - 32) / 1.8

fahrenheitTemp = 50
celciusTemp = round(convertCelcius(fahrenheitTemp), 2)

print("Fahrenheit: {} °F\nCelsius: {} °C".format(fahrenheitTemp, celciusTemp))
 
