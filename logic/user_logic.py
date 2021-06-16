from core.pyba_logic import PybaLogic

class UserLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    def getUserByEmail(self, userEmail):
        database = self.createDatabaseObj()
        sql = (
            "SELECT user_email, password, salt " 
            + f"FROM sakila.user where user_email like '{userEmail}';")
        result = database.executeQuery(sql)

        if len(result) > 0:
            return result[0] 

        else:
            return []

    def getAllUsers(self):
        database = self.createDatabaseObj()
        sql = (
            "SELECT * FROM sakila.user;")
        result = database.executeQuery(sql)

        if len(result) > 0:
            return result 

        else:
            return []


    def insertUser(self, userName, userEmail, password, salt):
        database = self.createDatabaseObj()
        sql = (
            "INSERT INTO `sakila`.`user` "
            + "(`id`,`user_name`,`user_email`,`password`,`salt`) "
            + f"VALUES(0,'{userName}','{userEmail}','{password}','{salt}');"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def getUsernameByEmail(self, userEmail):
        database = self.createDatabaseObj()
        sql = (
            "SELECT user_name " 
            + f"FROM sakila.user where user_email like '{userEmail}';")
        result = database.executeQuery(sql)

        if len(result) > 0:
            return result[0] 

        else:
            return []

    def checkUsername(self, username):
        database = self.createDatabaseObj()
        sql = (
            "SELECT * " 
            + f"FROM sakila.user where user_name like '{username}';")
        result = database.executeQuery(sql)

        if len(result) > 0:
            return False 

        else:
            return True