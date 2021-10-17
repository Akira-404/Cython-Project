from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

extension = Extension(
    name='pyx_primes',
    sources=['pyx_primes.pyx'],
    language='c'
)

setup(
    name='pyx_primes',
    ext_modules=cythonize(extension)
)
