import turtle
## 전역변수 선언 부분 ##
i,k,tx,ty =[0]*4
sw,sh = 800,450



## 메인 코드 부분 ##
if __name__ =="__main__":
    turtle.title("거북 구구단")
    turtle.shape("turtle")
    turtle.setup(width=sw+50,height = sh +50)
    turtle.screensize(sw,sh)
    turtle.penup()
    tx,ty=-500,250
    turtle.goto(tx,ty)

    for i in range(1,10):
        for k in range(2,10):
            turtle.goto(tx+80*k,ty-40*i)
            gugu = str(k)+ 'x'+str(i)+ "="+ str(k*i)
            turtle.write(gugu,font = ("Arial",12,"bold"))

    turtle.don()

##2019038085_이현도##
