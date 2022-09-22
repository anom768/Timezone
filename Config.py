from abc import ABC, abstractmethod
import sqlite3

class Database(ABC) :

    @abstractmethod
    def getConnection() :
        return sqlite3.connect('timezone')