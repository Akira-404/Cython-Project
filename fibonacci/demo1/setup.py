from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

extensions = [
    Extension(
        name='fib',
        sources=['fib.pyx'],
        language='c')
]

setup(name='fib',ext_modules=cythonize(extensions))
