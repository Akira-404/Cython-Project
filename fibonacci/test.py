from demo1 import fib
from demo2 import wrapper_cfib

print(f'fib:{fib}')

print(fib.fib(20))
print(fib.fib.__doc__)

print(wrapper_cfib.fib_with_c(20))
print(wrapper_cfib.fib_with_c.__doc__)
