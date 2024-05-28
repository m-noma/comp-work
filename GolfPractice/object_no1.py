# 今井
import re

class GolfHall:
  def __init__(self,hallnum,per):
    self.hallnum=hallnum
    self.per=per

class ScoreCalculator:
  def scoreget():
    #数値を入力
    while(True):
      hitcolumn=input("Input > ")
    
      inputjudge=re.search('(\d+,(\s?)){0,17}\d+,?', hitcolumn)#数値、カンマ、スペースだけのパターン
      inputjudge2=re.search('-|(,?[^\d]0+,?)', hitcolumn)#0とマイナスを除外するパターン

      if(inputjudge and not inputjudge2):
        break
      elif(inputjudge2):
        print("不適切な入力です。数値は1以上にしてください")
      else:
        print("不適切な入力です。数字と,のみを入力してください")

    #入力部で入力した文字から打数を抽出、scorearrに代入
    scorearr=hitcolumn.replace(' ','').split(',')
    if '' in scorearr:
      scorearr.remove('')#入力時末尾にカンマをつけると空の要素が追加されてしまうのでここで消す
    return scorearr
  
  def scoresumget(scorearr,golfhall):
    hitnum=len(scorearr)
    scoresum=0

    #総合点scoresumを計算
    for j in range(hitnum):
      scoresum+=int(scorearr[j])-golfhall[j].per

    #scoresumの数値に合わせて、+-の有無を決定
    if(scoresum>0):
      scorestr='+'+str(scoresum)
    elif(scoresum==0):
      scorestr='+-'+str(scoresum)
    else:
      scorestr=str(scoresum)
    
    return hitnum,scorestr

class Main:

  perarr=[4,4,3,4,5,4,5,3,4,4,3,4,5,4,3,4,5,4]#パーの値(固定値)
  golfhall=[]#ゴルフホール
  i=1

  #パーの値を各ホールに代入
  for x in perarr:
    golfhall.append(GolfHall(i,x))
    i+=1

  #入力した値を格納
  scorearr=ScoreCalculator.scoreget()

  hitnum,scorestr=ScoreCalculator.scoresumget(scorearr,golfhall)

  print("Output > %dホール終了して、%s" % (hitnum,scorestr))
  