from py_primes import primes
import pyx_primes
import time

t1=time.time()
py_ret=primes(1000)
t2=time.time()
# print(f'py_ret:{py_ret}')
print(f'py_ret time:{t2-t1}')


t1=time.time()
py_ret=pyx_primes.pyx_primes(1000)
t2=time.time()
# print(f'pyx_ret:{py_ret}')
print(f'pyx_ret time:{t2-t1}')