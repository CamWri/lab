class Account:
    def __init__(self, name: str):
        '''
        Establishes a bank account with a name and a balance of 0
        :param name: The name of the newly created bank account
        '''
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        '''
        Takes your current total value of your account and adds the inputed amount
        :param amount: The value that you are adding to your current account
        :return: Returns your new account balance after adding in the new amonut
        '''
        if amount <= 0:
            return False
        else:
            self.__account_balance = self.__account_balance + amount
            return True

    def withdraw(self, amount: float) -> bool:
        '''
        Takes your current total value of your account and subtracts the inputed amount
        :param amount: The value that you are subtracting to your current account
        :return: Returns your new account balance after subtracting the new amonut
        '''
        if amount <= 0 or amount > self.__account_balance:
            return False
        else:
            self.__account_balance = self.__account_balance - amount
            return True

    def get_balance(self) -> float:
        '''
        Retrieves the balance of your account
        :return: Returns your current account balance
        '''
        return self.__account_balance

    def get_name(self) -> str:
        '''
        Retrieves the name of your account
        :return: Returns the name of the created said account
        '''
        return self.get_name 