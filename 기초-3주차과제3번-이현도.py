## 전역변수 선언 부분 ##
i,k,heartnum =0,0,0
numstr,ch,heartstr = "","",""


## 메인 코드 부분 ##
if __name__ =="__main__":
    numstr = input("숫자를 여러 개 입력하세요 :" )
    print("")
    i = 0
    ch = numstr[i]
    while True:
        heartnum = int(ch)

        heartstr=""
        for k in range(0,heartnum):
            heartstr +="\u2665"
            k+=1

        print (heartstr)
        i +=1
        if (i>len(numstr)-1):
            break

        ch=numstr[i]

##2019038085_이현도##
