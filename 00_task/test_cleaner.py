import unittest

from cleaner import State, Device, Angle, Distance, Position, RobotCleaner


class Test_Angle(unittest.TestCase):

    def test_init(self):
        self.assertEqual(int(Angle(0)), 0)
        self.assertEqual(int(Angle(42)), 42)

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


class Test_Distance(unittest.TestCase):

    def test_init(self):
        self.assertEqual(int(Distance(0)), 0)
        self.assertEqual(int(Distance(10)), 10)

        self.assertEqual(Distance(0), Distance(0))
        self.assertEqual(Distance(10), Distance(10))

        self.assertRaises(AssertionError, lambda: Distance(-1))


class Test_Position(unittest.TestCase):

    def test_init(self):
        p = Position(0, 0)
        self.assertEqual((p.get_x(), p.get_y()), (0, 0))
        p = Position(4, 2)
        self.assertEqual((p.get_x(), p.get_y()), (4, 2))
        p = Position(-4, -2)
        self.assertEqual((p.get_x(), p.get_y()), (-4, -2))

    def test_shift_0(self):
        self.assertEqual(
            Position(0, 0).shift(Angle(0), Distance(0)),
            Position(0, 0))
        self.assertEqual(
            Position(0, 0).shift(Angle(0), Distance(100)),
            Position(100, 0))
        self.assertEqual(
            Position(0, 0).shift(Angle(90), Distance(100)),
            Position(0, 100))
        self.assertEqual(
            Position(0, 0).shift(Angle(180), Distance(100)),
            Position(-100, 0))
        self.assertEqual(
            Position(0, 0).shift(Angle(270), Distance(100)),
            Position(0, -100))
        self.assertEqual(
            Position(0, 0).shift(Angle(30), Distance(100)),
            Position(87, 50))

    def test_shift(self):
        self.assertEqual(
            Position(200, 300).shift(Angle(0), Distance(0)),
            Position(200, 300))
        self.assertEqual(
            Position(200, 300).shift(Angle(0), Distance(100)),
            Position(300, 300))
        self.assertEqual(
            Position(200, 300).shift(Angle(90), Distance(100)),
            Position(200, 400))
        self.assertEqual(
            Position(200, 300).shift(Angle(180), Distance(100)),
            Position(100, 300))
        self.assertEqual(
            Position(200, 300).shift(Angle(270), Distance(100)),
            Position(200, 200))
        self.assertEqual(
            Position(200, 300).shift(Angle(30), Distance(100)),
            Position(287, 350))


class Test_RobotCleaner(unittest.TestCase):

    def test_init(self):
        rc = RobotCleaner()
        self.assertEqual(rc.get_state(), State.IDLE)
        self.assertEqual(rc.get_device(), Device.NONE)
        self.assertEqual(rc.get_position(), Position(0, 0))
        self.assertEqual(rc.get_angle(), Angle(0))


if __name__ == '__main__':
    unittest.main()
