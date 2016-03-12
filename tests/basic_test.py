import sys
sys.path.insert(0, r'/home/tyler/Desktop/pytesting/src')
import app

class TestClass:
    def test_one(self):
        x = 3
        assert app.addOne(x) == 4

    def test_two(self):
        x = 5
        assert app.timesTwo(x) == 10

    def test_failing(self):
        x = 2
        assert app.timesTwo(x) == 4
