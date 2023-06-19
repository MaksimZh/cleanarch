import unittest

from motion import Angle, Location, Distance
from cleaner import RobotCleaner


class Test_RobotCleaner(unittest.TestCase):

    def test_init(self):
        rc = RobotCleaner(Location(0, 0), Angle(0), "water")
        self.assertEqual(rc.get_device_name(), "water")
        self.assertEqual(rc.get_location(), Location(0, 0))
        self.assertEqual(rc.get_angle(), Angle(0))

        rc = RobotCleaner(Location(100, 200), Angle(60), "soap")
        self.assertEqual(rc.get_device_name(), "soap")
        self.assertEqual(rc.get_location(), Location(100, 200))
        self.assertEqual(rc.get_angle(), Angle(60))


    def test_motion(self):
        rc = RobotCleaner(Location(0, 0), Angle(0), "water")
        self.assertEqual(rc.get_location(), Location(0, 0))
        self.assertEqual(rc.get_angle(), Angle(0))
        rc.move(Distance(100))
        self.assertEqual(rc.get_location(), Location(100, 0))
        self.assertEqual(rc.get_angle(), Angle(0))
        rc.move(Distance(20))
        self.assertEqual(rc.get_location(), Location(120, 0))
        self.assertEqual(rc.get_angle(), Angle(0))
        rc.turn(30)
        self.assertEqual(rc.get_location(), Location(120, 0))
        self.assertEqual(rc.get_angle(), Angle(30))
        rc.turn(60)
        self.assertEqual(rc.get_location(), Location(120, 0))
        self.assertEqual(rc.get_angle(), Angle(90))
        rc.move(Distance(30))
        self.assertEqual(rc.get_location(), Location(120, 30))
        self.assertEqual(rc.get_angle(), Angle(90))
        rc.turn(-30)
        self.assertEqual(rc.get_location(), Location(120, 30))
        self.assertEqual(rc.get_angle(), Angle(60))
        rc.move(Distance(100))
        self.assertEqual(rc.get_location(), Location(170, 117))
        self.assertEqual(rc.get_angle(), Angle(60))


    def test_device(self):
        rc = RobotCleaner(Location(0, 0), Angle(0), "water", "soap", "brush")
        self.assertEqual(rc.get_device_name(), "water")
        rc.select_device("water")
        self.assertEqual(rc.get_device_name(), "water")
        rc.select_device("soap")
        self.assertEqual(rc.get_device_name(), "soap")
        rc.select_device("brush")
        self.assertEqual(rc.get_device_name(), "brush")


if __name__ == '__main__':
    unittest.main()
