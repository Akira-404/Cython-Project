from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize

setup(
    cmdclass={'build_ext': build_ext},
    ext_modules=cythonize(
        Extension(
            'Rectangle',
            sources=['pyRectangle.pyx'],
            language='c++'
        ),
        compiler_directives={'language_level': '3'}
    )
)
