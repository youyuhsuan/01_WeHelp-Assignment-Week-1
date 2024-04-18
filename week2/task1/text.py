def find_and_print(messages, current_station):
    #Xiaobitan放在greenLine最後一個元素變成greenLineModified
    greenLineModified=["Songshan","Nanjing Sanmin","Taipei Arena","Nanjing Fuxing","Songjiang Nanjing","Zhongshan", 
               "Beimen","Ximen","Xiaonanmen","Chiang Kai-shek Memorial Hall","Guting","Taipower Building",
                "Gongguan","Wanlong","Jingmei","Dapinglin","Qizhang","Xindian City Hall","Xindian","Xiaobitan"]
    Frdlocation={} 
    #將message中朋友的訊息解構出來放入Frdlocation字典中key:"朋友名"，value:"朋友所在的站名"
    
    for friend,stationText in messages.items():
        friendstation=[str for str in greenLineModified if str in stationText]
        Frdlocation[friend]=friendstation[0]
        
        # 讓Frdlocation變成{朋友:所在地點}此種字典=>Frdlocation={"Leslie":"Xiaobitan","Bob":"Ximen","Mary":"Jingmei","Copper":"Taipei Arena","Vivian":"Xindian"}
    
    friendToStationsDistanceSet={}
    #計算每個朋友距離每個車站的距離並蒐集成{朋友:[3,2,1,0,1,2,3.....]}的字典，此字典例子=>朋友在Nanjing Fuxing
    
    for friend,location in Frdlocation.items():
        #將朋友與該朋友所在車站名稱拿出來遍歷
        
        if location!="Xiaobitan":
            #如果該朋友所在車站不是"Xiaobitan"，將該朋友距離每個車站的距離蒐集成list並將該擴充後的list成為朋友名字所對應的鍵值
            
            friendToStationsDistanceSet[friend]=[abs(greenLineModified[:-1].index(itm)-greenLineModified[:-1].index(location)) for itm in greenLineModified[:-1]]
            #由於"Xiaobitan"距離其他車站距離="Qizhang"距離其他車站距離+1站
            #以下特別加入"Xiaobitan"距離朋友的距離加入該list，並將該擴充後的list成為朋友名字所對應的鍵值
            
            friendToStationsDistanceSet[friend].append(abs(greenLineModified[:-1].index(location)-greenLineModified[:-1].index("Qizhang"))+1)
            
        elif location=="Xiaobitan":#如果該朋友所在車站剛好是"Xiaobitan"
            location="Qizhang"#將朋友所在車站換成"Qizhang"站去計算，最後統一加上1
            friendToStationsDistanceSet[friend]=[abs(greenLineModified[:-1].index(itm)-greenLineModified[:-1].index(location))+1 for itm in greenLineModified[:-1]]
            #手動加入朋友距離"Xiaobitan"距離進入list鍵值
            friendToStationsDistanceSet[friend].append(abs(greenLineModified[:-1].index(location)-greenLineModified[:-1].index("Qizhang")))

    myindex=greenLineModified.index(current_station)#current_station目前所在位置


    dis_of_friends={}#計算所有朋友與current_station的距離放入dis_of_friends字典中
    for friend,distSet in friendToStationsDistanceSet.items():
        dis_of_friends[friend]=distSet[myindex]
    # print(dis_of_friends)
    #找出最近距離的朋友們的名字
    min_dist_of_friends = min(dis_of_friends.values())#蒐集距離最近的朋友們的距離
    nearest_friends = [key for key, value in dis_of_friends.items() if value == min_dist_of_friends]
    for frd in nearest_friends:
        print(frd,end=" ")#印出最近距離的朋友們的名字
    print("")
    
# your code here
messages={
"Leslie":"I'm at home near Xiaobitan station.",
"Bob":"I'm at Ximen MRT station.",
"Mary":"I have a drink near Jingmei MRT station.",
"Copper":"I just saw a concert at Taipei Arena.",
"Vivian":"I'm at Xindian station waiting for you."
}
find_and_print(messages, "Wanlong") # print Mary
find_and_print(messages, "Songshan") # print Copper
find_and_print(messages, "Qizhang") # print Leslie
find_and_print(messages, "Ximen") # print Bob
find_and_print(messages, "Xindian City Hall") # print Vivian
