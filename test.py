#coding=utf-8
__author__ = 'ding'
import unittest
import screen
screen.W, screen.H = 3, 3

from main import is_valid, is_around_valid


class TestValid(unittest.TestCase):
    def setUp(self):
        self.matrix = [
            [1,    2,  3],
            ['*',  0, '*'],
            [' ', '*', 1]
        ]

    def test_is_valid(self):
        assert is_valid(self.matrix, 0, 1) == True
        assert is_valid(self.matrix, 0, 2) == False
        assert is_valid(self.matrix, 2, 2) == False

    def test_is_around_valid(self):
        print 'test_is_around_valid'
        assert is_around_valid(self.matrix, 1, 0) == True
        assert is_around_valid(self.matrix, 0, 1) == False
        assert is_around_valid(self.matrix, 2, 1) == False


class TestSearch(unittest.TestCase):
    def setUp(self):
        self.matrix = [
            [1,    2,  1],
            ['*',  0, '*'],
            [' ', '*', 1]
        ]

    def test_is_valid(self):
        assert is_valid(self.matrix, 0, 1) == True
        assert is_valid(self.matrix, 2, 2) == False




if __name__ == '__main__':
    unittest.main()