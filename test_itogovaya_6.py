import unittest
from itogovaya_6 import funkcia

class Test_Main(unittest.TestCase):
    def test_A(self):
        self.assertEqual(funkcia(170),(5,6))
    def test_B(self):
        self.assertNotEqual(funkcia('ауе'),TypeError)
    def test_C(self):
        self.assertEqual(funkcia(2),(0, 0))
    def test_D(self):
        self.assertEqual(funkcia(30),(0, 11))
    def test_F(self):
        self.assertNotEqual(funkcia([1]),TypeError)
        
if __name__ == '__main__':
    unittest.main()
