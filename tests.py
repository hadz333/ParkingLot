import unittest
from my_program import *

class TestObjects(unittest.TestCase):

    def testVehicle(self):
        v1 = Vehicle("KA-01-HH-1234", "White")
        self.assertEqual(v1.plate, "KA-01-HH-1234")
        self.assertEqual(v1.color, "White")

    def testParkingLot(self):
        p1 = ParkingLot(10)
        self.assertEqual(p1.spots[4], 'open')

if __name__ == '__main__':
    unittest.main()
