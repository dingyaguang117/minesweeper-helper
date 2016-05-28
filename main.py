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
    matrix = None
    round  = 1

    while True:
        print '-------- round %d --------' % round
        t = time.time()
        matrix = get_matrix(matrix)
        print_matrix(matrix)
        time.sleep(3)
        mines, nomines = calc(matrix)
        print mines, nomines
        for position in mines:
            flag(position[0], position[1], False)
        for position in nomines:
            flag(position[0], position[1], False)

        round += 1

if __name__ == '__main__':
    main()