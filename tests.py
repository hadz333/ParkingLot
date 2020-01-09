import unittest
from my_program import *

class TestObjects(unittest.TestCase):
    # test Vehicle object initialization
    def testVehicle(self):
        v1 = Vehicle("KA-01-HH-1234", "White")
        self.assertEqual(v1.plate, "KA-01-HH-1234")
        self.assertEqual(v1.color, "White")
    # test ParkingLot object initialization
    def testParkingLot(self):
        p1 = ParkingLot(10)
        self.assertEqual(p1.capacity, 11)
        self.assertEqual(p1.spots[4], 'open')
        self.assertEqual(p1.spots[10], 'open')

class TestSpots(unittest.TestCase):
    # test park vehicle function
    def testParkVehicle(self):
        v1 = Vehicle("KA-01-HH-2701", "Blue")
        p1 = ParkingLot(10)
        p1.parkVehicle(v1)
        self.assertEqual(p1.spots[1], v1)
        self.assertEqual(p1.spots[2], 'open')

    # make sure that parking lot full is handled
    def testParkingLotFull(self):
        v1 = Vehicle("KA-01-HH-2701", "Blue")
        p1 = ParkingLot(10)
        for i in range(1, p1.capacity):
            p1.parkVehicle(v1)
        self.assertEqual(p1.parkVehicle(v1), "Sorry, parking lot is full")

    # test vehicle leaving
    def testRemoveVehicle(self):
        v1 = Vehicle("KA-01-HH-2701", "Blue")
        p1 = ParkingLot(10)
        p1.parkVehicle(v1)
        p1.removeVehicle(1)
        self.assertEqual(p1.spots[1], 'open')



# this class will test special queries
class TestQueries(unittest.TestCase):
    # test vehicle slot number retrieval
    def testGetSlotNumberWithPlate(self):
        v1 = Vehicle("KA-01-HH-2701", "Blue")
        v2 = Vehicle("KA-01-HH-1234", "White")
        p1 = ParkingLot(5)
        p1.parkVehicle(v1)
        p1.parkVehicle(v2)
        self.assertEqual(p1.getSlotNumberWithPlate(v2.plate), 2)
        self.assertEqual(p1.getSlotNumberWithPlate("KB-02-HG-6921"), "Not found")

    # test registration number retrieval with color
    def testGetRegistrationNumbersWithColor(self):
        v1 = Vehicle("KA-01-HH-2701", "Blue")
        v2 = Vehicle("KA-01-HH-1234", "White")
        v3 = Vehicle("KA-02-HH-4321", "White")
        p1 = ParkingLot(5)
        p1.parkVehicle(v1)
        p1.parkVehicle(v2)
        p1.parkVehicle(v3)
        self.assertEqual(p1.getRegistrationNumbersWithColor("Blue"), ["KA-01-HH-2701"])
        self.assertEqual(p1.getRegistrationNumbersWithColor("White"), ["KA-01-HH-1234", "KA-02-HH-4321"])
        self.assertEqual(p1.getRegistrationNumbersWithColor("Orange"), [])

    # test slot retrieval with color
    def testGetSlotsWithColor(self):
        v1 = Vehicle("KA-01-HH-2701", "Blue")
        v2 = Vehicle("KA-01-HH-1234", "White")
        v3 = Vehicle("KA-02-HH-4321", "White")
        p1 = ParkingLot(5)
        p1.parkVehicle(v1)
        p1.parkVehicle(v2)
        p1.parkVehicle(v3)
        self.assertEqual(p1.getSlotsWithColor("Blue"), [1])
        self.assertEqual(p1.getSlotsWithColor("White"), [2, 3])
        self.assertEqual(p1.getSlotsWithColor("Black"), [])


if __name__ == '__main__':
    unittest.main()
