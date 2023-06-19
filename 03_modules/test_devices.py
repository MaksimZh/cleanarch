import unittest

from devices import Device


class Test_RobotCleaner(unittest.TestCase):

    def test(self):
        d = Device("water", "soap", "brush")
        self.assertEqual(d.get(), "water")
        d.select("water")
        self.assertEqual(d.get(), "water")
        d.select("soap")
        self.assertEqual(d.get(), "soap")
        d.select("brush")
        self.assertEqual(d.get(), "brush")

    def test_error(self):
        self.assertRaises(
            AssertionError,
            lambda: Device("water", "soap", "brush").select("laser"))


if __name__ == '__main__':
    unittest.main()
