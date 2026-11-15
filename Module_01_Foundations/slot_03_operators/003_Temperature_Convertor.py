#Complete this temperature converter
celsius = input("Enter temperature in Celsius:")
celsius_num = int(celsius)
fahrenheit = (celsius_num*9/5) + 32
print(celsius_num, "°C = ", fahrenheit, "°F ")

#Test: If user enters 0, should output: 0 °C = 32.0 °F