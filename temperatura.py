# Função para converter Celsius para Fahrenheit
def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Função para converter Fahrenheit para Celsius
def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Função para converter Celsius para Kelvin
def celsius_para_kelvin(celsius):
    return celsius + 273.15

# Função para converter Kelvin para Celsius
def kelvin_para_celsius(kelvin):
    return kelvin - 273.15

# Função para converter Fahrenheit para Kelvin
def fahrenheit_para_kelvin(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius + 273.15

# Função para converter Kelvin para  Fahrenheit 
def kelvin_para_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    return (celsius * 9/5) + 32

# Exemplos de uso:

# Definindo valores de temperatura para os exemplos
celsius = 25
fahrenheit = 77
kelvin = 298.15

# Exibe a Conversão de Temperatura
print("\n##### Conversão de Temperatura #####")
# Exibe as conversões para o usuário
print(f"{celsius}°C para Fahrenheit: {celsius_para_fahrenheit(celsius)}°F")
print(f"{fahrenheit}°F para Celsius: {fahrenheit_para_celsius(fahrenheit)}°C")
print(f"{celsius}°C para Kelvin: {celsius_para_kelvin(celsius)}K")
print(f"{kelvin}K para Celsius: {kelvin_para_celsius(kelvin)}°C")
print(f"{fahrenheit}°F para Kelvin: {fahrenheit_para_kelvin(fahrenheit)}K")
print(f"{kelvin}K para Fahrenheit: {kelvin_para_fahrenheit(kelvin)}°F")
