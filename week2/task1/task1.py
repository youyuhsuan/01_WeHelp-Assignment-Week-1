def find_and_print(messages, current_station):
    SongshanXindian_Line = [
        "Songshan",
        "Nanjing Sanmin", 
        "Taipei Arena",
        "Nanjing Fuxing",
        "Songjing Nanjing", 
        "Zhongshan",
        "Beimen", 
        "Ximen", 
        "Xiaonanmen", 
        "Chiang Kai-Shek Memorial Hall", 
        "Guting",
        "Taipower Building", 
        "Gongguan",
        "Wanlong",
        "Jingmei",
        "Dapinglin",
        "Qizhang", 
        "Xiaobitan",
        "Xindian City Hall", 
        "Xindian"
    ]
  
    current_position = SongshanXindian_Line.index(current_station)
    comparisonValue = float("inf")
    SongshanXindian_Line_tempVaule = None
    nearFriend = ""
  
    for name,value in messages.items():
        for line,station in enumerate(SongshanXindian_Line):
            if station in value:
                SongshanXindian_Line_tempVaule=abs(line-current_position)
                if station in value:
                    if current_station == "Xindian City Hall" and station == "Xindian":
                        comparisonValue = line
                        nearFriend = name
                        break
                    elif SongshanXindian_Line_tempVaule < comparisonValue:
                        comparisonValue = SongshanXindian_Line_tempVaule
                        nearFriend=name
    print(nearFriend) 

  
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