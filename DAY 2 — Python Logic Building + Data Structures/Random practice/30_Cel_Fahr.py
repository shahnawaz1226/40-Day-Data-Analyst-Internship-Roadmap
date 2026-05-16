# Temperature Converter
# Convert Celsius to Fahrenheit. Formula: F = (C × 9/5) + 32

celcius = int(input("Enter celcius degree: "))

def fahrenheit(celcius):
    return (celcius*9/5)+32

print(fahrenheit(celcius))