from Model import UserLoginRequest, UserRegistrationRequest
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
                self.login()
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
    
    def login(self) :
        print("\n" + "="*10 + " L O G I N " + "="*10)
        request = UserLoginRequest()
        request.username = input("[+] Username: ")
        request.password = input("[+] Password: ")

        try :
            response = self.__userService.login(request)
            self.dashboard(response.user.username)
        except Exception as exception :
            print("[!] ERROR: " , exception, "\n")
    
    def dashboard(self, username:str) :
        print("\n" + "="*10 + f" W E L C O M E , {username} " + "="*10)
        while True :
            print("[1] Guess Number")
            print("[2] ROSCIPA")
            print("[3] Rolling Number")
            print("[0] Logout")

            choose = input("Choose Menu: ")
            if choose == "1" :
                print("guess number")
            elif choose == "2" :
                print("roscipa")
            elif choose == "3" :
                print("rolling number")
            elif choose == "0" :
                print("="*10 + " E N D E D " + "="*10 + "\n")
                quit()
            else :
                print("[!] ERROR: INVALID INPUT !\n")