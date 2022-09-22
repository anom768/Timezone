from Domain import Users
from Config import Database

class UserRepository() :

    def __init__(self, connection:Database) -> None:
        self.__connection = connection

    def save(self, user:Users) -> Users :
        cursor = self.__connection.cursor()
        cursor.execute("INSERT INTO users(username, password) VALUES (:username, :password)", {
            'username' : user.username,
            'password' : user.password
        })
        self.__connection.commit()
        return user
    
    def findByUsername(self, username:str) -> Users :
        cursor = self.__connection.cursor()
        statement = cursor.execute("SELECT id, username, password FROM users WHERE username = :username", {
            'username' : username
        })
        row = statement.fetchone()
        if row :
            user = Users()
            user.id = row[0]
            user.username = row[1]
            user.password = row[2]
            return user
        else :
            return None
    
    def deleteAll(self) :
        self.__connection.execute("DELETE FROM users")