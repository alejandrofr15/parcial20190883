import requests

#Esta información debe contener la información de CreateParser, y debe ser un diccionario
info = {"title": "ACADEMY", "description": "Drama", "release_year": 2006, "language_id": 1, "original_language_id": 5, "rental_duration": 6, "rental_rate": "0.99", "length": 86, "replacement_cost": "20.99", "rating": "PG", "special_features": "Deleted", "last_update": "2006-02-15 05:03:42"}
#1,'ACADEMY DINOSAUR','A Epic Drama of a Feminist And a Mad Scientist who must Battle a Teacher in The Canadian Rockies',2006,1,NULL,6,'0.99',86,'20.99','PG','Deleted Scenes,Behind the Scenes','2006-02-15 05:03:42'
#Método para insertar en la BD. Debe llevar la palabra clave
#def insertFilm(self):
response = requests.put("http://localhost:23512/film/0", data=info)

#Método para hacer update dado un id. Debe llevar la palabra clave
#response = requests.patch("http://127.0.0.1:5000/film/1", data=info)

#Método para hacer select dado un id. Debe llevar la palabra clave
#response = requests.get("http://127.0.0.1:5000/film/1")

#Método para hacer un delete dado un id. Debe llevar la palabra clave
#response = requests.delete("http://127.0.0.1:5000/film/2")


print (response)
messageJson = response.json()
print(messageJson)

#print("name:" + str(messageJson['name']))
#print("views:" + str(messageJson['views']))
#print("likes:" + str(messageJson['likes']))
