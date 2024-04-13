def get_number(index):
    number = 0
    for i in range(1, index + 1):
        if i % 3 == 0:
            number -= 1
        else:
            number += 4
    print(number)
    # return number


get_number(1)  # print 4
get_number(5)  # print 15
get_number(10)  # print 25
get_number(30)  # print 70
