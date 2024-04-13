def find_and_print(messages, current_station):
    greenLine=["Songshan", "Nanjing Sanmin", "Taipei Arena", "Nanjing Fuxing", "Songjing Nanjing", "Zhongshan", "Beimen", "Ximen", "Xiaonanmen", "Chiang Kai-Shek Memorial Hall", "Guting", "Taipower Building", "Gongguan", "Wanlong", "Jingmei", "Dapinglin", "Qizhang", "Xiaobitan", "Xindian City Hall", "Xindian"]
    minNear=float("inf")
    currentStationIndex=greenLine.index(current_station)
    for key,value in messages.items():
        for greenIndex,station in enumerate(greenLine):
            if station in value:
                distance=abs(greenIndex-currentStationIndex)
                if current_station == "Xindian City Hall" and station == "Xindian":
                    minNear = distance
                    friend = key
                    break
                elif distance < minNear:
                    minNear = distance
                    friend=key
    print(friend)
messages={
"Leslie":"I'm at home near Xiaobitan station.",
 "Bob":"I'm at Ximen MRT station.",
"Mary":"I have a drink near Jingmei MRT station.", 
"Copper":"I just saw a concert at Taipei Arena.",
 "Vivian":"I'm at Qizhan station waiting for you."
}
find_and_print(messages, "Wanlong") # print Mary 
find_and_print(messages, "Songshan") # print Copper 
find_and_print(messages, "Xindian") # print Leslie 
find_and_print(messages, "Ximen") # print Bob 
find_and_print(messages, "Xindian City Hall") # print Vivian