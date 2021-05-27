import unittest

from calc import compose_Formula
n = 0

class TestCalc(unittest.TestCase):
    def __init__(self,r):
        r = None

        string1 = compose_Formula(['+'],[i for i in range(3,6)])
        for ch in string1:
            if (ch == '+'):
                number = n + 1
        if (n >=3) & (n <=5):
            self.r = 1
    def test01(self,r):
        print('r')
        self.assertEqual(1, self.r)

if __name__ == '__main__':
    unittest.main()
