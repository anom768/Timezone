from abc import ABC, abstractmethod
import sqlite3

class Database(ABC) :

    @abstractmethod
    def getConnection() :
        return sqlite3.connect('timezone')
    
    @abstractmethod
    def create() :
        connection = Database.getConnection()
        cursor = connection.cursor()

        sql = """
            CREATE TABLE ticket
            (
                id int auto_increment,
                user varchar(255) not null,
                game varchar(255) not null,
                ticket int not null,
                primary key(id, user, game)
            )"""
        cursor.execute(sql)
        connection.commit()
        cursor.close()
        print("suskses")