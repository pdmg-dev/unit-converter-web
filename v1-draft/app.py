from flask import Flask, render_template, request
from converter import convert_length, convert_weight

app = Flask(__name__)

# HOME route
@app.route('/')
def home():
  return '''
  <h2>Welcome to Unit Converter</h2>
  <ul>
    <li><a href="./length">Length</a></li>
    <li><a href="./weight">Weight</a></li>
    <li><a href="./temperature">Temperature</a></li>
  </ul>
  '''

@app.route('/length', methods=['GET', 'POST'])
def length():
  result = None
  if request.method == 'POST':
    try:
      value = float(request.form['value'])
      from_unit = request.form['from_unit']
      to_unit = request.form['to_unit']
      result = convert_length(value, from_unit, to_unit)
    except ValueError:
      result = "Invalid input or unit."
  return render_template('length.html', result=result)

@app.route('/weight', methods=['GET', 'POST'])
def weight():
  result = None
  if request.method == 'POST':
    try:
      value = float(request.form['value'])
      from_unit = request.form['from_unit']
      to_unit = request.form['to_unit']
      result = convert_weight(value, from_unit, to_unit)
    except ValueError:
      result = "Invalid input or unit."
  return render_template('weight.html', result=result)

from converter import convert_length, convert_weight, convert_temperature


@app.route('/temperature', methods=['GET', 'POST'])
def temperature():
    result = None
    if request.method == 'POST':
      try:
        value = float(request.form['value'])
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']
        result = convert_temperature(value, from_unit, to_unit)
      except ValueError:
        result = "Invalid input or unit."
    return render_template('temperature.html', result=result)

if __name__ == '__main__':
  app.run(debug=True)