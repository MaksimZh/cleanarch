import unittest

from cleaner import State, Device, Angle, Position, RobotCleaner


class Test_Angle(unittest.TestCase):

    def test_init(self):
        pass


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
