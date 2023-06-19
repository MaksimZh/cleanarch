import unittest

from driver import RobotCleanerDriver


class Test_run_cleaner(unittest.TestCase):

    def test_example(self):
        commands = [
            "move 100",
            "turn -90",
            "set soap",
            "start",
            "move 50",
            "stop",
        ]
        test = [
            "POS 100, 0",
            "ANGLE 270",
            "STATE soap",
            "START WITH soap",
            "POS 100, -50",
            "STOP",
        ]
        output = list[str]()
        rcd = RobotCleanerDriver(lambda c: output.append(c))
        for i in range(len(commands)):
            self.assertEqual(output, test[:i])
            rcd.run(commands[i])
        self.assertEqual(output, test)

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
        test = [
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
        ]
        output = list[str]()
        rcd = RobotCleanerDriver(lambda c: output.append(c))
        for i in range(len(commands)):
            self.assertEqual(output, test[:i])
            rcd.run(commands[i])
        self.assertEqual(output, test)


if __name__ == '__main__':
    unittest.main()
