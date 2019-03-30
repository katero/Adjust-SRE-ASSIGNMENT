# 1 在terminal 创建脚本:
$ vi shufflenumber.py


# 2 写代码：

#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

list = [1,2,3,4,5,6,7,8,9,10]
random.shuffle(list)

print(list)


# 3 运行脚本
$ python3 shufflenumber.py

