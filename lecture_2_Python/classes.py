class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(2, 3)
# print(p.x, p.y)

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    
    def add_passengers(self, name):
        if self.open_seats() > 0:
            self.passengers.append(name)
            return True
        return False

    def open_seats(self):
        return self.capacity -  len(self.passengers)

flight = Flight(3)
people = ["Saad", "Babar", "Shaheen", "Amir"]
for person in people:
    if flight.add_passengers(person) :
        print(f"Added {person} to the flight successfully")
    else:
        print(f"No available seats for {person}")