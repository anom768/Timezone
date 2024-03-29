from Domain import Users, Ticket
from Model import UserLoginRequest, UserLoginResponse, UserRegistrationRequest, UserRegistrationResponse
from Repository import TicketRepository, UserRepository

class UserService() :
    __userRepository:UserRepository
    __ticketRepository:TicketRepository

    def __init__(self, userRepository:UserRepository, ticketRepository:TicketRepository) -> None:
        self.__userRepository = userRepository
        self.__ticketRepository = ticketRepository
    
    def register(self, request:UserRegistrationRequest) -> UserRegistrationResponse :
        self.__validateRegistrationRequest(request)

        try :
            user = Users()
            user.username = request.username
            user.password = request.password
            self.__userRepository.save(user)

            ticket = Ticket()
            ticket.username = user.username
            ticket.game = "Guess Number"
            ticket.ticket = 0
            self.__ticketRepository.save(ticket)

            ticket.game = "Roscipa"
            self.__ticketRepository.save(ticket)

            ticket.game = "Roll Number"
            self.__ticketRepository.save(ticket)

            response = UserRegistrationResponse()
            response.user = user
            return response
        except :
            raise Exception("Registration Failed")
    
    def __validateRegistrationRequest(self, request:UserRegistrationRequest) -> None :
        if (request.username == None or request.password == None or request.passwordVerify == None or
            request.password == "" or request.username == "" or request.passwordVerify == "") :
                raise Exception("Username and password can not blank")

        if (request.password != request.passwordVerify) :
            raise Exception("Password not same")

        user = self.__userRepository.findByUsername(request.username)
        if (user != None) :
            raise Exception("Username is already exists")
    
    def login(self, request:UserLoginRequest) -> UserLoginResponse :
        user = self.__validateLoginRequest(request)

        response = UserLoginResponse()
        response.user = user

        return response

    def __validateLoginRequest(self, request:UserLoginRequest) :
        if (request.username == None or request.password == None or
            request.password == "" or request.username == "") :
                raise Exception("Username and password can not blank")
        
        user = self.__userRepository.findByUsername(request.username)
        if user == None :
            raise Exception("Username or password is wrong")
        
        if request.password != user.password :
            raise Exception("Username or password is wrong")
        
        return user