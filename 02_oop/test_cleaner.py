import unittest

from cleaner import *



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


class Test_Location(unittest.TestCase):

    def test_init(self):
        p = Location(0, 0)
        self.assertEqual((p.get_x(), p.get_y()), (0, 0))
        p = Location(4, 2)
        self.assertEqual((p.get_x(), p.get_y()), (4, 2))
        p = Location(-4, -2)
        self.assertEqual((p.get_x(), p.get_y()), (-4, -2))

    def test_shift_0(self):
        self.assertEqual(
            Location(0, 0).shift(Angle(0), Distance(0)),
            Location(0, 0))
        self.assertEqual(
            Location(0, 0).shift(Angle(0), Distance(100)),
            Location(100, 0))
        self.assertEqual(
            Location(0, 0).shift(Angle(90), Distance(100)),
            Location(0, 100))
        self.assertEqual(
            Location(0, 0).shift(Angle(180), Distance(100)),
            Location(-100, 0))
        self.assertEqual(
            Location(0, 0).shift(Angle(270), Distance(100)),
            Location(0, -100))
        self.assertEqual(
            Location(0, 0).shift(Angle(30), Distance(100)),
            Location(87, 50))

    def test_shift(self):
        self.assertEqual(
            Location(200, 300).shift(Angle(0), Distance(0)),
            Location(200, 300))
        self.assertEqual(
            Location(200, 300).shift(Angle(0), Distance(100)),
            Location(300, 300))
        self.assertEqual(
            Location(200, 300).shift(Angle(90), Distance(100)),
            Location(200, 400))
        self.assertEqual(
            Location(200, 300).shift(Angle(180), Distance(100)),
            Location(100, 300))
        self.assertEqual(
            Location(200, 300).shift(Angle(270), Distance(100)),
            Location(200, 200))
        self.assertEqual(
            Location(200, 300).shift(Angle(30), Distance(100)),
            Location(287, 350))



class Test_RobotCleaner(unittest.TestCase):

    def test_init(self):
        rc = RobotCleaner(Location(0, 0), Angle(0), Device.WATER)
        self.assertEqual(rc.get_device(), Device.WATER)
        self.assertEqual(rc.get_location(), Location(0, 0))
        self.assertEqual(rc.get_angle(), Angle(0))

        rc = RobotCleaner(Location(100, 200), Angle(60), Device.SOAP)
        self.assertEqual(rc.get_device(), Device.SOAP)
        self.assertEqual(rc.get_location(), Location(100, 200))
        self.assertEqual(rc.get_angle(), Angle(60))


    def test_motion(self):
        rc = RobotCleaner(Location(0, 0), Angle(0), Device.WATER)
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
        rc = RobotCleaner(Location(0, 0), Angle(0), Device.WATER)
        self.assertEqual(rc.get_device(), Device.WATER)
        rc.set_device(Device.WATER)
        self.assertEqual(rc.get_device(), Device.WATER)
        rc.set_device(Device.SOAP)
        self.assertEqual(rc.get_device(), Device.SOAP)
        rc.set_device(Device.BRUSH)
        self.assertEqual(rc.get_device(), Device.BRUSH)


class Test_run_cleaner(unittest.TestCase):

    def test_nothing(self):
        commands = []
        output = run_cleaner(commands)
        self.assertEqual(
            output,
            [])
        
    def test_example(self):
        commands = [
            "move 100",
            "turn -90",
            "set soap",
            "start",
            "move 50",
            "stop",
        ]
        output = run_cleaner(commands)
        self.assertEqual(
            output,
            [
                "POS 100, 0",
                "ANGLE 270",
                "STATE soap",
                "START WITH soap",
                "POS 100, -50",
                "STOP",
            ])
        
    def test_square(self):
        commands = [
            "turn 90",
            "set brush",
            "start",
            "move 100",
            "turn -90",
            "move 100",
            "turn -90",
            "move 100",
            "turn -90",
            "move 100",
            "stop",
            "turn -90",
            "set soap",
            "start",
            "move 100",
            "turn -90",
            "move 100",
            "turn -90",
            "move 100",
            "turn -90",
            "move 100",
            "stop",
            "turn -90",
            "set water",
            "start",
            "move 100",
            "turn -90",
            "move 100",
            "turn -90",
            "move 100",
            "turn -90",
            "move 100",
            "stop",
        ]
        output = run_cleaner(commands)
        self.assertEqual(
            output,
            [
                "ANGLE 90",
                "STATE brush",
                "START WITH brush",
                "POS 0, 100",
                "ANGLE 0",
                "POS 100, 100",
                "ANGLE 270",
                "POS 100, 0",
                "ANGLE 180",
                "POS 0, 0",
                "STOP",
                "ANGLE 90",
                "STATE soap",
                "START WITH soap",
                "POS 0, 100",
                "ANGLE 0",
                "POS 100, 100",
                "ANGLE 270",
                "POS 100, 0",
                "ANGLE 180",
                "POS 0, 0",
                "STOP",
                "ANGLE 90",
                "STATE water",
                "START WITH water",
                "POS 0, 100",
                "ANGLE 0",
                "POS 100, 100",
                "ANGLE 270",
                "POS 100, 0",
                "ANGLE 180",
                "POS 0, 0",
                "STOP",
            ])


if __name__ == '__main__':
    unittest.main()
