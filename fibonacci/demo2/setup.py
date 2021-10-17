from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

extensions = [
    Extension(
        name='wrapper_cfib',
        sources=['wrapper_cfib.pyx', 'cfib.c']
    )
]

setup(name='wrapper_cfib',ext_modules=cythonize(extensions))
