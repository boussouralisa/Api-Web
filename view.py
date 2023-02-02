# from app import app
from flask import Flask
import sqlite3
from flask import render_template
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__,static_folder="static",
            template_folder="templates")

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/Contact')
def contact():
	return render_template("contact.html")

@app.route('/Panier')
def panier():
	conn = sqlite3.connect("glycemic_index.db")
	c = conn.cursor()
	c.execute("SELECT * FROM panier where meal_id = 1")
	data = c.fetchall()
	conn.close()
	return render_template("panier.html", data=data)

@app.route('/Ajoute')
def Ajoute():
	return render_template("AjoutsPlats.html")

#swagger configs
SWAGGER_URL = "/swagger"
API_URL = "/static/swagger.json"
SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
	SWAGGER_URL,
	API_URL,
	config={
		"app_name" : "LISTE API"
	}
	)

app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix= SWAGGER_URL)

if __name__ == '__main__':
    app.run(debug=True)
