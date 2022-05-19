class BankCard :
    __card_number = ''
    @property
    def card_number(self) -> str :
        return self.__card_number

    __PIN_number = '0000' # 4 digits

    def __init__(self, card_number : str) -> None:
        self.__card_number = card_number
        self.__PIN_number = '0000'
        pass

    def setPIN(self, oldPIN : str, PIN : str) -> bool:
        if oldPIN != self.__PIN_number or PIN == self.__PIN_number or PIN == '0000' or not self.validatePIN(PIN) :
            return False
        else :
            self.__PIN_number = PIN
            return True

    def authenticate(self, PIN : str) -> bool:
        return PIN == self.__PIN_number

    @staticmethod
    def validatePIN(PIN : str) -> bool :
        return bool(PIN.isdigit() and 4 == len(PIN))
