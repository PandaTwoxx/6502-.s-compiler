import os
import time

def write():
    start = time.time()
    print('Starting to write rom')
    if not(os.path.exists('rom.bin')):
        print('Write failed: Unable to locate rom.bin')
        print(f'Failed in {time.time()-start}')
        return 0
    os.system('minipro -p AT28C256 -w -rom.bin')
    print(f'Write completed in {time.time()-start}')
    return 1

write()