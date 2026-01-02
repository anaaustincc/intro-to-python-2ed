"""
Convert a temperature from Fahrenheit to Celsius
"""
temp_f = float(input("Temp in °F: "))

temp_C = str((temp_f - 32) * 5 / 9)

print("Temp in °C:   " + temp_C)
