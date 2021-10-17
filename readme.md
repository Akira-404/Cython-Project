# 一系列基于Cython 的Demo实例

## Matrix Multiplication矩阵乘法运算

------

## Fibonacci 斐波那契数列计算

### 文件目录

```
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

