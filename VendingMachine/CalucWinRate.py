import random

class Rolette:
    # 0~引数を含む値のランダム値をwinning_rateとして保持する
    def __init__(self, winning_rate_num):
        # calcilation random number
        self.winning_rate = random.randint(0, winning_rate_num)
        if(self.winning_rate == winning_rate_num):
            print("atari")

    def hit_or_outskirts(self):
        print("a")
    

class Rolette1:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print("{}, {}".format(self.a, self.b))

