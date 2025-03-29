from typing import Tuple

from TerminalApp_Base import ConsoleApplication


class BankAccount:
    def __init__(self, user_id: str, user_name: str, balance: float, credit_limit: float):
        self.user_id = user_id
        self.user_name = user_name
        self.balance = balance
        self.credit_limit = credit_limit

    @staticmethod
    def get_initials(value: str) -> str:

        return "".join([c for c in value if c.isupper()])

    def get_tag(self) -> str:
        return f'[{BankAccount.get_initials(self.user_name)}:{self.user_id}]'

    def add_funds(self, amount: float) -> None:
        print(f'{self.get_tag()} Adding {amount} in funds: '
              f'{self.balance} -> {self.balance + amount}')
        self.balance += amount

    def remove_funds(self, amount: float) -> bool:
        print(f'{self.get_tag()} Removing {amount} in funds: '
              f'{self.balance} -> {self.balance - amount}')
        if self.balance + self.credit_limit < amount:
            return False
        self.balance -= amount
        return True

    def deposit(self, amount: float) -> None:
        self.add_funds(amount)

    def withdraw(self, amount: float) -> None:

        if self.remove_funds(amount):
            print(f'Withdrew {amount} from account. Current {self.balance}')
        else:
            print(f'Denied due to insufficient balance')

    def display(self, use_header: bool = True, use_footer: bool = True) -> str:
        credit: float = BankAccount.clamp(
            0,
            self.credit_limit,
            self.credit_limit + self.balance)

        padding: str = '-' * 5
        header: str = f'{padding}Account details{padding}'
        return (
            (f'{header}\n' if use_header else '') +
            f'ID: {self.user_id}\n'
            f'Name: {self.user_name}\n'
            f'Balance: {self.balance}\n'
            f'Credit: {credit}' +
            (f"\n{'-'*len(header)}" if use_footer else '')
            )

    @staticmethod
    def clamp(min_value: float, max_value: float, value: float):
        if value < min_value:
            return min_value
        elif value > max_value:
            return max_value
        else:
            return value

def transfer_funds(
        from_acc: BankAccount,
        to_acc: BankAccount,
        amount: float,
        debug: bool = False):

    if debug:
        print(
            f'Transferring {amount} from\n'
            f'{from_acc.display()}\n'
            f'to\n'
            f'{to_acc.display()}')

    if from_acc.remove_funds(amount):
        to_acc.add_funds(amount)

    if debug:
        print('Transfer complete')
        print(from_acc.display())
        print(to_acc.display(use_header=False))

def run_test_cases():
    padding = '=' * 30
    print(padding)
    print('Running test cases')
    print(padding)

    account_1, accounts = generate_accounts()
    account_2 = accounts[0]

    print('Listing acc. 1')
    print(account_1.display())
    print('Listing acc. 2')
    print(account_2.display())

    account_1.withdraw(50)
    account_1.withdraw(100)
    account_1.withdraw(100)
    account_1.deposit(50)
    transfer_funds(account_2, account_1, 200)

    print(padding)
    print('Simulation over')
    print(padding)

def setup_app(
        account: BankAccount,
        other_accounts: Tuple[BankAccount]) -> ConsoleApplication:
    return ConsoleApplication(
        'Welcome to Py Bank',
        {
            'Main': [
                ('V', 'View acc. data', lambda: print(account.display())),
                ('D', 'Deposit', lambda: account.deposit(get_amount_input())),
                ('W', 'Withdraw', lambda: account.withdraw(get_amount_input())),
                ('T', 'Transfer', lambda: transfer(account, other_accounts)),
                ('R', 'Request transfer', lambda: request_transfer(account, other_accounts)),
            ]})

def transfer (acc: BankAccount, accounts: Tuple[BankAccount]) -> None:
    transfer_funds(acc, get_target_account(accounts), get_amount_input())

def request_transfer (acc: BankAccount, accounts: Tuple[BankAccount]) -> None:
    transfer_funds(get_target_account(accounts), acc, get_amount_input())

def get_amount_input() -> float:
    return float(input('Please input the desired amount: '))

def get_target_account(accounts: Tuple[BankAccount]) -> BankAccount:
    print('Please input ID of desired account from the options below')
    for acc in accounts:
        print(f'[ID:{acc.user_id}] {acc.user_name}')
    target_id: str = input()
    return {acc.user_id: acc for acc in accounts}[target_id]

def generate_accounts() -> (BankAccount, Tuple[BankAccount]):
    acc_1: BankAccount = BankAccount(
        '0001',
        'Dan Domingues',
        100,
        100)
    acc_2: BankAccount = BankAccount(
        '0002',
        'Danilo Coelho',
        500,
        0)

    return acc_1, (acc_2,)

def start_system():
    account, accounts = generate_accounts()
    app: ConsoleApplication = setup_app(account, accounts)

    app.show_intro()
    while True:
        app.show_inputs('Main')
        app.read_input_for('Main', run_associated_callback=True)

#Runtime
run_test_cases()
start_system()

#Improvements
#Add ID be automatic (static id)
#Use decorators to put balance info before and after all transfers
#Add more accounts
#Review multi-thread and multi-process lecture