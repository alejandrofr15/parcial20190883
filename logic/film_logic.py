from core.pyba_logic import PybaLogic

class FilmLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    #En los values, los valores que sean string deben llevar '', los números no. Por ejemplo, la diferencia entre nombre e ingresos.
    #'{empresa['nombre']}'. empresa es por el nombre del parámetro, nombre es por la información que se da la date de consume_api.py
    def insertFilm(self, film):
        database = self.createDatabaseObj()
        sql = (
            f"INSERT INTO `sakila`.`film` "
         + f"(`film_id`, `title`, `description`, `release_year`, `language_id`, `original_language_id`, `rental_duration`, `rental_rate`, `length`, `replacement_cost`, `rating`, `special_features`, `last_update`) " 
         + f"VALUES (0, '{film['title']}', '{film['description']}', {film['release_year']}, {film['language_id']}, {film['original_language_id']}, {film['rental_duration']}, '{film['rental_rate']}', {film['length']}, '{film['replacement_cost']}', '{film['rating']}', '{film['special_features']}', '{film['last_update']}');"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    #En los values, los valores que sean string deben llevar '', los números no. Por ejemplo, la diferencia entre nombre e ingresos.
    def getFilmById(self, id):
        database = self.createDatabaseObj()
        sql = (
            f"SELECT * FROM sakila.film WHERE film_id = {id};"
        )
        result = database.executeQuery(sql)
        return result


    #En los values, los valores que sean string deben llevar '', los números no. Por ejemplo, la diferencia entre nombre e ingresos.
    #'{empresa['nombre']}'. empresa es por el nombre del parámetro, nombre es por la información que se da la date de consume_api.py
    def updateFilm(self, id, film):
        database = self.createDatabaseObj()
        sql = (
            "UPDATE `sakila`.`film` "
            + f"SET `title` = '{film['title']}', `description` = '{film['description']}', `release_year` = {film['release_year']}, `language_id` = {film['language_id']}, `original_language_id` = {film['original_language_id']}, `rental_duration` = {film['rental_duration']}, `rental_rate` = '{film['rental_rate']}', `length` = {film['length']}, `replacement_cost` = '{film['replacement_cost']}', `rating` = '{film['rating']}', `special_features` = '{film['special_features']}', `last_update` = '{film['last_update']}' "
            + f"WHERE `id` = {id};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    #En los values, los valores que sean string deben llevar '', los números no. Por ejemplo, la diferencia entre nombre e ingresos.
    #'{empresa['nombre']}'. empresa es por el nombre del parámetro, nombre es por la información que se da la date de consume_api.py
    def deleteFilm(self, id):
        database = self.createDatabaseObj()
        sql = (
            f"DELETE FROM sakila.film WHERE id = {id};"
            )
        rows = database.executeNonQueryRows(sql)
        return rows
