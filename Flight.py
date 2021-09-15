class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self,name):
        if not self.open_seats():  # same as if self.open_seats == 0
            return False           # more pythonic :)
        self.passengers.append(name)
        return True
    
    def open_seats(self):
        return self.capacity-len(self.passengers)

flight = Flight(3)
peaple = ["Harry","Ron","Hermione","Ginny"]
for person in peaple:
    if flight.add_passenger(person):
        print(f"The passenger {person} was added successfuly")
    else:
        print(f"faild to add {person} as a passenger")