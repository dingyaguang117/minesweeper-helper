#coding=utf-8
__author__ = 'ding'

print 'importing PyMouse Module...'
from pymouse import PyMouse
print 'done'
from screen import get_base_xy, SIZE

m = PyMouse()


def flag(col, row, is_mine):
    x, y = get_base_xy(col, row)
    x += SIZE / 2
    y += SIZE / 2
    button = 2 if is_mine else 1
    m.click(x, y, button)


if __name__ == '__main__':
    flag(0, 0, False)