import unittest

from cleaner import State, Device, Angle, Position, RobotCleaner


class Test_Angle(unittest.TestCase):

    def test_init(self):
        self.assertEqual(Angle(0), Angle(0))
        self.assertEqual(Angle(42), Angle(42))
        self.assertEqual(Angle(180), Angle(180))
        self.assertEqual(Angle(359), Angle(359))
        self.assertEqual(Angle(360), Angle(0))
        self.assertEqual(Angle(361), Angle(1))
        self.assertEqual(Angle(1000), Angle(280))
        self.assertEqual(Angle(-42), Angle(318))
        self.assertEqual(Angle(-180), Angle(180))
        self.assertEqual(Angle(-359), Angle(1))
        self.assertEqual(Angle(-360), Angle(0))
        self.assertEqual(Angle(-361), Angle(359))
        self.assertEqual(Angle(-1000), Angle(80))

    def test_turn(self):
        self.assertEqual(Angle(0).turn(42), Angle(42))
        self.assertEqual(Angle(0).turn(-42), Angle(-42))
        self.assertEqual(Angle(180).turn(42), Angle(180 + 42))
        self.assertEqual(Angle(180).turn(420), Angle(180 + 420))
        self.assertEqual(Angle(180).turn(-420), Angle(180 - 420))



class Test_Position(unittest.TestCase):

    def test_init(self):
        pass


class Test_RobotCleaner(unittest.TestCase):

    def test_init(self):
        rc = RobotCleaner()
        self.assertEqual(rc.get_state(), State.IDLE)
        self.assertEqual(rc.get_device(), Device.NONE)
        self.assertEqual(rc.get_position(), Position(0, 0))
        self.assertEqual(rc.get_angle(), Angle(0))


if __name__ == '__main__':
    unittest.main()
