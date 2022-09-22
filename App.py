from View import View
from Config import Database
from Repository import UserRepository
from Service import UserService

userRepository = UserRepository(Database.getConnection())
userService = UserService(userRepository)

app = View(userService)

if __name__ == "__main__" :
    app.run()