import random
import os
from time import sleep


class Casino:
    player_name = ''
    cls_screen = ''
    player_balance = 0.0
    bid_amount = 0.0
    guess = 0

    def clear(self):
        self.cls_screen = os.system('clear')

    @staticmethod
    def greeting():
        print('_____________________________________________________')
        print('_______WELCOME TO CASINO GUESSING NUMBERS GAME_______')
        print('-----------------------------------------------------')

    def player_config(self):
        self.player_name = input('ENTER YOUR FULL NAME : ')
        try:
            self.player_balance = float(input('ENTER YOUR BALANCE  : $'))
            print('-----------------------------------------------------')
            while self.player_balance < 10:
                print('SORRY, YOUR BALANCE SHOULD BE GREATER THAN $10')
                self.player_balance = float(input('RE ENTER YOUR BALANCE  : $'))
                print('-----------------------------------------------------')

        except ValueError:
            print('ERROR!!. . THE VALUE OF BALANCE SHOULD BE ONLY NUMBERS')

    def game_menu(self):
        casino.clear()
        print('_____________________________________________________')
        print(f'YOUR FULL NAME : {self.player_name}\nYour CURRENT BALANCE : ${self.player_balance}')
        print('-----------------------------------------------------')

    def game_setup(self):
        while True:
            hidden_number = random.randint(1, 10)

            self.game_menu()
            start = input(f'{self.player_name}, ARE YOUR READY TO START THE GAME ( Y | N ? : ')

            if start == 'y' or start == 'Y':
                self.game_menu()

                self.bid_amount = float(input('ENTER YOUR BID AMOUNT : $'))

                while self.bid_amount < 10:
                    self.game_menu()
                    print('SORRY, YOUR BID SHOULD SHOULD BE $10 AT LEAST TO PLAY!!!')
                    self.bid_amount = float(input('RE ENTER YOUR BID AMOUNT : $'))

                while self.bid_amount > self.player_balance:
                    self.game_menu()
                    print('SORRY, THE BID AMOUNT IS GREATER THAN YOUR BALANCE!!!')
                    self.bid_amount = float(input('RE ENTER YOUR BID AMOUNT : $'))

                self.guess = int(input('TRY TO GUESS THE NUMBER BETWEEN 1 - 10 : '))

                while self.guess <= 0 or self.guess > 10:
                    self.game_menu()
                    print('SORRY, THE GUESS NUMBER SHOULD BE BETWEEN 1 - 10!!!')
                    self.guess = int(input('TRY TO GUESS THE NUMBER BETWEEN 1 - 10 : '))

                if self.guess == hidden_number:
                    self.game_menu()
                    self.player_balance += self.bid_amount * 7
                    print(f'CONGRATULATIONS YOU GUESSED THE NUMBER. AND YOU WON : ${self.bid_amount * 7}')
                    sleep(2)

                else:
                    self.game_menu()
                    self.player_balance -= self.bid_amount
                    print(
                        f'OOPS GOOD LUCK NEXT TIME. THE RIGHT HIDDEN NUMBER WAS '
                        f'{hidden_number}. AND YOU LOST : ${self.bid_amount}')
                    sleep(2)

                if self.player_balance < 10:
                    casino.clear()
                    print('_____________________________________________________')
                    print(f'YOUR FULL NAME : {self.player_name}\nYour CURRENT BALANCE : ${self.player_balance}')
                    print('-----------------------------------------------------')

                    print('\n')
                    print(f'SORRY {self.player_name} YOU DO NOT HAVE ENOUGH MONEY TO PLAY!!!')
                    exit(0)

            else:
                self.game_menu()
                print('____________________________________________')
                print('_______THANK YOU FOR PLAYING OUR GAME_______')
                print('--------------------------------------------')
                exit(0)


casino = Casino()
casino.clear()
casino.greeting()
casino.player_config()
casino.game_setup()
