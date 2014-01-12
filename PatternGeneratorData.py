#!/usr/bin/env python

import os
import sys
import time # for sleep
import struct

#debug = True
#debug = False

class PatternGeneratorData:
    def __init__(self):
        self.debug = False
        self.ascii_data = []
        self.binary_data = []
        self.bit_len = 0

    def set_debug(self):
        self.debug = True

    def unset_debug(self):
        self.debug = False

    def accumurate_ascii_data(self, line):
        c = list(line)
        for i in c:
            if i != 'H' and i != 'L':
                raise ValueError, 'Invaild Char %s' % (i)
        self.ascii_data.append(line)
        self.bit_len += len(line)

#    def get_n_ascii_data(self):
#        return len(self.ascii_data)
    
    def get_bit_len_ascii_data(self):
        return self.bit_len

    def print_ascii_data(self):
        for i in range(0, len(self.ascii_data)):
            print i, self.ascii_data[i]

    def _convert_ascii_to_binary(self):
        del self.binary_data[:]
        for i in self.ascii_data:
            x = i.replace('L', '0').replace('H', '1')
            value = int(x, 2)
            if self.debug:
                print '%s %08X' % (i, value)
            b = struct.pack('>I', value)
            self.binary_data.append(b)

    def clear_ascii_data(self):
        del self.ascii_data[:]
        self.bit_len = 0

    def get_binary_to_send(self):
        self._convert_ascii_to_binary()
        rv = ''.join(self.binary_data)
        return rv

def main():
    pgd = PatternGeneratorData()

    print '---'
    try:
        pgd.accumurate_ascii_data('LLLL')
    except ValueError, e:
        sys.exit(e)
    try:
        pgd.accumurate_ascii_data('LLLH')
    except ValueError, e:
        sys.exit(e)
    pgd.accumurate_ascii_data('LLHL')
    pgd.accumurate_ascii_data('LLHH')
    print 'accumurated', pgd.get_bit_len_ascii_data(), 'bit data'
    pgd.print_ascii_data()
    packet_data = pgd.get_binary_to_send()
    print 'send', len(packet_data), 'bytes data'
    sys.stderr.write(packet_data)
    pgd.clear_ascii_data()

    print '---'
    pgd.accumurate_ascii_data('HLLL')
    pgd.accumurate_ascii_data('HLLH')
    pgd.accumurate_ascii_data('HLHL')
    pgd.accumurate_ascii_data('HLHH')
    print 'accumurated', pgd.get_bit_len_ascii_data(), 'bit data'
    pgd.print_ascii_data()
    packet_data = pgd.get_binary_to_send()
    print 'send', len(packet_data), 'bytes data'
    sys.stderr.write(packet_data)
    pgd.clear_ascii_data()


if __name__ == '__main__':
    main()
