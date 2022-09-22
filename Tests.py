from Config import Database
import unittest
from Model import UserRegistrationRequest
from Repository import UserRepository
from Domain import Users
from Service import UserService
from View import View

class AppTest(unittest.TestCase) :
    
    __connection:Database
    __userRepository:UserRepository
    __userService:UserService

    def setUp(self) -> None:
        self.__connection = Database.getConnection()
        self.__userRepository = UserRepository(self.__connection)
        self.__userService = UserService(self.__userRepository)

        self.__userRepository.deleteAll()

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

if __name__ == "__main__" :
    unittest.main()