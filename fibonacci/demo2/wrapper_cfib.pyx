cdef extern from "cfib.h":
    double cfib(int n)

def fib_with_c(n):
    return cfib(n)

