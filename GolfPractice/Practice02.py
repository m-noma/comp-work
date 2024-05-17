import re

# class Golf:
#     def __init__(self, hole_data):
#         print("golefクラス作成")
#         self.hole_data = hole_data

    
class GolfGame:
    def __init__(self, player_name, hole_data_array, input_score_array):
        self.player_name = player_name
        self.hole_data_array = hole_data_array
        self.input_score_array = input_score_array


class Hole:
    def __init__(self, par_num_array):
        self.par_num_array = par_num_array


class Player:
    def __init__(self, player_name, input_score_array):
        self.player_name = player_name
        self.input_score_array = input_score_array


# 入力を受け付ける
def input_score():
    input_str = input()
    return input_str

# 引数で与えられた文字列から数字を抜き出す
def re_base_score(input_str):
    score_array = re.findall(r"\d+", input_str)
    if(len(score_array) <= 0):
        print("再度入力してください\n")
        return re_base_score(input_score())
    else:
        return score_array
    

# スコアを計算し, ポイントの形に変換. (1: パーの値, 2: プレーヤーのスコア)
def calc_score(par_num, input_score):
    return int(input_score) - int(par_num)

def hole_count_conversion(hole_par_array, player_score_array):
    if(len(hole_par_array) < len(player_score_array)):
        result = len(hole_par_array)
    elif(len(player_score_array) < len(hole_par_array)):
        result = len(player_score_array)
    elif(len(player_score_array) == len(hole_par_array)):
        result = len(hole_par_array)
    return result

def score_conversion(calc):
    if(calc < 0):
        return "{}".format(calc)
    if(0 < calc):
        return "+{}".format(calc)
    elif(calc == 0):
        return "+-{}".format(calc)
    else:
        return "calculation errer."
    

def main():
    hole_base_score = [4, 4, 3, 4, 5,
                        4, 5, 3, 4, 4,
                        3, 4, 5, 4, 3,
                        4, 5, 4]
    player_score = input_score()
    player_score = re_base_score(player_score)
    player_total_score = 0
    for i in range(len(player_score)):
        if(18 <= i):
            break
        hole_data = Hole(hole_base_score[i])
        player_total_score += calc_score(hole_data.par_num, player_score[i])
    print("{}ホール終了して, {}.".format(hole_count_conversion(player_score, hole_base_score),
                                        score_conversion(player_total_score)))


if __name__ == "__main__":
    main()