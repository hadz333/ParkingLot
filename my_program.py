# Vehicle object, stores license plate and color
class Vehicle:
  def __init__(self, plate, color):
    self.plate = plate
    self.color = color

class ParkingLot:
    def __init__(self, capacity):
        # spots is a list that keeps track of all parking spots
        self.spots = []
        # capacity increased by 1 (index 0 in list is never used so we don't have to add 1 later)
        self.capacity = capacity + 1
        for i in range(0, self.capacity):
            self.spots.append('open')

    # This function will park the vehicle passed in at the nearest stall
    def parkVehicle(self, vehicle):
        # start from first stall and check ascending (further from entrance)
        for i in range(1, self.capacity):
            if self.spots[i] == 'open':
                self.spots[i] = vehicle
                break
            if i == (self.capacity - 1):
                print("Sorry, parking lot is full")
                return "Sorry, parking lot is full"