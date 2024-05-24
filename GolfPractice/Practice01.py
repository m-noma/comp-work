import re

class Golf:
    def __init__(self, hole_score_array, player_array):
        self.hole_score_array = hole_score_array
        self.player_array = player_array

    # 最終ホール計算
    def total_hole_num(self):
        result = []
        for i in self.player_array:
            if(len(self.hole_score_array) < len(self.player_array[i][1])):
                result = len(self.hole_score_array)
            elif(len(self.player_array[i][1]) < len(self.hole_score_array)):
                result = len(self.player_array[i][1])
            elif(len(self.player_array[i][1]) == len(self.hole_score_array)):
                result = len(self.player_array[i][1])
        return result
    
    # スコアを計算し, ポイントの形に変換. (1: パーの値, 2: プレーヤーのスコア)
    def calc_score(self, total_hole_num):
        total_score = 0
        for i in range(total_hole_num):
            total_score += int(self.player_score_array[i]) - int(self.hole_score_array[i])
        return total_score

class GolfPlayer:
    def __init__(self, player_name, player_score_array):
        self.player_name = player_name
        self.player_score_array = player_score_array
    
    # スコアの表記方法を改良する 
    def score_conversion(self, calc_num):
        if(calc_num < 0):
            return "{}".format(calc_num)
        if(0 < calc_num):
            return "+{}".format(calc_num)
        elif(calc_num == 0):
            return "+-{}".format(calc_num)
        else:
            return "calculation errer."
        
    def play_result(self):
        return self.calc_score(self.total_hole_num())
        
    def show_play_result(self):
        total_hole_num = self.total_hole_num()
        print("{}選手: {}ホール終了して{}. \n".format(self.player_name, total_hole_num,
                                            self.score_conversion(self.calc_score(total_hole_num))))

# 人数の入力を受け付ける
def input_player_num():
    input_mun = input("人数を入力: ")

# ゴルフプレイの入力を受け付ける
def input_score():
    input_str = input("データの入力: ")
    return input_str

# 引数で与えられた文字列から数字を抜き出す
def re_base_score(input_str):
    if(input_str == "help"):
        print("""スコアに入力可能な文字は, 「数字(0-9)」, 「カンマ(,)」, 「半角スペース」のみ「カンマ(,)」は数値の区切り文字とする""")
        return re_base_score(input_score())
    # elif(input_str == r"[- ,]"):
    #     print("指定文字以外が含まれています.\n再度入力して下さい.\n")
    #     return re_base_score(input_score())
    else:
        # 空白をまず消し、その後数字を取得する(,区切りで数字を見るため "2 2"を2,2と取りたい場合は.replaceを削除)
        # "3 -5"がはじけない現状だと[3,-5]となってしまうため
        score_array = re.findall(r"-?\d+", input_str.replace(" ", ""))
        print("入力値: {}".format(score_array))
        # 指定文字以外の配列を作る
        str_array = re.findall(r"[^0-9^,^ ^-]", input_str)
        if(0 < len(re.findall(r"[^0-9^,^ ^-]", input_str))):
            print("指定文字以外が含まれています.\n再度入力して下さい.\n")
            return re_base_score(input_score())
        if(0 < len(re.findall(r'\b\d+\-\d+\b', input_str))):
            print("計算分を入れないでください.\n再度入力してください.\n")
            return re_base_score(input_score())
        if(len(score_array) <= 0):
            # ↓入力が"-"のみの場合「空白です」に入ってしまう...
            print("空白です.\n再度入力してください.\n")
            return re_base_score(input_score())
        else:
            for score in score_array:
                if(int(score) <= 0):
                    print("0以下の値が含まれます.\n再度入力してください.\n")
                    return re_base_score(input_score())
            return score_array
    
def main():
    hole_base_score = [4, 4, 3, 4, 5,
                        4, 5, 3, 4, 4,
                        3, 4, 5, 4, 3,
                        4, 5, 4]
    player_score = input_score()
    player_score = re_base_score(player_score)
    GolfPlayer(hole_base_score, "aaaa", player_score).show_play_result()

if __name__ == "__main__":
    main()