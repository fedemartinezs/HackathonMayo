from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("mostrar_datos.html")

if __name__ == "__main__" :
    app.run(debug=True)

