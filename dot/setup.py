from distutils.core import setup,Extension
from Cython.Build import cythonize

import numpy

setup(
        ext_modules=cythonize(Extension(
            'dot_cython',#动态链接库名字
            sources=['dot_cython.pyx'],#code file
            language='c',#default c
            include_dirs=[numpy.get_include()],#gcc -I
            library_dirs=[],#gcc -L
            libraries=[],#gcc -l
            extra_compile_args=[],#额外编译参数
            extra_link_args=[]#额外链接参数
            )
        )
    )


