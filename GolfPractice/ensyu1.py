def kara(x):
    print("oooo")
    print(len(x))
    if len(x) <= 0:
        for n in range(1):
            print("もう一度入力しなおしてください")
            sx =[x for x in input().split(",")]
            if len(x) == 0:
                print("oooo")
                continue
        

list=[4,4,3,4,5,4,5,3,4,4,3,4,5,4,3,4,5,4]
leco = 0
print("数値を複数入力")

# print("x: {}\n".format(input()))
sx =[x for x in input().split(",") if x.strip()]
kara(sx)

print("------------------------")
for n in sx:
    print(sx)

print(sx)
for i in range(len(sx)):
    leco += (sx[i] - list[i])
    hole = i
    #print(i)
    
print("%dホール終了して、%d " %(hole+1,leco))



