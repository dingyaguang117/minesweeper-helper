#coding=utf-8
__author__ = 'ding'
import time
from common import timer
from itertools import product
from screen import get_matrix, print_matrix, W, H
from mouse import flag


around = filter(lambda a: a!= (0, 0), product(xrange(-1, 2), xrange(-1, 2)))
useless = set()

def get_around_grids(col, row):
    ret = []
    for offset in around:
        _col, _row = col + offset[0], row + offset[1]
        if _col < 0 or _col >= W or _row < 0 or _row >= H:
            continue
        ret.append((_col, _row))
    return ret


def is_valid(matrix, col, row):
    '''
    judge if the num of col, row is valid
    '''
    num_mine, num_unkown = 0, 0
    num = matrix[col][row]
    for _col, _row in get_around_grids(col, row):
        if matrix[_col][_row] == '*':
            num_mine += 1
        elif matrix[_col][_row] == 0:
            num_unkown += 1
    if num_mine > num or num_mine + num_unkown < num:
        return False
    return True


def is_around_valid(matrix, col, row):
    for _col, _row in get_around_grids(col, row):
        if not 0 < matrix[_col][_row] < 9:
            continue
        if not is_valid(matrix, _col, _row):
            return False
    return True


def uncertain_grids(matrix, col, row):
    if (col, row) in useless:
        return []

    if not 0 < matrix[col][row] < 9:
        return []

    ret = []
    for _col, _row in get_around_grids(col, row):
        if matrix[_col][_row] == 0:
            ret.append((_col, _row))

    if not ret:
        useless.add((col, row))
    return ret


def search(matrix, grids, index, result):
    '''
        dfs all available combinations in given grids
    '''
    if index == len(grids):
        l = [1 if matrix[col][row] == '*' else 0 for col, row in grids]
        result.append(l)
        return

    col, row = grids[index]
    # if it is mine
    matrix[col][row] = '*'
    if is_around_valid(matrix, col, row):
        search(matrix, grids, index+1, result)
    matrix[col][row] = 0
    # if it is not mine
    matrix[col][row] = ' '
    if is_around_valid(matrix, col, row):
        search(matrix, grids, index+1, result)
    matrix[col][row] = 0


def calc(matrix):
    '''
     get all mines, safeties and unknow grid's probability
    '''
    t1 = time.time()
    mines, safeties = set(), set()
    probability = {}

    for col in xrange(W):
        for row in xrange(H):
            candidates = uncertain_grids(matrix, col, row)
            if not candidates:
                continue
            print 'search: ', col, row, candidates
            results = []
            search(matrix, candidates, 0, results)
            print results
            # enumerate results:
            # if some grid is mine (safety) in all result, we can affirm the grid is mine (safety)
            stat = reduce(lambda a, b: [x+y for x, y in zip(a,b)], results, [0]*len(candidates))
            for candidate, num in zip(candidates, stat):
                if num == 0:
                    safeties.add(candidate)
                elif num == len(results):
                    mines.add(candidate)
                elif candidate not in safeties and candidate not in mines:
                    p = num *1.0 / len(results)
                    if candidate in probability:
                        probability[candidate] = max(probability[candidate], p)
                    else:
                        probability[candidate] = p

    t2 = time.time()
    print 'calc cost %.2fs' % (t2-t1)
    return mines, safeties, probability

def main():
    matrix = None
    round  = 1

    # get focus
    flag(0, 0, False)
    time.sleep(0.2)
    flag(7, 7, False)
    time.sleep(0.5)

    while True:
        print '-------- round %d --------' % round
        matrix = get_matrix(matrix)
        print_matrix(matrix)
        mines, safeties, probability = calc(matrix)
        print 'mines:', mines
        print 'safe:', safeties

        if not mines and not safeties:
            if not probability:
                break
            print 'probability:', probability
            items = sorted(probability.items(), key=lambda a:a[1])
            position = items[0][0]
            flag(position[0], position[1], False)

        for position in mines:
            flag(position[0], position[1], True)
        for position in safeties:
            flag(position[0], position[1], False)

        round += 1
        if round == 20:
            break
        time.sleep(0.5)

if __name__ == '__main__':



    main()