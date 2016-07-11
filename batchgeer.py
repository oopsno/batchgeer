#!/usr/bin/python
import math
import sys
import os
import imp


def process_generator(n):
    counter = 1
    digits = int(math.log10(n)) + 1
    tpl = '\033[032;1m[{{:3.0f}}%][{{:{0}d}}/{{:{0}d}}]\033[0m'.format(digits)
    while counter <= n:
        yield tpl.format(counter / n * 100, counter, n)
        counter += 1


def generator(fn):
    generated_main(fn)
    return fn


def geer(gen, items):
    n = len(items)
    pro = process_generator(n)
    for item in items:
        command = gen(item.strip())
        print('echo "{} processing: {}"\n{}'.format(next(pro), item, command))


def load_items(items):
    with open(items) as fd:
        return fd.readlines()


def generated_main(gen):
    if len(sys.argv) != 2:
        print('Usage: {} [list]'.format(sys.argv[0]))
        exit(-1)
    items = sys.argv[1]
    geer(gen, load_items(items))


def main():
    if len(sys.argv) != 3:
        print('Usage: batchgeer [conf.py] [list]')
        exit(-1)
    [conf, items] = sys.argv[1:]
    handler = imp.load_source(os.curdir, conf)
    gen = handler.gen
    geer(gen, load_items(items))

if __name__ == '__main__':
    main()



