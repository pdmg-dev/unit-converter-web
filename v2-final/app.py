from flask import Flask, render_template, request
from converter import convert_length, convert_mass, convert_temperature

# Initialize the Flask app
app = Flask(__name__)

# Helper function to handle unit conversion
def handle_conversion(converter):
  result = None
  unit = None
  
  # Get from data
  value = float(request.form["value"])
  from_unit = request.form["from_unit"]
  to_unit = request.form["to_unit"]
   
  # Call the appropriate converter function
  result = converter(value, from_unit, to_unit)
  unit = to_unit

  return result, unit

# Make 'request' available in templates
@app.context_processor
def inject_request():
    return dict(request=request)

# Route for home - redirects to length converter
@app.route("/", methods=["GET", "POST"])
def home():
    result, unit = (handle_conversion(convert_length) if request.method == "POST" else (None, None))
    return render_template("length.html", result=result, unit=unit, active_page="length")

# Route for length conversion
@app.route("/length", methods=["GET", "POST"])
def length():
  result, unit = (handle_conversion(convert_length) if request.method == "POST" else (None, None))
  return render_template("length.html", result=result, unit=unit, active_page="length")

# Route for mass conversion
@app.route("/mass", methods=["GET", "POST"])
def mass():
  result, unit = (handle_conversion(convert_mass) if request.method == "POST" else (None, None))
  return render_template("mass.html", result=result, unit=unit, active_page="mass")

# Route for temperature conversion
@app.route("/temperature", methods=["GET", "POST"])
def temperature():
  result, unit = (handle_conversion(convert_temperature) if request.method == "POST" else (None, None))
  return render_template("temperature.html", result=result, unit=unit, active_page="temperature")

# Run the app in development mode
if __name__ == "__main__":
  app.run(debug=True)