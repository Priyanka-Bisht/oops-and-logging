# Multiple inheritance
class bank:
    def transaction(self):
        print("total transaction value")
    def account_opening(self):
        print("this will show you your account open status")
    def deposite(self):
        print("this will show your deposited amount")
    def test(self):
        print("this is a test method from bank class")

class HDFC_bank():
    def hdfc_to_icici(self):
        print("this will show you all the trasaction happend to icici through hdfc")
    def test(self):
        print("this is a test method ")

class ineuron_bank:
    def account_status_icici(self):
        print("print a account status in icici")


class icici(HDFC_bank,bank,ineuron_bank):
    pass

i = icici()
i.transaction()
i.account_opening()
i.deposite()
i.hdfc_to_icici()
i.test()
i.account_status_icici()

