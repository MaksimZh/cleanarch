import unittest

from cleaner import *


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

class Test_run_command(unittest.TestCase):

    def test_move(self):
        self.assertEqual(
            run_command(Robot(0, 0, 0, Device.WATER), "move 100"),
            (Robot(100, 0, 0, Device.WATER), "POS 100, 0"))
        self.assertEqual(
            run_command(Robot(20, 30, 0, Device.SOAP), "move 100"),
            (Robot(120, 30, 0, Device.SOAP), "POS 120, 30"))
        self.assertEqual(
            run_command(Robot(0, 0, 90, Device.WATER), "move 50"),
            (Robot(0, 50, 90, Device.WATER), "POS 0, 50"))
        self.assertEqual(
            run_command(Robot(20, 30, 90, Device.SOAP), "move 50"),
            (Robot(20, 80, 90, Device.SOAP), "POS 20, 80"))
        self.assertEqual(
            run_command(Robot(0, 0, 30, Device.WATER), "move 100"),
            (Robot(87, 50, 30, Device.WATER), "POS 87, 50"))
        self.assertEqual(
            run_command(Robot(20, 30, 30, Device.SOAP), "move 100"),
            (Robot(107, 80, 30, Device.SOAP), "POS 107, 80"))
        
    def test_turn(self):
        self.assertEqual(
            run_command(Robot(0, 0, 0, Device.WATER), "turn 60"),
            (Robot(0, 0, 60, Device.WATER), "ANGLE 60"))
        self.assertEqual(
            run_command(Robot(0, 0, 0, Device.SOAP), "turn -60"),
            (Robot(0, 0, 300, Device.SOAP), "ANGLE 300"))
        self.assertEqual(
            run_command(Robot(0, 0, 150, Device.WATER), "turn 60"),
            (Robot(0, 0, 210, Device.WATER), "ANGLE 210"))
        self.assertEqual(
            run_command(Robot(0, 0, 150, Device.SOAP), "turn -60"),
            (Robot(0, 0, 90, Device.SOAP), "ANGLE 90"))
        
    def test_set_state(self):
        self.assertEqual(
            run_command(Robot(0, 0, 0, Device.WATER), "set water"),
            (Robot(0, 0, 0, Device.WATER), "STATE water"))
        self.assertEqual(
            run_command(Robot(100, 200, 90, Device.WATER), "set soap"),
            (Robot(100, 200, 90, Device.SOAP), "STATE soap"))
        self.assertEqual(
            run_command(Robot(0, 0, 0, Device.SOAP), "set brush"),
            (Robot(0, 0, 0, Device.BRUSH), "STATE brush"))
        
    def test_start(self):
        self.assertEqual(
            run_command(Robot(0, 0, 0, Device.WATER), "start"),
            (Robot(0, 0, 0, Device.WATER), "START WITH water"))
        self.assertEqual(
            run_command(Robot(100, 200, 90, Device.SOAP), "start"),
            (Robot(100, 200, 90, Device.SOAP), "START WITH soap"))
        
    def test_stop(self):
        self.assertEqual(
            run_command(Robot(0, 0, 0, Device.WATER), "stop"),
            (Robot(0, 0, 0, Device.WATER), "STOP"))
        self.assertEqual(
            run_command(Robot(100, 200, 90, Device.SOAP), "stop"),
            (Robot(100, 200, 90, Device.SOAP), "STOP"))


if __name__ == '__main__':
    unittest.main()
