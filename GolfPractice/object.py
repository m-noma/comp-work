# 渡辺
import re
class score:
    def __init__(self,per):
        self.per = per

class keisan:
    def nyuuryoku():
        inputseiki = ""
        while(True):
            inpu=input("Input > ")
            # re.serach()は一致してる部分があるか調べる
            inputseiki = re.search(r"(\d+,(\s?)){0,17}\d+,?", inpu).group()
            print("ここ→: {}".format(inputseiki))
            suuzidake = inputseiki.replace(' ','').split(',')
            print(suuzidake)
            if(inputseiki):
                break
            else:
                print("文字やめろ")
        
        
        return suuzidake
    
    def hallsuu(suuzidake,golfhall):
        dasuu=len(suuzidake)
        scoresum = 0
        for i in range(dasuu):
            score = int(suuzidake[i]-golfhall[i].per)
            scoresum += score
            if(scoresum > 0):
                scorestr = '+'+str(scoresum)
            elif(scoresum == 0):
                scorestr = '+-'+str(scoresum)
            else:
                scorestr = str(scoresum)
                return dasuu,scorestr
            
class main:
    perarray=[4,4,3,4,5,4,5,3,4,4,3,4,5,4,3,4,5,4]
    golfhall = []
    for x in perarray:
        golfhall.append(score(x))
    scorearray = keisan.nyuuryoku()
    dasuu,scorestr=keisan.hallsuu(scorearray,golfhall)

    print("output > " + dasuu + "ホール終了して、"+ scorestr)