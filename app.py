from flask import Flask, render_template, request, redirect, session
from logic.user_logic import UserLogic
import bcrypt
import requests

app = Flask(__name__)
app.secret_key = "Bad1secret2key3!+"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    #data = {}
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        logic = UserLogic()
        userEmail = request.form["useremail"]
        passwd = request.form["passwd"]
        userDict = logic.getUserByEmail(userEmail)
        userName = logic.getUsernameByEmail(userEmail)


        #Esta es la sección para el recaptcha
        #Esta es la secret key      
        #data["secret"] = "6LfofjMbAAAAABJIKmoHERPcYolH7pf075gITpwn"
        #data["response"]= request.form["g-recaptcha-response"]

        #Este es el link que da Google Recaptcha
        #response = requests.post("https://www.google.com/recaptcha/api/siteverify", params=data)

        #if response.status_code == 200:
        #    messageJson = response.json()


        if len(userDict) > 0:
            salt = userDict["salt"].encode("utf-8")
            hashPasswd = bcrypt.hashpw(passwd.encode("utf-8"), salt)
            dbPasswd = userDict["password"].encode("utf-8")
            #Condición de contraseñas iguales
            if hashPasswd == dbPasswd:
                #Condición del recaptcha
                #if messageJson["success"]:
                #    session["login_username"] = userName["user_name"]
                #    session["login_user"] = userEmail
                #    session["loggedIn"] = True
                #    #Caso en que contraseñas sean iguales y se haya hecho el recaptcha
                return redirect("dashboard")
                
                #else:
                #    #Caso en que las contraseñas coincidan pero no se hizo el recaptcha
                #    return redirect("login")


            else:
                #Caso en que la contraseña no es la correcta
                return redirect("login")

        else:
            #Caso en el que no se encontró el correo ingresado
            return redirect("login")
        
        return "posted login"


@app.route("/logout")
def logout():
    if session.get("loggedIn"):
        session.pop("login_user")
        session.pop("loggedIn")
        return redirect("login")
    else:
        return redirect("login")


@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if request.method == "GET":
        if session.get("loggedIn"):
            
#Esta información debe contener la información de CreateParser, y debe ser un diccionario
            #info = {"title": "ACADEMY", "description": "Drama", "release_year": 2006, "language_id": 1, "original_language_id": 5, "rental_duration": 6, "rental_rate": "0.99", "length": 86, "replacement_cost": "20.99", "rating": "PG", "special_features": "Deleted", "last_update": "2006-02-15 05:03:42"}
#1,'ACADEMY DINOSAUR','A Epic Drama of a Feminist And a Mad Scientist who must Battle a Teacher in The Canadian Rockies',2006,1,NULL,6,'0.99',86,'20.99','PG','Deleted Scenes,Behind the Scenes','2006-02-15 05:03:42'
#Método para insertar en la BD. Debe llevar la palabra clave
            #response = requests.put("http://localhost:23512/film/0", data=info)

#Método para hacer update dado un id. Debe llevar la palabra clave
            #response = requests.patch("http://127.0.0.1:5000/film/1", data=info)

#Método para hacer select dado un id. Debe llevar la palabra clave
            #response = requests.get("http://127.0.0.1:5000/film/1")

#Método para hacer un delete dado un id. Debe llevar la palabra clave
            #response = requests.delete("http://127.0.0.1:5000/film/2")


            #print (response)
            #messageJson = response.json()
            #print(messageJson)


        #user = session.get("login_user")
        #user = session.get("login_username")

        #logic = UserLogic()
        #usersDict = logic.getAllUsers()
            return render_template("dashboard.html")
        else:
            return redirect("login")

    elif request.method == "POST":
        if session.get("loggedIn"):
        #user = session.get("login_user")
        #user = session.get("login_username")

        #logic = UserLogic()
        #usersDict = logic.getAllUsers()
            return render_template("dashboard.html")
        else:
            return redirect("login")

    


@app.route("/register", methods=["GET", "POST"])
def register():
    data = {}
    if request.method == "GET":
        return render_template("register.html")

    elif request.method == "POST":
        logic = UserLogic()
        userName = request.form["username"]
        userEmail = request.form["useremail"]
        passwd = request.form["passwd"]
        confpasswd = request.form["confpasswd"]
        #userName = logic.getUsernameByEmail(userEmail)

        data["secret"] = "6LfofjMbAAAAABJIKmoHERPcYolH7pf075gITpwn"
        data["response"]= request.form["g-recaptcha-response"]
        response = requests.post("https://www.google.com/recaptcha/api/siteverify", params=data)

        if response.status_code == 200:
            messageJson = response.json()


        if passwd == confpasswd:
            salt = bcrypt.gensalt(rounds=14)
            strSalt = salt.decode("utf-8")
            encPasswd = passwd.encode("utf-8")
            hashPasswd = bcrypt.hashpw(encPasswd, salt)
            strPasswd = hashPasswd.decode("utf-8")
            #rows = logic.insertUser(userName, userEmail, strPasswd, strSalt)

            if messageJson["success"]:
                #session["login_username"] = userName["user_name"]
                session["login_user"] = userEmail
                session["loggedIn"] = True
                

                if logic.checkUsername(userName) == True:
                    rows = logic.insertUser(userName, userEmail, strPasswd, strSalt)
                    return redirect("login")

                else:
                    return redirect("register")


            else:
                #Caso en que las contraseñas coincidan pero no se hizo el recaptcha
                return redirect("register")
        else:
            return redirect("register")
        return f"posted register rows: {rows}"


if __name__ == "__main__":
    app.run(debug=True)