from View import View
from Config import Database
from Repository import UserRepository, TicketRepository
from Service import UserService

userRepository = UserRepository(Database.getConnection())
ticketRepository = TicketRepository(Database.getConnection())
userService = UserService(userRepository, ticketRepository)

app = View(userService, ticketRepository)

if __name__ == "__main__" :
    app.run()