from random import randint
from account import Account
from bank_card import BankCard


class ATMDataProvider:
    __accounts = {}         # {"accountID":Account(), ...}
    @property
    def accounts(self) -> list :
        return list(self.__accounts.keys())
    __cards = {}            # {"cardnum":BankCard(), ...}
    @property
    def cards(self) -> list :
        return list(self.__cards.keys())
    __accountholders = {}   # {"cardnum":["accountID1", "accountID2", ...], ...}

    def addCard(self) -> str:
        while True :
            card_number = self.__generateCardNumber()
            if card_number not in self.__cards.keys() :
                break

        self.__cards[card_number] = BankCard(card_number)
        self.__accountholders[card_number] = []
        return card_number

    def addAccount(self, card : BankCard) -> str:
        while True :
            account_id = self.__generateAccountID()
            if account_id not in self.__accounts.keys() :
                break

        self.__accounts[account_id] = Account(account_id)

        self.__accountholders[card.card_number].append(account_id)
        return account_id

    def getCardInfo(self, card_number, PIN) -> BankCard:
        if card_number not in self.cards :
            return None
        card = self.__cards[card_number]
        if card.authenticate(PIN) :
            return card
        else : 
            return None
    
    def getAccounts(self, card : BankCard) -> list :
        accounts = []
        if card.card_number in self.__accountholders.keys() :
            accounts = list(self.__accountholders[card.card_number])
        return accounts

    def getAccount(self, account_id : str) -> Account :
        account = None
        if account_id in self.__accounts.keys() :
            account = self.__accounts[account_id]
        return account


    @staticmethod
    def __generateCardNumber() -> str:
        cn_tmp = ''
        for i in range(0, 4):
            cn_tmp += str(randint(1000, 9999)) + '-'
        cn_tmp = cn_tmp[0:-1]   # remove tail
        return cn_tmp

    @staticmethod
    def __generateAccountID() -> str:
        acc_id = ''
        for i in range(0, 3):
            acc_id += str(randint(10000, 99999)) + '-'
        acc_id = acc_id[0:-1]   # remove tail
        return acc_id