from tkinter.messagebox import NO
from typing import final
from atm_service_provider import ATMServiceProvider
from bank_card import BankCard

class TellerMachine:
    __atm_service = ATMServiceProvider()

    __state_start : final = 0
    __state_insertcard : final = 10
    __state_inputpin : final = 20
    __state_selectoperation : final = 30
    __state_seebalance : final = 40
    __state_deposit : final = 50
    __state_withdraw : final = 60
    __state_endoperation : final = 70
    __state_selectaccount : final = 80

    def main(self) :
        card_number = ''
        pin_retry = 0
        state = 0
        while True :
            if self.__state_start == state :
                state = self.__state_insertcard
                continue
            elif self.__state_insertcard == state :
                card_number = input("INSERT CARD('xxxx-xxxx-xxxx-xxxx') >> ")
                state = self.__state_inputpin
                pin_retry = 3
                continue
            elif self.__state_inputpin == state :
                pin_number = input("INPUT PIN Number('xxxx') >> ")
                if True == self.__atm_service.insertCard(card_number=card_number, PIN=pin_number) :
                    state = self.__state_selectaccount
                elif 0 >= pin_retry:
                    pin_retry -= 1
                    print("PIN mismatch, try again.")
                    continue
                else :
                    print("PIN mismatch overcount, remove card.")
                    state = self.__state_insertcard
                continue
            elif self.__state_selectaccount == state :
                accounts = self.__atm_service.getAccountList()
                print("Account List >>")
                for i in accounts :
                    print(i)
                input_id = input("SELECT Account ID >> ")
                if input_id in accounts :
                    self.__atm_service.selectAccount(account_id=input_id)
                    state = self.__state_selectoperation
                continue
            elif self.__state_selectoperation == state :
                print("1) see Balance")
                print("2) Deposit")
                print("3) withdraw")
                operation = input("select Operation (1-3) >> ")
                
                if not operation.isdigit() :
                    continue
                elif  not int(operation) in range(1, 4) :
                    continue
                
                state = (int(operation) * 10 + self.__state_seebalance - 10)
                continue
            elif self.__state_seebalance == state :
                print("Balance : ", self.__atm_service.balance())
                state = self.__state_endoperation
            elif self.__state_deposit == state :
                cash = input("INSERT Cash to deposit >> ")
                if cash.isnumeric() :
                    self.__atm_service.deposit(int(cash))
                state = self.__state_seebalance
            elif self.__state_withdraw == state :
                cash = input("INPUT Cash to withdraw >> ")
                if cash.isnumeric() :
                    withdraw = self.__atm_service.withdraw(int(cash))
                if withdraw == None :
                    print("!!! too much cashes to withdraw !!!")
                state = self.__state_seebalance
            elif self.__state_endoperation == state :
                select = input("Remove Card? (y/n) >>")
                if select == 'y' :
                    state = self.__state_insertcard
                elif select == 'n' : 
                    state = self.__state_selectoperation
                continue
    
    def makeTestSet(self) :
        cards = []
        for i in range(0, 3) :
            cards.append(self.__atm_service.issueCard())
            print(cards[i])
            self.__atm_service.insertCard(cards[i], '0000')
            self.__atm_service.issueAccount()
        
tm = TellerMachine()
tm.makeTestSet()
tm.main()
