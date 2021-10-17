import numpy
from distutils.core import setup, Extension
from Cython.Build import cythonize

extension=Extension(
    name='pyx_mm',
    sources=['mm.pyx'],  # code file
    language='c',  # default c
    include_dirs=[numpy.get_include()],  # gcc -I
    library_dirs=[],  # gcc -L
    libraries=[],  # gcc -l
    extra_compile_args=[],  # 额外编译参数
    extra_link_args=[]  # 额外链接参数
)
setup(name='pyx_mm',
      ext_modules=cythonize(extension))
