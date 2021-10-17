# 一系列关于Cython 运算的Demo实例

## 目录

## 矩阵乘法运算

## fibonacci 斐波那契数列计算

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

fibonacci/demo1/fibpyx:pyx实现fibonacci数列计算

fibonacci/demo1/setpu.py:编译

fibonacci/demo2/cfib.h cfib.c:C语言实现的fibonacci计算

fibonacci/demo2/wrapper_cfib.pyx:pyx调用c语言function

fibonacci/demo2/setpu.py:编译

fibonacci/test.py

## nms 非极大值抑制算法

## primes 求解质数

