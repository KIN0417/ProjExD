import random
import datetime

n1=10 #対象文字数
n2=2 #欠損文字数
Max=5 #最大繰り返し数
def quiz():
    for xyz in range(Max):
        moji=list("ABCDEFGHIJKMNOPQRSTUVWXYZ")
        q=[] #対象文字のリスト
        k=[] #欠損文字のリスト
        for i in range(n1):
            a=random.randint(0,len(moji)-1)
            q.append(moji.pop(a))
        print("対象文字：")
        print(" ".join(q)) #対象文字表示
        for i in range(n2):
            b=random.randint(0,len(q)-1)
            k.append(q.pop(b))
        print("表示文字：") #表示文字表示
        print(" ".join(q))
        #print(k) #答え確認用
        x=1
        for i in range(n2):
            kotae=input(f"{x}文字目の欠損文字を入れてください")
            if kotae in k:
                print("正解")
                x+=1
                k.remove(str(kotae))
            else:
                print("不正解")
                print("------------------------")
                if xyz==4 and len(k)!=0:
                    print("GAME OVER")
                break
        if len(k)==0:
            print("終了")
            break

start = datetime.datetime.now() # 始まる時間を記録
quiz()
end = datetime.datetime.now()   # 終わる時間を記録
print(end - start)