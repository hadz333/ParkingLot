import sys

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
                return "Allocated slot number: " + str(i)
                break
            # we have gotten to the end without any open spots
            if i == (self.capacity - 1):
                return "Sorry, parking lot is full"

    # function for vehicle leaving
    def removeVehicle(self, spotNumber):
        self.spots[int(spotNumber)] = 'open'
        return ("Slot number " + str(spotNumber) + " is free")

    # function to retrieve slot number of a specific registration
    def getSlotNumberWithPlate(self, plate):
        for i in range(1, self.capacity):
            if self.spots[i] != 'open':
                if self.spots[i].plate == plate:
                    return i
        return "Not found"

    # function to retrieve registration number of all vehicles with specified color
    def getRegistrationNumbersWithColor(self, color):
        registrationNumbers = []
        for i in range(1, self.capacity):
            if self.spots[i] != 'open':
                if self.spots[i].color == color:
                    registrationNumbers.append(self.spots[i].plate)
        return registrationNumbers

    # function to retrieve all slots with specific color
    def getSlotsWithColor(self, color):
        slots = []
        for i in range(1, self.capacity):
            if self.spots[i] != 'open':
                if self.spots[i].color == color:
                    slots.append(i)
        return slots

def executeCommand(cmd):
    global parkingLot1
    # cmd[0] is the first word in the command entered by user
    if cmd[0] == 'create_parking_lot':
        parkingLot1 = ParkingLot(int(cmd[1]))
        print("Created a parking lot with " + str(cmd[1]) + " slots")

    if cmd[0] == 'park':
        vehicle = Vehicle(cmd[1], cmd[2])
        print(parkingLot1.parkVehicle(vehicle))

    if cmd[0] == 'leave':
        print(parkingLot1.removeVehicle(cmd[1]))

    if cmd[0] == 'status':
        print("Slot No. \tRegistration No \tColour")
        for car in parkingLot1.spots:
            if car != 'open':
                print(str(parkingLot1.getSlotNumberWithPlate(car.plate)) +  "\t" + car.plate + "\t" + car.color)

    if cmd[0] == 'slot_number_for_registration_number':
        print(str(parkingLot1.getSlotNumberWithPlate(cmd[1])))

    if cmd[0] == 'registration_numbers_for_cars_with_colour':
        print(str(parkingLot1.getRegistrationNumbersWithColor(cmd[1])))

    if cmd[0] == 'slot_numbers_for_cars_with_colour':
        print(str(parkingLot1.getSlotsWithColor(cmd[1])))

if (len(sys.argv) > 1 and sys.argv[0] == "my_program.py"):
    # using an input file
    inputFile = sys.argv[1] # input file
    f = open(inputFile, "r") # read only
    contents = f.read()
    lines = contents.split('\n') # list of all commands (line by line)
    for command in lines:
        command_parsed = command.split(' ')
        executeCommand(command_parsed)

elif (sys.argv[0] == "my_program.py"):
    # Interactive mode
    print("Your are now in interactive mode. Presss Ctrl+C to quit.")
    while True:
        # wait for user's input
        line = input()
        # parse user's input into readable commands (separated by space)
        line = line.split(' ')
        executeCommand(line)
