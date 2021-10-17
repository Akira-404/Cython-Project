# 一系列基于Cython 的Demo实例

## Matrix Multiplication矩阵乘法运算

### 文件目录

```bash
matrix_multiplication
├── mm.c
├── mm.py
├── mm.pyx
├── pyx_mm.cp36-win_amd64.pyd(so)
├── setup.py
├── test.py
└── tree.txt
```

### 文件说明

1.`matrix_multiplication/mm.c`

编译生成的c文件

2.`matrix_multiplication/mm.py`

基于numpy实现的矩阵乘法

3.`matrix_multiplication/mm.pyx`

使用cython实现的矩阵乘法

4.`matrix_multiplication/setup.py`

编译文件

5.`matrix_multiplication/test.py`

测试文件

### 测试结果

```bash
py naive_dot time:5.25210976600647 sec
pyx naive_dot time:1.0249967575073242 sec
```



------

## Fibonacci 斐波那契数列计算

### 文件目录

```bash
fibonacci
├── demo1
│   ├── build
│   ├── fib.c
│   ├── fib.cp36-win_amd64.pyd(so)
│   ├── fib.pyx
│   └── setup.py
├── demo2
│   ├── build
│   ├── cfib.c
│   ├── cfib.h
│   ├── setup.py
│   ├── wrapper_cfib.c
│   ├── wrapper_cfib.cp36-win_amd64.pyd(so)
│   └── wrapper_cfib.pyx
├── test.py
└── tree.txt
```

### 文件说明

1.`fibonacci/demo1/fib.pyx`

​	pyx实现fibonacci数列计算

2.`fibonacci/demo1/setpu.py`

​	编译

3.`fibonacci/demo2/cfib.h cfib.c`

​	C语言实现的fibonacci计算

4.`fibonacci/demo2/wrapper_cfib.pyx`

​	pyx调用c语言function

5.`fibonacci/demo2/setpu.py`

​	编译

6.`fibonacci/test.py`

​	测试文件

------

## NMS非极大值抑制算法

------

## Primes 求解质数

