from Model import UserRegistrationRequest
from Service import UserService

class View() :

    __userService:UserService

    def __init__(self, userService:UserService) -> None:
        self.__userService = userService

    def run(self) :
        print("="*10 + " T I M E Z O N E " + "="*10)
        while True :
            print("[1] Register")
            print("[2] Login")
            print("[0] Exit")

            choose = input("Choose Menu: ")
            if choose == "1" :
                self.register()
            elif choose == "2" :
                pass
            elif choose == "0" :
                break
            else :
                print("[!] ERROR: INVALID INPUT !\n")

        print("="*10 + " E N D E D " + "="*10 + "\n")

    def register(self) :
        print("\n" + "="*10 + " R E G I S T E R " + "="*10)
        request = UserRegistrationRequest()
        request.username = input("[+] Username: ")
        request.password = input("[+] Password: ")
        request.passwordVerify = input("[+] Password verify: ")

        try :
            self.__userService.register(request)
            print("[#] Registration Success\n")
        except Exception as exception :
            print("[!] ERROR: " , exception, "\n")