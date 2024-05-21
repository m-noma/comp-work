import re

# 入力を受け付ける
def input_score():
    input_str = input("スコア入力: ")
    return input_str

# 引数で与えられた文字列から数字を抜き出す
def re_base_score(input_str):
    if(input_str == "help"):
        print("""入力可能な文字は, 「数字(0-9)」, 「カンマ(,)」, 「半角スペース」のみ「カンマ(,)」は数値の区切り文字とする""")
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