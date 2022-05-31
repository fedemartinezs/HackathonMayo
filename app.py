from flask import Flask
from flask.templating import render_template
import pandas as pd
import json

app = Flask(__name__)

@app.route('/')
def home():
    df = pd.read_csv('datos.txt')
    df.to_string()

    def parse_to_dicc(datos):
        diccionary = datos.to_dict(orient='records')
        return diccionary

    data = parse_to_dicc(df)

    datajson = json.dumps(data)
    
    return render_template("grafico.html", datajson=datajson )

if __name__ == "__main__" :
    app.run(debug=True)
#holaaa


