# Vehicle object,
class Vehicle:
  def __init__(self, plate, color):
    self.plate = plate
    self.color = color

class ParkingLot:
    def __init__(self, capacity):
        # spots is a list that keeps track of all parking spots
        self.spots = []
        for i in range(0, capacity):
            self.spots.append('open')

v1 = Vehicle("KA-01-HH-1234", "White")
print(v1.color)
