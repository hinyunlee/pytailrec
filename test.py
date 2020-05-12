import unittest
from tailrec import tailrec

class Test(unittest.TestCase):
    def test_evenodd(self):
        @tailrec
        def iseven(n):
            if n == 0:
                return True
            else:
                return isodd.tailcall(n - 1)

        @tailrec
        def isodd(n):
            if n == 0:
                return False
            else:
                return iseven.tailcall(n - 1)

        self.assertTrue(iseven(0))
        self.assertFalse(isodd(0))
        self.assertFalse(iseven(1))
        self.assertTrue(isodd(1))
        self.assertTrue(iseven(2))
        self.assertFalse(isodd(2))
        self.assertTrue(iseven(100))
        self.assertFalse(isodd(100))
        self.assertFalse(iseven(101))
        self.assertTrue(isodd(101))
        self.assertTrue(iseven(1000000))
        self.assertFalse(isodd(1000000))
        self.assertFalse(iseven(1000001))
        self.assertTrue(isodd(1000001))


    def test_evenodd_no_tco(self):
        def iseven(n):
            if n == 0:
                return True
            else:
                return isodd(n - 1)

        def isodd(n):
            if n == 0:
                return False
            else:
                return iseven(n - 1)

        try:
            iseven(1000000)
            self.fail()
        except Exception as e:
            print(e)

        try:
            isodd(1000000)
            self.fail()
        except Exception as e:
            print(e)

        try:
            iseven(1000001)
            self.fail()
        except Exception as e:
            print(e)

        try:
            isodd(1000001)
            self.fail()
        except Exception as e:
            print(e)

if __name__ == '__main__':
    unittest.main()
