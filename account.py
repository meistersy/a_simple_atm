class Account:
    __account_id = ''
    @property
    def account_id(self) -> str :
        return self.__account_id

    __Balance = 0
    @property
    def balance(self) -> int :
        return self.__Balance

    def __init__(self, account_id : str) -> None:
        self.__account_id = account_id
        self.__Balance = 0

    # return balance after deposit
    def deposit(self, cash : int) -> int :
        self.__Balance += cash
        return self.balance

    # return balance after withdraw
    def withdraw(self, cash : int) -> int : 
        if self.__Balance >= cash :
            self.__Balance -= cash
            return cash
        else :
            return None
    