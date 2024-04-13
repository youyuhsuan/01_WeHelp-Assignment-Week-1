JohnSchedule = [True] * 24
BobSchedule = [True] * 24
JennySchedule = [True] * 24

def book(consultants, hour, duration, criteria):
    sortCriteria = []
    if criteria ==  "price":
        sortCriteria = sorted(consultants, key=lambda x: x[criteria])

    else:
        sortCriteria = sorted(consultants, key=lambda x: x[criteria],reverse=True)
    
    for consultant in sortCriteria:
        Schedule = None
        if consultant["name"] == "John":
            Schedule = JohnSchedule
        elif consultant["name"] == "Bob":
            Schedule = BobSchedule
        elif consultant["name"] == "Jenny":
            Schedule = JennySchedule

        availabilityCheck = True
    
        for i in range(hour, hour + duration, 1):
            if Schedule[i] != True:
                availabilityCheck = False
                break
    
        if availabilityCheck:
            for i in range(hour, hour + duration, 1):
                Schedule[i] = False
            return consultant["name"]
    return "No Service"
    
consultants = [
    {"name": "John", "rate": 4.5, "price": 1000},
    {"name": "Bob", "rate": 3, "price": 1200},
    {"name": "Jenny", "rate": 3.8, "price": 800},
]

book(consultants, 15, 1, "price")  # Jenny
book(consultants, 11, 2, "price")  # Jenny
book(consultants, 10, 2, "price")  # John
book(consultants, 20, 2, "rate")  # John
book(consultants, 11, 1, "rate")  # Bob
book(consultants, 11, 2, "rate")  # No Service
book(consultants, 14, 3, "price")  # John

