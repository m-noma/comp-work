from inspect import _void

# 複数のボタン、アカウントが集約している
# processing_amount = 処理金額, account_balance = 残高
class ATM:
    def __init__(self, pin_str: str, account_balance: int) -> None:
        self.__processing_amount = 0 
        self.__pin_str = pin_str
        self.__account_balance = account_balance
        # print("pin: {}, [type: {}]\n".format(self._pin_str, type(self._pin_str)))

    # 暗証番号を認証
    def __authenticate_pin(self, input_pin_str: str) -> bool:
        pin_flag = False
        if(self.__pin_str == input_pin_str):
            pin_flag = True
            print("認証成功. \n")
        else:
            print("認証失敗. \n再度入力してください. \n")
        return pin_flag

    # 預金残高を確認
    def __check_deposit_balances(self, amount_transacted: int) -> bool:
        balance_flag = False
        balance_calculation = self.__account_balance - amount_transacted
        if(0 <= balance_calculation):
            balance_flag = True
            print("取引後の金額は{}です. \n".format(balance_calculation))
            self.__process_deposit_balances(-amount_transacted)
            print("{}円の引き落としです. \n".format(self.__processing_amount))
        else:
            print("{}円の残高不足です.\n再度入力してください. \n".format(balance_calculation))
        return balance_flag
    
    # 預金残高の処理
    def __process_deposit_balances(self, amount_transacted: int) -> _void:
        self.__processing_amount = amount_transacted

    # 暗証番号を入力
    def input_pin(self) -> _void:
        while(True):
            input_pin_str = input("暗証番号入力: ")
            if(self.__authenticate_pin(input_pin_str)):
                break

    # 出金額を入力
    def input_amount_of_withdrawal(self) -> _void:
        while(True):
            input_withdrawal = input("出金額入力: ")
            if(self.__check_deposit_balances(int(input_withdrawal))):
                break
    
    # 入金額を入力
    def input_amount_of_deposit(self) -> _void:
        self.__processing_amount = input("入金額入力: ")
    
    # 現金を用意
    def provide_cash(self) -> _void:
        print("現金")   

    # キャッシュカードを返却
    def  return_cash_card() -> _void:
        print("キャッシュカード返却")

    @property
    def processing_amount(self) -> int:
        return self.__processing_amount
    
    @processing_amount.setter
    def processing_amount(self, processing_amount: int) -> _void:
        self.__processing_amount = self.__processing_amount + processing_amount

# ATMに複数のアカウントが存在する
class Account:
    def __init__(self, bank_branch_name: str, account_number: str,
                 name: str, account_balance: int, pin_str: str) -> None:
        self.__bank_branch_name = bank_branch_name
        self.__account_number = account_number
        self.__name = name
        self.__account_balance = account_balance
        self.__pin_str = pin_str

    # 口座情報を設定
    # def __set_account(self, amount_transacted: int) -> _void:
    #     self.__account_balance = amount_transacted
        
    # 暗証番号ゲッター
    @property
    def pin_str(self) -> str:
        return self.__pin_str

    # 口座残高ゲッター
    @property
    def accaunt_balance(self) -> int:
        return self.__account_balance
    
    # 口座残高セッター
    @accaunt_balance.setter
    def account_balance(self, account_balance: int) -> _void:
        self.__account_balance = self.__account_balance + int(account_balance)
    
    # 全データ表示
    def show_data(self) -> _void:
        print("支店名: {},\n口座番号: {},\n氏名: {},\n口座残高: {},\n暗証番号: {}.\n".format(self.__bank_branch_name, self.__account_number, self.__name, self.__account_balance, self.__pin_str))


# アカウントのサブクラス
class UserAccount(Account):
    def __init__(self, bank_branch_name: str, account_number: str,
                 name: str, account_balance: int, pin_str: str) -> None:
        super().__init__(bank_branch_name, account_number, name, account_balance, pin_str)


# ボタンはATMに複数配置される
class Button:
    def __init__(self, button_name: str) -> None:
        self.__button_name = button_name

    def push_button(self) -> _void:
        print("{}を選択".format(self.__button_name))


# 処理を選択 / キャッシュカードを挿入 / 暗証番号を入力 / 引き出しor預入　/ カード返却
def main() -> _void:
    # ---------------------------------預金フェーズ--------------------------------------------------
    # 処理操作: 出金
    deposit_btn = Button("引き出し").push_button()

    # キャッシュカードを挿入
    my_account = UserAccount("福山", "32240267", "野間 瑞生", 16000, "2318")
    atm = ATM(my_account.pin_str, my_account.accaunt_balance)

    # 暗証番号を入力
    atm.input_pin()

    # 出金額入力
    atm.input_amount_of_withdrawal()

    # 口座情報更新
    my_account.account_balance = atm.processing_amount

    # 口座情報確認
    my_account.show_data()

    # del my_account
# ------------------------------------預金フェーズ----------------------------------------------------


# ---------------------------------引き出しフェーズ--------------------------------------------------
    # 処理を選択: 入金
    withdrawal_btn = Button("預入").push_button()
        
    # 暗証番号を入力
    atm.input_pin()

    # 入金額を入力
    atm.input_amount_of_deposit()

    # 口座情報更新
    my_account.account_balance = atm.processing_amount

    # 口座情報確認
    my_account.show_data()



# ---------------------------------引き出しフェーズ--------------------------------------------------

if __name__ == "__main__":
    main()