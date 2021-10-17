from mm import py_naive_dot
import pyx_mm
import numpy as np
import time

if __name__ == '__main__':
    a = np.random.randn(100, 200).astype(np.float32)
    b = np.random.randn(200, 500).astype(np.float32)
    t1=time.time()
    ret = py_naive_dot(a, b)
    t2=time.time()
    # print(f'ret:{ret}')
    print(f'py naive_dot time:{t2-t1} sec')

    t1=time.time()
    ret = pyx_mm.pyx_naive_dot(a, b)
    t2=time.time()
    # print(f'ret:{ret}')
    print(f'pyx naive_dot time:{t2-t1} sec')

