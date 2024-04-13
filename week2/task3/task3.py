def func(*data):
    newData = []
    for name in data:
        length = len(name)
        newData.append(name[length // 2])

    for index, value in enumerate(newData):
        if newData.count(value) == 1:
            return data[index]
    else:
        return "沒有"


func("彭大牆", "陳王明雅", "吳明")  # print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花")  # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花")  # print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆")  # print 夏曼藍波安