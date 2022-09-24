from Domain import Ticket, Users
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

class TicketRepository() :
    def __init__(self, connection:Database) -> None:
        self.__connection = connection
        self.__connection.commit()
    
    def save(self, ticket:Ticket) -> Ticket :
        cursor = self.__connection.cursor()
        cursor.execute("INSERT INTO ticket(user, game, ticket) VALUES(:user, :game, :ticket)", {
            'user' : ticket.username,
            'game' : ticket.game,
            'ticket' : ticket.ticket
        })
        self.__connection.commit()
        return ticket
    
    def update(self, username:str, game:str, ticket:int) :
        cursor = self.__connection.cursor()
        cursor.execute("UPDATE ticket SET ticket = ticket + :ticket WHERE user = :user AND game = :game", {
            'user' : username,
            'game' : game,
            'ticket' : ticket
        })
        self.__connection.commit()

    def findTicket(self, username:str, game:str) -> int :
        cursor = self.__connection.cursor()
        statement = cursor.execute("SELECT ticket from ticket WHERE user = :user AND game = :game", {
            'user' : username,
            'game' : game
        })
        row = statement.fetchone()
        if row :
            return row[0]
        else :
            return None
    
    def total(self, username:str) -> int :
        cursor = self.__connection.cursor()
        cursor.execute("SELECT SUM(ticket) FROM ticket WHERE user = :user", {
            'user' : username
        })
        row = cursor.fetchone()
        return int(row[0])
    
    def deleteAll(self) :
        self.__connection.execute("DELETE FROM ticket")
        self.__connection.commit()