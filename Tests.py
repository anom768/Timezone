from Config import Database
import unittest
from Model import UserLoginRequest, UserRegistrationRequest
from Repository import TicketRepository, UserRepository
from Domain import Ticket, Users
from Service import UserService

class AppTest(unittest.TestCase) :
    
    __connection:Database
    __userRepository:UserRepository
    __userService:UserService
    __ticketRepository:TicketRepository

    def setUp(self) -> None:
        self.__connection = Database.getConnection()
        self.__userRepository = UserRepository(self.__connection)
        self.__ticketRepository = TicketRepository(self.__connection)
        self.__userService = UserService(self.__userRepository, self.__ticketRepository)

        self.__userRepository.deleteAll()
        self.__ticketRepository.deleteAll()

    # DATABASE TEST
    def testGetConnection(self) :
        self.assertIsNotNone(self.__connection)
    
    # USER REPOSITORY TEST
    def testSave(self) :
        user = Users()
        user.username = "anom"
        user.password = "rahasia"
        result = self.__userRepository.save(user)

        self.assertEqual(user.username, result.username)
        self.assertEqual(user.password, result.password)
    
    def testFindByUsernameNotFound(self) :
        result = self.__userRepository.findByUsername("notfound")

        self.assertIsNone(result)
    
    def testFindByUsernameSuccess(self) :
        user = Users()
        user.username = "anom"
        user.password = "rahasia"
        self.__userRepository.save(user)
        result = self.__userRepository.findByUsername(user.username)
        
        self.assertIsNotNone(result)
        self.assertEqual(user.username, result.username)
        self.assertEqual(user.password, result.password)
    
    # # USER SERVICE TEST
    def testRegistrationNone(self) :

        request = UserRegistrationRequest()
        request.username = None
        request.password = None
        request.passwordVerify = None
        
        self.assertRaises(Exception, self.__userService.register, request)

    def testRegistrationDiffPassword(self) :

        request = UserRegistrationRequest()
        request.username = "anom"
        request.password = "rahasia"
        request.passwordVerify = "123"
        
        self.assertRaises(Exception, self.__userService.register, request)
    
    def testRegistrationDuplicate(self) :
        user = Users()
        user.username = "anom"
        user.password = "rahasia"
        self.__userRepository.save(user)

        request = UserRegistrationRequest()
        request.username = "anom"
        request.password = "rahasia"
        request.passwordVerify = "rahasia"
        
        self.assertRaises(Exception, self.__userService.register, request)
    
    def testRegistrationSuccess(self) :

        request = UserRegistrationRequest()
        request.username = "anom"
        request.password = "rahasia"
        request.passwordVerify = "rahasia"
        result = self.__userService.register(request)

        self.assertEqual(request.username, result.user.username)
        self.assertEqual(request.password, result.user.password)
    
    def testLoginBlank(self) :
        request = UserLoginRequest()
        request.username = ""
        request.password = ""

        self.assertRaises(Exception, self.__userService.login, request)
    
    def testLoginWrongUsername(self) :
        request = UserLoginRequest()
        request.username = "wrong"
        request.password = "rahasia"

        self.assertRaises(Exception, self.__userService.login, request)
    
    def testLoginWrongPassword(self) :
        request = UserLoginRequest()
        request.username = "anom"
        request.password = "wrong"

        self.assertRaises(Exception, self.__userService.login, request)
    
    def testLoginSuccess(self) :
        user = Users()
        user.username = "anom"
        user.password = "rahasia"
        self.__userRepository.save(user)

        request = UserLoginRequest()
        request.username = "anom"
        request.password = "rahasia"
        result = self.__userService.login(request)

        self.assertEqual(user.username, result.user.username)
        self.assertEqual(user.password, result.user.password)
    
    # TICKET REPOSITORY TEST
    def testSave(self) :
        ticket = Ticket()
        ticket.username = "anom"
        ticket.game = "Guess Number"
        ticket.ticket = 0
        result = self.__ticketRepository.save(ticket)

        self.assertEqual(ticket.username, result.username)
        self.assertEqual(ticket.game, result.game)
        self.assertEqual(ticket.ticket, result.ticket)
    
    def testUpdate(self) :
        ticket = Ticket()
        ticket.username = "anom"
        ticket.game = "Guess Number"
        ticket.ticket = 10
        self.__ticketRepository.save(ticket)

        self.__ticketRepository.update(ticket.username, ticket.game, 2)

        result = self.__ticketRepository.findTicket(ticket.username, ticket.game)
        self.assertEqual(12, result)
        self.__ticketRepository.deleteAll()
    
    # JUST FOR DELETE ALL
    def testTrue(self) :
        self.__userRepository.deleteAll()
        self.assertTrue(True)

if __name__ == "__main__" :
    unittest.main()