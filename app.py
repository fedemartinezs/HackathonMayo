import pandas as pd
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def home():
    df = pd.read_csv('datos.txt', parse_dates=['fecha'], dayfirst=True)
    df.to_string()

    def parse_to_dicc(datos):
        diccionary = datos.to_dict(orient='records')
        print(diccionary)

    parse_to_dicc(df)
    
    return render_template("mostrar_datos.html")
#holaaa







