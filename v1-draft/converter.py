length_factors = {
    'mm': 0.001,
    'cm': 0.01,
    'm': 1.0,
    'km': 1000.0,
    'in': 0.0254,
    'ft': 0.3048,
    'yd': 0.9144,
    'mi': 1609.34
}

weight_factors = {
    'mg': 0.001,
    'g': 1.0,
    'kg': 1000.0,
    'oz': 28.3495,
    'lb': 453.592
}

def convert_length(value: float, from_unit: str, to_unit: str) -> float:
    try:
        value_in_meters = value * length_factors[from_unit]
        return value_in_meters / length_factors[to_unit]
    except (KeyError, ZeroDivisionError):
        raise ValueError("Invalid length unit.")
    
def convert_weight(value: float, from_unit: str, to_unit: str) -> float:
    try:
        value_in_grams = value * weight_factors[from_unit]
        return value_in_grams / weight_factors[to_unit]
    except (KeyError, ZeroDivisionError):
        raise ValueError("Invalid weight unit.")

def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    if from_unit == to_unit:
        return value

    # Convert to Celsius first
    if from_unit == 'C':
        celsius = value
    elif from_unit == 'F':
        celsius = (value - 32) * 5/9
    elif from_unit == 'K':
        celsius = value - 273.15
    else:
        raise ValueError("Invalid temperature unit.")

    # Convert from Celsius to target unit
    if to_unit == 'C':
        return celsius
    elif to_unit == 'F':
        return celsius * 9/5 + 32
    elif to_unit == 'K':
        return celsius + 273.15
    else:
        raise ValueError("Invalid temperature unit.")
