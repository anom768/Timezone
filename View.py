from Model import UserLoginRequest, UserRegistrationRequest
from Repository import TicketRepository
from Service import UserService
import random

class View() :

    __userService:UserService
    __ticketRepository:TicketRepository

    def __init__(self, userService:UserService, ticketRepository:TicketRepository) -> None:
        self.__userService = userService
        self.__ticketRepository = ticketRepository
        self.__ticket = 0

    def run(self) :
        print("="*10 + " T I M E Z O N E " + "="*10)
        while True :
            print("[1] Register")
            print("[2] Login")
            print("[q] Exit")

            choose = input("Choose Menu: ")
            if choose == "1" :
                self.register()
            elif choose == "2" :
                self.login()
            elif choose == "q" :
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
        while True :
            print("\n" + "="*10 + f" W E L C O M E , {username} " + "="*10)
            print(f"Total ticket: {self.__ticketRepository.total(username)}")
            print("[1] Guess Number")
            print("[2] ROSCIPA")
            print("[3] Rolling Number")
            print("[q] Logout")

            choose = input("Choose Menu: ")
            if choose == "1" :
                self.guessNumber(username)
            elif choose == "2" :
                print("roscipa")
            elif choose == "3" :
                print("rolling number")
            elif choose == "q" :
                print("="*10 + " E N D E D " + "="*10 + "\n")
                quit()
            else :
                print("[!] ERROR: INVALID INPUT !\n")
                
    # ================= GUESS NUMBER =================
    def guessNumber(self, username:str) :
        print("\n" + "="*10 + " G U E S S  N U M B E R " + "="*10)
        input ("[#] Press enter to play: ")
        self.playGuessNumber(username, number=None)
    
    def playGuessNumber(self, username:str , number:int) :   
        if number == None :
            number = random.randint(0, 9)

        guess = input("[#] (q for exit) Guess number 0 - 9: ")
        if guess.isdigit():
            guess = int(guess)
            self.playingGuessNumber(username, guess, number)
        elif guess.lower() == 'q':
            print(f"[$] CONGRATULATION You Got: {self.__ticket} ticket.")
            self.__ticketRepository.update(username, "Guess Number", self.__ticket)
            self.__ticket = 0
        else:                                                                                                                                                                                                                                                                                                                                                                                                                                         
            print("[!] ERROR: INVALID INPUT !\n")
            self.playGuessNumber(username, number)

    def playingGuessNumber(self, username:str, choose:int, number:int) :
        if choose == number :
            print("[#] CORRECT: The number is:", number)
            self.__ticket += 1
            self.playAgainGuessNumber(username)
        elif choose > number:
            print("[!] WRONG: Number too big")
            self.playGuessNumber(username, number)
        else:
            print("[!] WRONG: Number too small")
            self.playGuessNumber(username, number)
    
    def playAgainGuessNumber(self, username:str) :
        choose = input("[?] Play again (y/n): ")
        if choose.lower() == "y":
            self.playGuessNumber(username, number=None)
        elif choose.lower() == "n":
            print(f"[$] CONGRATULATION You Got: {self.__ticket} ticket.")
            self.__ticketRepository.update(username, "Guess Number", self.__ticket)
            self.__ticket = 0
        else:
            print("[!] ERROR: INVALID INPUT !\n")
            self.playAgainGuessNumber(username)