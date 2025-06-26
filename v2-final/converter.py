# Length unit conversion factors relative to meter
length_factors  = {
    'mm': 0.001,
    'cm': 0.01,
    'm': 1.0,
    'km': 1000.0,
    'in': 0.0254,
    'ft': 0.3048,
    'yd': 0.9144,
    'mi': 1609.34
}

# Mass unit conversion factors relative to gram
mass_factors = {
    'mg': 0.001,
    'g': 1.0,
    'kg': 1000.0,
    'oz': 28.3495,
    'lb': 453.592
}

# Convert between length units by converting to meter first
def convert_length(value: float, from_unit: str, to_unit: str):
  value_in_meter = value*length_factors[from_unit]  # Initialize: value to 'meter'
  result = value_in_meter/length_factors[to_unit]   # value-in-meter to desired unit
  return round(result, 4)

# Convert between mass units by converting to gram first
def convert_mass(value: float, from_unit: str, to_unit: str):
  value_in_gram = value*mass_factors[from_unit]   # Initialize: value to 'gram'
  result = value_in_gram/mass_factors[to_unit]    # value-in-gram to desired unit
  return round(result, 4)  

# Convert between temperature units using formula-based conversion
def convert_temperature(value: float, from_unit: str, to_unit: str):
  # Step 1: Convert input to Celsius
  if from_unit == "F":
    value_in_celsius = (value-32)*5/9
  elif from_unit == "K":
    value_in_celsius = value-273.15
  else:
    value_in_celsius = value

  # Step 2: Convert Celsius to target unit
  if to_unit == "F":
    result = (value_in_celsius*9/5) + 32
  elif to_unit == "K":
    result = value_in_celsius+273.15
  else:
    result = value_in_celsius
  return round(result, 4)  
