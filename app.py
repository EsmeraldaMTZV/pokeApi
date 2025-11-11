from flask import Flask, render_template, request, redirect, url_for, flash, session
import requests

app = Flask(__name__)
app.secret_key = 'mi_clave_secreta'
API = "https://pokeapi.co/api/v2/pokemon/"

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search_pokemon():
    pokemon_name = request.form.get ('pokemon_name', '').strip().lower()
    
    if not pokemon_name:
        flash('Ingresa un nombre correcto de Pokemon')
        return redirect(url_for('index'))
    
        resp= request.get(f"{API}{pokemon_name}")
        if resp.status_code == 200:
            pokemon_data= resp.json()
    
    if __name__ == "__main__":
        app.run(debug=True)