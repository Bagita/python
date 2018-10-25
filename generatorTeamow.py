import random

gracze = ['gracz1','gracz2','gracz3','gracz4','gracz5','gracz6','gracz7','gracz8','gracz9','gracz10']

def genTeam(lista):
    random.shuffle(lista)
    polowaListy = len(lista) // 2
    team1 = lista [ 0 : polowaListy ]
    team2 = lista [ polowaListy : ]
    return team1,team2

a = genTeam( [1,2,3,4,5,6,7,8,9] )
print(a [0])
print(a [1])

