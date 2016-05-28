#coding=utf-8
__author__ = 'ding'
import contextlib
import time

@contextlib.contextmanager
def timer(msg):
    start = time.time()
    yield
    end = time.time()
    print "%s: %.2fs" % (msg, end-start)