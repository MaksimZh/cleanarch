import unittest

from devices import Device


class Test_Device(unittest.TestCase):

    def test(self):
        d = Device("water", "soap", "brush")
        self.assertEqual(d.get_name(), "water")
        d.select("water")
        self.assertEqual(d.get_name(), "water")
        d.select("soap")
        self.assertEqual(d.get_name(), "soap")
        d.select("brush")
        self.assertEqual(d.get_name(), "brush")

    def test_error(self):
        self.assertRaises(
            AssertionError,
            lambda: Device("water", "soap", "brush").select("laser"))


if __name__ == '__main__':
    unittest.main()
