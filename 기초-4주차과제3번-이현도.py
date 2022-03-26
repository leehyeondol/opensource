import random
import turtle

myTurtle, tX, tY, tColor, tSize, tShape, tSum = [None] * 7## 엑스 와이 자표 합##
playerTurtles = []
swidth, sheight = 500, 500

if __name__ == "__main__" :
    turtle.title('거북 리스트 활용(정렬)')
    turtle.setup(width = swidth + 50, height = sheight + 50)##창의 크기 결정##
    turtle.screensize(swidth, sheight)##창의 크기 결정##
    for i in range(0, 5) :## 랜덤을;거북이 객체 10개 생성 후 playerTuertles에 넣기##
        myTurtle = turtle.Turtle('turtle')
        tX = random.randrange(-swidth / 2, swidth / 2)
        tY = random.randrange(-sheight / 2, sheight / 2)
        r = random.random(); g = random.random(); b = random.random()
        tSize = random.randrange(1, 100)/10
        tSum = tSize
        playerTurtles.append([myTurtle, tX, tY, tSize, r, g, b, tSum])##2차원 리스트 형태##

##tSum을 키로해서 플레이어 터틀을 오름차순으로 정렬한 다음 reverse##
##플레이어터틀의 각 원소를 반환하면 이를 터틀로 받아 터틀[7]인 tSum을 키로 사용##
        
    sortedTurtles = sorted(playerTurtles, key = lambda turtles : turtles[7])##정렬. 키는 람다 터틀. 값은 터틀의 크기##
    for index, tList in enumerate(sortedTurtles[0:]):
        myTurtle = tList[0]
        myTurtle.color((tList[4], tList[5], tList[6]))
        myTurtle.pencolor((tList[4], tList[5], tList[6]))
        myTurtle.turtlesize(tList[3])
        myTurtle.penup()
        if index == 0:##첫 번째 거북이는 이전 거북이가 없기 때문에 해당 위치로만 이동##
            myTurtle.goto(tList[1], tList[2])
            continue
        myTurtle.goto(sortedTurtles[index-1][1], sortedTurtles[index-1][2])## 선을 그을 거북이를 이전의 거북이위치로 이동##
        myTurtle.pendown()
        myTurtle.goto(tList[1], tList[2])## 설정된 거북이의 좌표로 이동하면서 선 긋기##
        myTurtle.setheading(random.randrange(0,360 ))##거북이 각도 랜덤하게 돌리기##

        ##2019038085_이현도##
        
turtle.done()
