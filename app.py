from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from utils.db import db
from routes.clienteroute import clientes
from routes.productoroute import productos
from routes.ventaroute import ventas


app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5000"}})
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/informacion'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
app.register_blueprint(clientes)
app.register_blueprint(productos)
app.register_blueprint(ventas)


@cross_origin()
@app.route('/')
def index():
    return jsonify({'message': 'welcome'})


def pagina_no_encontrada(error):
    return "<h1>La pagina a la que intentas acceder no existe...</h1>"


if __name__ == "__main__":
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True, host="0.0.0.0")
