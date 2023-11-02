class AccountDB:
    '''
    Set database for banking system to insert , search , delete and return str in self.account_database
    '''

    def __init__(self):
        '''
        Set self.account_database name
        '''
        self.account_database = []

    def insert(self, account):
        '''
        Used __search_private to search that if account is none exist will return -1 and will enter if statement
        then it will append to self.account_database else will print Duplicate account to alert user

        '''
        index = self.__search_private(account.account_number)
        if index == -1:
            self.account_database.append(account)
        else:
            print(account, "Duplicated account; nothing to be insert")

    def __search_private(self, account_num):
        '''
        Using private to search in self.account_database then if it matching, it will return i but if none exist it will 
        return -1 to used in other functions
        '''
        for i in range(len(self.account_database)):
            if self.account_database[i].account_number == account_num:
                return i
        return -1

    def search_public(self, account_num):
        '''
        This will allowed user to see their account by for loop in self.account_database to find account then if it match it will
        return account 
        '''
        for account in self.account_database:
            if account.account_number == account_num:
                return account
        return None

    def delete(self, account_num):
        '''
        Search in __search_private if it index != -1 it will delete account in self.account_database else will return invalid 
        with nothing change       
        '''
        index = self.__search_private(account_num)
        if index != -1:
            del self.account_database[index]
        else:
            print(account_num, "invalid account number; nothing to be deleted.")

    def __str__(self):
        '''
        return account with for loop
        '''
        s = ''
        for account in self.account_database:
            s += str(account) + ", "
        return s


class Account:

    def __init__(self, num, type, account_name, balance):
        '''
        Set statement for 1 account number
        '''
        self.account_number = num
        self.type = type
        self.account_name = account_name
        self.balance = balance

    def deposit(self, amount):
        '''
        deposit money to bank account
        '''
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount

    def __str__(self):
        return '{' + str(self.account_number) + ',' + str(self.type) + ',' + str(self.account_name) + ',' + str(self.balance) + '}'


account1 = Account("0000", "saving", "David Patterson", 1000)
account2 = Account("0001", "checking", "John Hennessy", 2000)
account3 = Account("0003", "saving", "Mark Hill", 3000)

my_account_DB = AccountDB()
my_account_DB.insert(account1)
my_account_DB.insert(account2)
my_account_DB.insert(account3)
print(my_account_DB)
my_account_DB.search_public("0003").deposit(50)
print(my_account_DB)
my_account_DB.search_public("0003").withdraw(100)
print(my_account_DB)
my_account_DB.search_public("0010").deposit(50)
print(my_account_DB)
