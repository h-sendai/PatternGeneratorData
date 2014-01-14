#!/usr/bin/env python

import os
import sys
import time # for sleep
import struct

def byte_to_hl(x, n_bit):
    output = []
    for n_shift in range(0, n_bit):
        y = (x >> n_shift)
        y = (y & 0x01)
        if y == 0:
            output.append('L')
        else:
            output.append('H')
    output.reverse()
    print '%s # %d' % (''.join(output), x)

def main():
    l = range(0, 2**32, 2**15)
    l.append(2**32 - 1)

    for i in l:
        byte_to_hl(i, n_bit = 32)

if __name__ == '__main__':
    main()
