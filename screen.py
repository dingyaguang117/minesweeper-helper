#coding=utf-8
__author__ = 'ding'
import os
import time

from collections import defaultdict
from itertools import product

from PIL import ImageGrab

SIZE = 30           # size of grid
W, H = 16, 16       # count of cols and rows

offset = None       # content offset of screen

COLORS = {
    (0,  0, 15): 1,
    (0,  7,  0): 2,
    (15, 0,  0): 3,
    (0,  0,  7): 4,
    (7,  0,  0): 5,
    (0,  7,  7): 6,
    (0,  0,  0): '*',    # mine
}


def find_offset():
    '''
    return top-left position of grid[0][0]
    '''
    global offset
    if offset is None:
        offset = os.popen('osascript position.scpt').read()
        offset = map(int, offset.split(','))
        offset = (offset[0] + 15, offset[1] + 97)    # (15, 97) is offset in window
        print offset
    return offset


def get_base_xy(col, row):
    '''
    return top-left position of grid[col][row]
    '''
    base_offset = find_offset()
    base_x = col * SIZE + base_offset[0]
    base_y = row * SIZE + base_offset[1]
    return base_x, base_y


def get_matrix():
    t1 = time.time()
    im = ImageGrab.grab()
    t2 = time.time()

    matrix = []
    for i in xrange(0, W):
        matrix.append([0] * H)

    for col, row in product(xrange(W), xrange(H)):
        # s = defaultdict(int)
        base_x, base_y = get_base_xy(col, row)

        for _x, _y in product(xrange(4, SIZE - 4), xrange(4, SIZE - 4)):
            color = im.getpixel((base_x + _x, base_y + _y))
            color = tuple(map(lambda a: a >> 4, color[:3]))

            # s[color] += 1
            if color in COLORS:
                matrix[col][row] = COLORS[color]
                # break

        if matrix[col][row] == 0 and im.getpixel((base_x, base_y))[0] < 200:
            matrix[col][row] = ' '
        # print '-----', col, row
        # for color in s:
        #     print color, s[color]
    t3 = time.time()
    print 'snapshot cost %.2fs, recognize cost %.2fs' % (t2 - t1, t3 - t2)
    return matrix


def print_matrix(matrix):
    for row in xrange(H):
        for col in xrange(W):
            print matrix[col][row],
        print ''



if __name__ == '__main__':
    print_matrix(get_matrix())