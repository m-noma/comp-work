from inspect import _void


class ATM:
    def __init__(self, processing_amount: int, identification_number:str, account_balance:int) -> None:
        self.processing_amount = processing_amount 
        self.identification_number = identification_number
        self.account_balance = account_balance

    def check_identification_number(self) -> bool:
        input_identification_num = input("暗証番号入力: ")
        return False 
    
    
    
class account:
    def __init__(self, bank_branch_name:str, account_number:str,
                 name:str, account_balance:int, identification_number:str) -> None:
        self.bank_branch_name = bank_branch_name
        self.account_number = account_number
        self.name = name
        self.account_balance = account_balance
        self.identification_number = identification_number

    def set_account(self) -> _void:
        