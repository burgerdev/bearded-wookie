#!/usr/bin/python

import sys
import os
import traceback
from glob import glob

from generate import l2n, generate
from rename import rename

def cleanup(fn):
    '''
    clean up what rename() might have left, generate mp3s afterwards
    '''
    
    for f in glob("./*.mp3"):
        os.remove(f)
    generate(fn)
    
def verify(fn):
    '''
    verify the implementation of rename()
    Returns: True, if the implementation is as specified
             False, otherwise
    '''
    
    failed = False
    
    try:
        rename(fn)
    except:
        print("The function rename() raised an Exception:\n======")
        traceback.print_exc()
        print("======")
        return False
    
    with open(fn, 'r') as f: 
        for i,line in enumerate(f):
            lc = l2n(line)
            expectedname = "%02d_" % (i,) + lc
            if not os.path.exists(expectedname):
                print("  * the file '{}' does not exist in directory '{}'".format(expectedname, os.getcwd()))
                failed = True
            if os.path.exists(lc):
                print("  * the file '{}' still exists in directory '{}'".format(lc, os.getcwd()))
                failed = True
            
    return not failed
    

if __name__ == "__main__":
    
    if len(sys.argv)<2:
        print("Usage: {} <listing file>".format(sys.argv[0]))
        sys.exit(1)
    else:
        fn = sys.argv[1]
        
    success = verify(fn)
    if not success:
        print("Verification failed (see above)")
        cleanup(fn)
        sys.exit(2)
    else:
        print("Success!")
        sys.exit(0)


     
