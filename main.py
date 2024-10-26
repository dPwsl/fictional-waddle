from ursina import *
from ursina.prefabs.first_person_controller import *

app=Ursina()

def  makemap(St,Map,A):
    for i in range(len(St)):
        for j in range(len(St[i])):
            for k in range(len(St[i][j])):
                if St[i][j][k]==3:
                    win=Entity(
                    model='cube',
                    position=(j+A,i,k),
                    scale=(1,1,1),
                    collider='box',
                    color=color.lime
                        )
                elif St[i][j][k]:
                    a=Entity(
                        model='cube',
                        position=(j+A,i,k),
                        scale=(1,1,1),
                        collider='box'
                    )
    wall=Entity(
        position=(0,50,Map+100),
        scale=(500,500,1),
        color=color.dark_gray,
        model='cube'   
    )
    return win

player=FirstPersonController(
    model='cube',
    collider='box',
    color=color.light_gray
) #기본적인 플래이어



ground=Entity(              #태스트용 땅 생성
    position=(0,0,0),
    model='plane',
    scale=(2,1,3),
    collider='mesh'
)


#맵은 St(n)으로 저장
# 3차원 배열 [[[]]] y z x
#0=공허 1=블럭 2=player 3=끝,클리어 -예정
#더 보기에 위에있는 배열이 y좌표가 더 낮음

#5*5*5

St1=[
    [
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]
    ],
    [
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,1,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]
    ],
    [
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,3,0],
        [0,0,0,0,0]
    ],
    [
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]
    ],
    [
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]
    ]

]

A=[]
l=makemap(St1,100,0)
A.append(l)
pl=(0,10,0)

def update():
    if player.position.y<-20:
        player.position=pl
        player.rotation=(0,90,0)


app.run()