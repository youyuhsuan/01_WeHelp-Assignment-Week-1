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

