def convert_temperature(temperature, unit):
    if unit == 'F':
        # Fahrenheit to Celsius conversion
        converted_temp = (temperature - 32) * 5/9
    elif unit == 'C':
        # Celsius to Fahrenheit conversion
        converted_temp = (temperature * 9/5) + 32
    else:
        return "Invalid unit. Please provide 'F' for Fahrenheit or 'C' for Celsius."

    return round(converted_temp, 2)

# Example usage:
print(convert_temperature(32, 'F')) 
print(convert_temperature(100, 'C'))
