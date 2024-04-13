def find(spaces, stat, n):
    availSeat = spaces
    for i in range(len(stat)):
        if stat[i] == 0:
            availSeat[i] = 0
    
    for i in range(n,max(availSeat),1):
        for j in range(len(availSeat)):
            if availSeat[j] == i:
                return j
            
    return -1

        
find([3, 1, 5, 4, 3, 2], [0, 1, 0, 1, 1, 1], 2) # print 5
find([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4) # print -1
find([4, 6, 5, 8], [0, 1, 1, 1], 4) # print 2
