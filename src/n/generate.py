#!/usr/bin/python

import os
import sys

def merge(t):
    return "".join([chr(c) for c in t])
    
def l2n(obf):
    '''
    don't look to close, it will spoil your fun
    '''
    obf = getattr(obf, merge([115, 116, 114, 105, 112]))()
    obf = getattr(obf, merge([108, 111, 119, 101, 114]))()
    obf = getattr(obf, merge([114, 101, 112, 108, 97, 99, 101]))(chr(32), chr(95))
    return obf + merge((46, 109, 112, 51))

def generate(fn):
    '''
    generate the alphabetically ordered, non-indexed mp3s
    '''
    with open(fn, 'r') as f: 
        L = f.readlines()
        L.sort()
        for line in L:
            open(l2n(line), 'w').close()
     
if __name__ == "__main__":
    import sys
    if len(sys.argv)<2:
        print("Usage: {} <listing file>".format(sys.argv[0]))
        sys.exit(1)
    else:
        fn = sys.argv[1]
    
    generate(fn)
