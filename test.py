
import unittest

class TestExample(unittest.TestCase):
    
    def test_case_1(self):
        self.assertEqual(1 + 1, 2)

    def test_case_2(self):
        self.assertTrue(isinstance("hello", str))

if __name__ == '__main__':
    unittest.main()