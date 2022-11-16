from account import *

class Test:
    def setup_method(self):
        self.p1 = Account('Jane')
        self.p2 = Account('Camden')
        self.p3 = Account('Bobby')
        self.p4 = Account('Danny')

    def test_init(self):
        assert self.p1.get_name() == 'Jane'
        assert self.p1.get_balance() == 0

        assert self.p2.get_name() == 'Camden'
        assert self.p2.get_balance() == 0

        assert self.p3.get_name() == 'Bobby'
        assert self.p3.get_balance() == 0

        assert self.p4.get_name() == 'Danny'
        assert self.p4.get_balance() == 0

    def test_deposit(self):
        assert self.p1.deposit(5000) == True
        assert self.p1.get_balance() == 5000

        assert self.p2.deposit(-5000) == False
        assert self.p2.get_balance() == 0

        assert self.p3.deposit(0) == False
        assert self.p3.get_balance() == 0

    def test_withdraw(self):
        assert self.p1.deposit(5000) == True
        assert self.p1.withdraw(3000) == True
        assert self.p1.get_balance() == 2000

        assert self.p2.deposit(5000) == True
        assert self.p2.withdraw(-1000) == False
        assert self.p2.get_balance() == 5000

        assert self.p3.deposit(5000) == True
        assert self.p3.withdraw(0) == False
        assert self.p3.get_balance() == 5000

        assert self.p4.deposit(5000) == True
        assert self.p4.withdraw(6000) == False
        assert self.p4.get_balance() == 5000
