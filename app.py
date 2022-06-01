from flask import Flask
from flask.templating import render_template
import pandas as pd
import json

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route('/datos')
def home():
    df = pd.read_csv('datos.txt')
    df.to_string()

    def parse_to_dicc(datos):
        diccionary = datos.to_dict(orient='records')
        return diccionary

    data = parse_to_dicc(df)

    datajson = json.dumps(data)
    
    return render_template("mostrar_datos.html", datajson=datajson )

@app.route('/datos-15')
def home2():
    df = pd.read_csv('datos.txt')
    df.to_string()

    def parse_to_dicc(datos):
        diccionary = datos.to_dict(orient='records')
        return diccionary

    data15 = parse_to_dicc(df)

    df15 = json.dumps(data15)

    
    return render_template("datos_15.html", df15=df15 )

if __name__ == "__main__" :
    app.run(debug=True)




