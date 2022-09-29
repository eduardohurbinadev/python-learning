import unittest

def guess_number(num):
    if num == 1:
        return True
    else:
        return False

class TestIncrease(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(guess_number(3), )

if __name__ == '__main__':
    unittest.main()

