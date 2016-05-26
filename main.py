#coding=utf-8
__author__ = 'ding'
import time

from screen import get_matrix, print_matrix, W, H
from mouse import flag

def calc(matrix):
    for col in xrange(W):
        for row in xrange(H):
            return [(col, row)], []


def main():
    while True:
        t = time.time()
        matrix = get_matrix()
        print_matrix(matrix)
        time.sleep(3)
        print 'time:', time.time() - t
        # print matrix
        print calc(matrix)
        mines, nomines = calc(matrix)
        print mines, nomines
        for position in mines:
            flag(position[0], position[1], False)
        for position in nomines:
            flag(position[0], position[1], False)

if __name__ == '__main__':
    main()