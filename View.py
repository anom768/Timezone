from ast import Or
from re import T
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
        self.__user_win = 0
        self.__com_win = 0
        self.__draw = 0
        self.__options = ["rock", "scissor", "papper"]

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
                self.playGuessNumber(username)
            elif choose == "2" :
                self.playRoscipa(username)
            elif choose == "3" :
                self.playRollNumber(username)
            elif choose == "q" :
                print("="*10 + " E N D E D " + "="*10 + "\n")
                quit()
            else :
                print("[!] ERROR: INVALID INPUT !\n")
    
    # ================================================
    # ================= GUESS NUMBER =================
    # ================================================
    def playGuessNumber(self, username:str) :
        print("\n" + "="*10 + " G U E S S  N U M B E R " + "="*10)
        input ("[#] Press enter to play: ")
        self.guessNumber(username, number=None)
    
    def guessNumber(self, username:str , number:int) :   
        if number == None :
            number = random.randint(0, 9)

        guess = input("[#] (q for exit) Guess number 0 - 9: ")
        if guess.isdigit():
            guess = int(guess)
            self.validateGuessNumber(username, guess, number)
        elif guess.lower() == 'q':
            self.countScore(username, "Guess Number")
        else:                                                                                                                                                                                                                                                                                                                                                                                                                                         
            print("[!] ERROR: INVALID INPUT !\n")
            self.guessNumber(username, number)

    def validateGuessNumber(self, username:str, choose:int, number:int) :
        if choose == number :
            print("[#] CORRECT: The number is:", number)
            self.__ticket += 1
            self.playAgain(username, "Guess Number", number)
        elif choose > number:
            print("[!] WRONG: Number too big")
            self.guessNumber(username, number)
        else:
            print("[!] WRONG: Number too small")
            self.guessNumber(username, number)
    
    # ================================================
    # ================= R O S C I P A ================
    # ================================================
    def playRoscipa(self, username:str) :
        print("\n" + "="*10 + " ROCK SCISSOR PAPPER " + "="*10)
        input ("[#] Press enter to play: ")
        self.choiceRoscipa(username)
    
    def choiceRoscipa(self, username:str) :
        user_choice = input("[#] Choice (Rock)||(Scissor)||(Papper)||(Q)uit: ").lower()
        if user_choice == "q":
             self.countScore(username, "Roscipa")
        elif user_choice not in self.__options:
            print("[!] ERROR: INVALID INPUT !\n")
            self.choiceRoscipa(username)
        else :
            self.validateChoiceRoscipa(user_choice, username)
    
    def validateChoiceRoscipa(self, user_choice:str, username:str) :
        com_choice = self.__options[random.randint(0, 2)]
        
        print("    =>   Computer Choice     : ", com_choice)
        print(f"    =>   {username} Choice         : ", user_choice)

        if (user_choice == "rock" and com_choice == "scissor" or
            user_choice == "scissor" and com_choice == "papper" or
            user_choice == "papper" and com_choice == "rock") :
            print("    =>   Result              :  YOU WON!")
            self.__user_win += 1
        elif user_choice == com_choice:
            print("    =>   Result              :  DRAW!")
            self.__draw += 1
        else:
            print("    =>   Result              :  YOU LOSE!")
            self.__com_win += 1
        self.playAgain(username, "Roscipa", None)

    # ================================================
    # ================= ROLL NUMBER ==================
    # ================================================
    def playRollNumber(self, username:str) :
        print("\n" + "="*10 + " R O L L I N G   N U M B E R " + "="*10)
        input ("[#] Press enter to play: ")
        self.rollNumber(username)
    
    def rollNumber(self, username:str) :
        roll = input("[#] Press Enter to Roll || (Q)uit: ").lower()
        if roll == "q":
            self.countScore(username, "Roll Number")
        else :
            number1 = random.randint(0,9)
            number2 = random.randint(0,9)
            number3 = random.randint(0,9)
            print("\n")
            print("="*33)
            print("="*10,f" {number1} | {number2} | {number3} ", "="*10)
            print("="*33)
            print("\n")
            self.validateRollNumber(number1, number2, number3, username)
    
    def validateRollNumber(self, number1:int, number2:int, number3:int, username:str) :
        if number1 != number2 and number2 != number3 and number1 != number3:
            print("[#] No number same. Ticket + 0",)
        elif number1 == number2 == number3:
            print("[$] CONGRATULATION JACKPOT. Ticket + 10")
            self.__ticket += 10
        else:
            print("[#] Two numbers same. Ticket + 1")
            self.__ticket += 1
        self.rollNumber(username)
    
    # ================================================
    # =================  S C O R E  ==================
    # ================================================
    def playAgain(self, username:str, game:str, number:int) :
        choose = input("[?] Play again (y/n): ")
        if choose.lower() == "y" and game == "Roscipa" :
            self.choiceRoscipa(username)
        elif choose.lower() == "y" and game == "Guess Number" :
            self.guessNumber(username, number)
        elif choose.lower() == "n":
            self.countScore(username, game)
        else:
            print("[!] ERROR: INVALID INPUT !\n")
            if game == "Roscipa" :
                self.playAgain(username, game, number)
            else :
                self.playAgain(username, game, number)

    def countScore(self, username:str, game:str) :
        if game == "Roscipa" :
            print("    Total Score : ")
            print(f"    {username}     = {self.__user_win} WON")
            print(f"    Computer = {self.__com_win} WON")
            print(f"    Draw     = {self.__draw} Draw")
            self.__ticket = self.__user_win
        print(f"[$] CONGRATULATION You Got: {self.__ticket} ticket.")
        self.__ticketRepository.update(username, game, self.__ticket)
        self.__ticket = 0
        self.__user_win = 0
        self.__com_win = 0
        self.__draw = 0