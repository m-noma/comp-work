import re


class GolfGame:
    def __init__(self, hole_score_array, player_array):
        self.hole_score_array = hole_score_array
        self.player_array = player_array

    # 最終ホール計算
    def total_hole_num(self, player_score_array):
        if(len(self.hole_score_array) < len(player_score_array)):
            result = len(self.hole_score_array)
        elif(len(player_score_array) < len(self.hole_score_array)):
            result = len(player_score_array)
        elif(len(player_score_array) == len(self.hole_score_array)):
            result = len(player_score_array)
        return result
    
    # スコアを計算し, ポイントの形に変換. (1: パーの値, 2: プレーヤーのスコア)
    def calc_score(self, total_hole_num, player_score_array):
        total_score = 0
        for i in range(total_hole_num):
            total_score += int(player_score_array[i]) - int(self.hole_score_array[i])
        return total_score
    
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
        
    def show_player_result_unit(self, player_num):
        total_hole_num = self.total_hole_num(self.player_array[player_num].player_score_array)
        print("{}選手: {}ホール終了して{}.\n".format(self.player_array[player_num].player_name, total_hole_num,
                                                        self.score_conversion(self.calc_score(total_hole_num, self.player_array[player_num].player_score_array))))
    
    def show_play_result_all(self):
        for i, player in enumerate(self.player_array):
            total_hole_num = self.total_hole_num(player.player_score_array)
            print("{}: \n{}選手: {}ホール終了して{}.\n".format(i, player.player_name, total_hole_num,
                                                        self.score_conversion(self.calc_score(total_hole_num, player.player_score_array))))
    def show_play_data_unit(self):
        for i, player in enumerate(self.player_array):
            print("player{}: {}".format(i, player))
    
    def show_result_1vs1(self, player1_num, player2_num):
        player1 = self.player_array[player1_num]
        player2 = self.player_array[player2_num]
        player1_score = self.calc_score(len(self.hole_score_array), player1.player_score_array)
        player2_score = self.calc_score(len(self.hole_score_array), player2.player_score_array)
        if(player1_score < player2_score):
            print("{}の勝利!!\n".format(player1.player_name))
        elif(player2_score < player1_score):
            print("{}の勝利!!\n".format(player2.player_name))
        else:
            print("引き分け!!")

    
class GolfPlayer:
    def __init__(self, player_name, player_score_array):
        self.player_name = player_name
        self.player_score_array = player_score_array

    def show_player_data(self):
        print("名前: {},\nスコア: {}\n".format(self.player_name, self.player_score_array))

def divide_name_and_score(input_str, player_num):
    str_array = input_str.split(",", player_num)
    return str_array[:player_num], str_array[player_num]

# 引数で与えられた文字列から数字を抜き出す
def re_base_score(input_str):
    if(input_str == "help"):
        print("""スコアに入力可能な文字は, 「数字(0-9)」, 「カンマ(,)」, 「半角スペース」のみ「カンマ(,)」は数値の区切り文字とする""")
        return re_base_score(input("スコア入力: "))
    else:
        # 空白をまず消し、その後数字を取得する(,区切りで数字を見るため "2 2"を2,2と取りたい場合は.replaceを削除)
        # "3 -5"がはじけない現状だと[3,-5]となってしまうため
        score_array = re.findall(r"-?\d+", input_str.replace(" ", ""))
        # 指定文字以外の配列を作る
        str_array = re.findall(r"[^0-9^,^ ^-]", input_str)
        if(0 < len(re.findall(r"[^0-9^,^ ^-]", input_str))):
            print("スコアに指定文字以外が含まれています.\n再度入力して下さい.\n")
            return re_base_score(input("スコア入力: "))
        elif(0 < len(re.findall(r'\b\d+\-\d+\b', input_str))):
            print("スコアに計算分を入れないでください.\n再度入力してください.\n")
            return re_base_score(input("スコア入力: "))
        elif(len(score_array) <= 0):
            # ↓入力が"-"のみの場合「空白です」に入ってしまう...
            print("スコアが空白です.\n再度入力してください.\n")
            return re_base_score(input("スコア入力: "))
        else:
            for score in score_array:
                if(int(score) <= 0):
                    print("0以下の値が含まれます.\n再度入力してください.\n")
                    return re_base_score(input("スコア入力: "))
        return score_array

def re_base_array(player_num, constant_array, input_array):
    score_array = []
    for i in range(player_num):
        score = []
        for j in range(len(constant_array)):
            # ここにOutOfIndexエラーの際の処理を記述しないとダメ
            score.append(input_array[i * len(constant_array) + j])
        score_array.append(score)
    print("score: {}".format(score_array))
    return score_array

def main():
    constant_array = [4, 4, 3, 4, 5, 4, 5, 3, 4, 4, 3, 4, 5, 4, 3, 4, 5, 4]
    player_list = []
    input_player_num = int(input("人数を入力: "))
    input_player_data = input("データ入力: ")
    player_name_list, input_score = divide_name_and_score(input_player_data, input_player_num)
    player_score_list = re_base_score(input_score)
    player_score_list = re_base_array(2, constant_array, player_score_list)
    for i in range(input_player_num):
            player_list.append(GolfPlayer(player_name_list[i], player_score_list[i]))
    # for i, player in enumerate(player_list):
    #     print("{}: ".format(i+1))
    #     player.show_player_data()
    g = GolfGame(constant_array, player_list)
    g.show_play_result_all()
    g.show_result_1vs1(0,1)
    



    # for i in range():


if __name__ == "__main__":
    main()