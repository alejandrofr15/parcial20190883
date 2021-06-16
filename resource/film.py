from flask_restful import Resource, reqparse
from logic.film_logic import FilmLogic

class Film(Resource):
    def __init__(self):
        self.film_put_args = self.createParser()

    #Tener cuidado con el type
    def createParser(self):
        args = reqparse.RequestParser()
        args.add_argument("title", type=str, help= "Título")
        args.add_argument("description", type=str, help= "Descripción")
        args.add_argument("release_year", type=int, help= "Año se estreno")
        args.add_argument("language_id", type=int, help= "Id del lenguaje")
        args.add_argument("original_language_id", type=int, help= "Id del lenguaje original")
        args.add_argument("rental_duration", type=int, help= "Duración de la renta")
        args.add_argument("rental_rate", type=str, help= "Clasificación de la renta")
        args.add_argument("length", type=int, help= "Duración")
        args.add_argument("replacement_cost", type=str, help= "Costo de reemplazo")
        args.add_argument("rating", type=str, help= "Calificación")
        args.add_argument("special_features", type=str, help= "Extras")
        args.add_argument("last_update", type=str, help= "Última modificación")
        return args

    def get(self, id):
        logic = FilmLogic()
        result = logic.getFilmById()


        if len(result) == 0:
            return {}

        else:
            return result[0], 200

    #Tener cuidado con el nombre del args
    def put(self, id):
        film = self.film_put_args.parse_args()
        logic = FilmLogic()
        rows = logic.insertFilm(film)
        return {"rowsAffected": rows}, 200

    #Tener cuidado con el nombre del args
    def patch(self, id):
        film = self.film_put_args.parse_args()
        logic = FilmLogic()
        rows = logic.updateFilm(id, film)
        return {"rowsAffected": rows}, 200
    
    def delete(self, id):
        logic = FilmLogic()
        rows = logic.deleteFilm(id)
        return {"rowsAffected": rows}, 200
