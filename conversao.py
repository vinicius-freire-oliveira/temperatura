# Definindo a função para converter Celsius para Fahrenheit
def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Definindo a função para converter Celsius para Kelvin
def celsius_para_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

# Definindo a temperatura em graus Celsius
temperatura_celsius = 25

# Chamando as funções para realizar as conversões de temperatura
temperatura_fahrenheit = celsius_para_fahrenheit(temperatura_celsius)
temperatura_kelvin = celsius_para_kelvin(temperatura_celsius)

# Exibe a Conversão de Temperatura
print("\n##### Conversão de Temperatura #####")
# Imprimindo os resultados das conversões
print(f"{temperatura_celsius} graus Celsius são equivalentes a {temperatura_fahrenheit:.2f} Fahrenheit e {temperatura_kelvin:.2f} Kelvin.")

