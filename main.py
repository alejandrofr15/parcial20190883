from flask import Flask
from flask_restful import Api
from resource.film import Film


app = Flask(__name__)
api = Api(app)

#Empresa es la palabra clave
api.add_resource(Film, "/film/<int:id>")

if __name__ == "__main__":
    app.run(debug=True, port=23512)