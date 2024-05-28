import re

par = [4,4,3,4,5,4,5,3,4,4,3,4,5,4,3,4,5,4]

def cancel_input(input):
    if input == '':
        print("入力がありません。")
        return 1
    if re.search('^.+,.+,.*[^\\d,-]',input):
        print("入力できない文字が含まれています。")
        return 1
    if re.search('^.+,.+,.*[^,]-\\d+',input):
        print("入力できない文字が含まれています。")
        return 1
    if re.search('^.+,.+,.*-\\d+',input):
        print("0以下の数値が入力されています。")
        return 1
    if re.search('^.+,.+,.*-',input):
        print("入力できない文字が含まれています。")
        return 1
    if re.search('^.+,.+,.*0+,',input):
        print("0以下の数値が入力されています。")
        return 1
    if re.search('^.+,.+,.*0+$',input):
        print("0以下の数値が入力されています。")
        return 1
    return 0

def input_string():
    flag = 1
    while flag:
        result = input("input   > ")
        result = result.replace(" ","")
        result = re.sub(",+",",",result)
        flag = cancel_input(result) 
    result = result.strip(",")
    result_list = result.split(',')
    del result_list[38:]
    result_list[2:] = [int(s) for s in result_list[2:]]
    
    return result_list

class Player:
    
    name = "golfer"
    result = [4,4,3,4,5,4,5,3,4,4,3,4,5,4,3,4,5,4]

    def set(self, a, b):
        self.name = a
        self.result = b

def calculate_score(result):
    score = 0
    for i in range(min(len(result),18)):
        score += result[i] - par[i]
    return score

def print_score(score):
    if score > 0:
        print("Output > 18ホール終了して、+",score)
    elif score == 0:
        print("Output > 18ホール終了して、+-0")
    else:
        print("Output > 18ホール終了して、",score)

def main():
    while(1):
        result_list = input_string()
        if(len(result_list) != 38):
            print("数字の数が足りません。")
        else:
            break
    player1 = Player()
    player2 = Player()
    player1.set(result_list[0],result_list[2:19])
    player2.set(result_list[1],result_list[20:37])
    print_score(calculate_score(player1.result))
    print_score(calculate_score(player2.result))

    if(calculate_score(player1.result)<calculate_score(player2.result)):
        print("勝者は",player1.name)
    elif(calculate_score(player1.result)==calculate_score(player2.result)):
        print("引き分け")
    else:
        print("勝者は",player2.name)

if __name__ == "__main__":
    main()