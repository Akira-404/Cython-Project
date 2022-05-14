# 包含来自Rectangle.cpp的 C ++代码
cdef extern from "Rectangle.cpp" namespace "shapes":
    pass

cdef extern from "Rectangle.h" namespace "shapes":
    cdef cppclass Rectangle:
        # 构造函数声明为“except+”。如果C++代码或初始内存分配由于失败而引发异常，这将使Cython 安全地引发适当的Python 异常
        Rectangle() except +
        Rectangle(int, int, int, int) except +
        int x0, y0, x1, y1
        int getArea()
        void getSize(int * width, int * height)
        void move(int, int)
