#-*-:encoding = UTF-8 -*-
"""
import requests
from bs4 import BeautifulSoup

content = requests.get('https://qiushibaike.com/').content
soup = BeautifulSoup(content,'html.parser')

for div in soup.find_all('div',{'class':'content'}):
    print(div.text.strip())
"""

def demo_string():
    stra = " \n\txys \t\n"
    strb = "lalala"
    strc = "hi arashi"
    print(1, stra)
    print(2, strb.strip())
    print(3, stra.strip()+strb.strip())
    print(4, stra.strip() , strb.strip())
    print(5, strc.split('r'))

def demo_buildinfunction():
    x = 1
    y = 2.2
    print(type(x),type(y))

def demo_controlflow():
    score = 65
    if score > 90:
        print("A")
    elif score > 60:
        print("B")
    else:
        print("C")

def demo_list():
    lista = [1,2,3]
    print(1,lista)
    lista[1] = 'a'
    print(2,lista) #liat可变，对list所做的修改会保存
    lista.insert(3,'b')
    print(3,lista)
    lista.pop(2)
    print(4,lista)
    print(5,lista*2)
    lista.reverse()
    print(6,lista)
   # lista.sort()
    #print(7, lista)  #sort好像不能用
    print(8,[0]*14)

    tuplea = (1,2,3)
    lista.append("ww")
    print(9,lista)

def demo_dict():
    dicta = {1:1,2:4,3:9}
    print(1,dicta)
    print(2,dicta.keys(),dicta.values())
    print(3, 1 in dicta, '1' in dicta)
    for key,value in dicta.items():
        print(key,value)

def demo_set():
    seta = set((1,2,3))
    setb = set((4,5,6))
    print(1,seta)
    print(2,seta.intersection(setb),seta&setb) #好像没有起作用
    print(3,seta.union(setb))
    seta.add('x')
    print(4,seta)

if __name__ == '__main__':
    print("Hello World！")
    demo_string()
    #print('\n')
    demo_buildinfunction()
    demo_controlflow()
    demo_list()
    demo_dict()
    demo_set()
