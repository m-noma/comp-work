import re

def cancel_input(input):
    if re.search('[^\\d,-]',input):
        print("入力できない文字が含まれています。")
        return 1
    if input == '':
        print("入力がありません。")
        return 1
    if re.search('[^,]-\\d+',input):
        print("入力できない文字が含まれています。")
        return 1
    if re.search('-\\d+',input):
        print("0以下の数値が入力されています。")
        return 1
    if re.search('-',input):
        print("入力できない文字が含まれています。")
        return 1
    if re.search('^0+,',input):
        print("0以下の数値が入力されています。")
        return 1
    if re.search(',0+,',input):
        print("0以下の数値が入力されています。")
        return 1
    if re.search(',0+$',input):
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
    result_list = [int(s) for s in result.split(',')]
    
    return result_list

def calculate_score(result):
    par = [4,4,3,4,5,4,5,3,4,4,3,4,5,4,3,4,5,4]
    score = 0
    for i in range(min(len(result),18)):
        score += result[i] - par[i]
    return score

def main():
    result = input_string()
    score = calculate_score(result)
    if score > 0:
        print("Output > ",min(len(result),18),"ホール終了して、+",score)
    elif score == 0:
        print("Output > ",min(len(result),18),"ホール終了して、+-0")
    else:
        print("Output > ",min(len(result),18),"ホール終了して、",score)


if __name__ == "__main__":
    main()