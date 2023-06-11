import unittest

from cleaner import run_cleaner


class Test_run_cleaner(unittest.TestCase):

    def test_nothing(self):
        commands = []
        output = run_cleaner(commands)
        self.assertEqual(
            output,
            [])

if __name__ == '__main__':
    unittest.main()
