import random

from sympy import Q 
def shutudai():
    sazae=["サザエの旦那の名前は？","マスオ","ますお"]
    katuo=["カツオの妹の名前は？","ワカメ","わかめ"]
    tarao=["タラオはカツオからみてどんな関係？","甥","おい","甥っ子","おいっこ"]
    num=random.randint(0,2)
    if num==0:
        q=num
        print(sazae[0])
    if num==1:
        q=num
        print(katuo[0])
    if num==2:
        q=num
        print(tarao[0])
    return q

def kaitou(q):
    sazae=["サザエの旦那の名前は？","マスオ","ますお"]
    katuo=["カツオの妹の名前は？","ワカメ","わかめ"]
    tarao=["タラオはカツオからみてどんな関係？","甥","おい","甥っ子","おいっこ"]
    a=input("答え")
    if q==0:
        if a==sazae[1] or sazae[2]:
            print("正解")
        else:
            print("不正解")
    if q==1:
        if a==katuo[1] or katuo[2]:
            print("正解")
        else:
            print("不正解")
    if q==2:
        if a==tarao[1] or tarao[2] or tarao[3] or tarao[4]:
            print("正解")
        else:
            print("不正解")
        
q=shutudai()
kaitou(q)
