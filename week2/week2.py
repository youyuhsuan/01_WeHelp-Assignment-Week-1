# task1
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
    return nearFriend

  
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

# task2
def createSchedule(consultants):
    schedule={}
    for consultant in consultants:
        schedule[consultant['name']] = [True] * 24
    return schedule

def book(consultants, hour, duration, criteria):
    sortCriteria = []
    if criteria ==  "price":
        sortCriteria = sorted(consultants, key=lambda x: x[criteria])
    else:
        sortCriteria = sorted(consultants, key=lambda x: x[criteria],reverse=True)
    
    for consultant in sortCriteria:
        Schedule = schedule[consultant['name']]
        availabilityCheck = True
    
        for i in range(hour, hour + duration, 1):
            if Schedule[i] != True:
                availabilityCheck = False
                break
    
        if availabilityCheck:
            for i in range(hour, hour + duration, 1):
                Schedule[i] = False
            print(consultant['name'])
            return consultant['name']
            
    print("No Service")
    return "No Service"
    
consultants = [
    {"name": "John", "rate": 4.5, "price": 1000},
    {"name": "Bob", "rate": 3, "price": 1200},
    {"name": "Jenny", "rate": 3.8, "price": 800},
]

schedule = createSchedule(consultants)

book(consultants, 15, 1, "price")  # Jenny
book(consultants, 11, 2, "price")  # Jenny
book(consultants, 10, 2, "price")  # John
book(consultants, 20, 2, "rate")  # John
book(consultants, 11, 1, "rate")  # Bob
book(consultants, 11, 2, "rate")  # No Service
book(consultants, 14, 3, "price")  # John

# task3
def func(*data):
    newData = []
    check = True
    for name in data:
        length = len(name)
        newData.append(name[length // 2])

    for index, value in enumerate(newData):
        if newData.count(value) == 1:
            check = False
            print (data[index])
            return data[index]
    if(check):
        print ("沒有")
        return "沒有"


func("彭大牆", "陳王明雅", "吳明")  # print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花")  # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花")  # print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆")  # print 夏曼藍波安

# task4
def get_number(index):
    number = 0
    for i in range(1, index + 1):
        if i % 3 == 0:
            number -= 1
        else:
            number += 4
    print(number)
    return number


get_number(1)  # print 4
get_number(5)  # print 15
get_number(10)  # print 25
get_number(30)  # print 70

# task5
def find(spaces, stat, n):
    availSeat = spaces
    for i in range(len(stat)):
        if stat[i] == 0:
            availSeat[i] = 0
    
    for i in range(n,max(availSeat),1):
        for j in range(len(availSeat)):
            if availSeat[j] == i:
                print(j)
                return j
    print(-1)        
    return -1

        
find([3, 1, 5, 4, 3, 2], [0, 1, 0, 1, 1, 1], 2) # print 5
find([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4) # print -1
find([4, 6, 5, 8], [0, 1, 1, 1], 4) # print 2

