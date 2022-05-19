from xml.etree.ElementTree import PI
from account import Account
from atm_data_provider import ATMDataProvider
from bank_card import BankCard

class ATMServiceProvider:
    __atm_data = ATMDataProvider()

    __tmp_card : BankCard = None
    __tmp_account : Account = None

    def issueCard(self) -> str :
        return self.__atm_data.addCard()

    def issueAccount(self) -> str :
        if self.__tmp_card == None :
            return None
        return self.__atm_data.addAccount(self.__tmp_card)

    def insertCard(self, card_number : str, PIN : str) -> bool:
        card = self.__atm_data.getCardInfo(card_number=card_number, PIN=PIN)
        if card == None :
            return False
        else :
            self.__tmp_card = card
            return True

    def getAccountList(self) -> list :
        if self.__tmp_card == None :
            return []
        return self.__atm_data.getAccounts(card=self.__tmp_card)

    def selectAccount(self, account_id : str) -> bool :
        account = self.__atm_data.getAccount(account_id=account_id)
        if account != None :
            self.__tmp_account = account
            return True
        else :
            return False
    
    def deposit(self, cash : int) -> int :
        if self.__tmp_account == None :
            return None
        return self.__tmp_account.deposit(cash=cash)
        
    def withdraw(self, cash : int) -> int :
        if self.__tmp_account == None :
            return None
        return self.__tmp_account.withdraw(cash=cash)
        
    def balance(self) -> int :
        if self.__tmp_account == None :
            return None
        return self.__tmp_account.balance
        
    def removeCard(self) -> None :
        self.__tmp_card = None
        self.__tmp_account = None