from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/f2c/<value>")
def convert_temperature(value):
    try:
       fahrenheit = float(value)
       celsius = (fahrenheit - 32) * 5 / 9
       celsius = round(celsius, 3)  # Round to three decimal places
    except:
       return render_template('index.html')

    return render_template('convert1.html', var1=value, var2=celsius)


