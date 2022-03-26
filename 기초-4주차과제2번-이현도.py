import operator

 

##전역 변수 선언 부분 ##

tlist = [("카이리",5),("어빙",8),("제임스",9),("하든",5),
             ("케빈",4),("듀란드",7),("데미안",3),("릴라드",8),
             ("스테픈",5),("커리",13)]
dic, li = {},[]
tmptup = None
trank,crank = 1,1
##메인 코드 부분##

if __name__== "__main__":
    for tmptup in tlist:
        tname = tmptup[0]
        tweight = tmptup[1]
        if tname in dic:
            dic[tname]+=tweight
        else:
            dic[tname]=tweight
    print('기차 수송량 목록=>',tlist)
    print("-----------------------")
    li = sorted(dic.items(),key = operator.itemgetter(1),reverse = True)
    print("기차\t종 수송량\t순위") 
    print(li[0][0],"\t",li[0][1],'\t\t',crank)
    for i in range(1,len(li)):
        trank += 1
        if li[i][1] == li[i-1][1]:
            pass
        else:
            crank = trank
        print(li[i][0], "\t",li[i][1],"\t\t",crank)


        ##2019038085_이현도##
