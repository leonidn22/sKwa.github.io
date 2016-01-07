import mypkg
import unittest


class TestStringMethods(unittest.TestCase):
    def test_foo(self):
        self.assertEqual(mypkg.code.foo(1, 2, 3), 6)


if __name__ == '__main__':
    unittest.main()
