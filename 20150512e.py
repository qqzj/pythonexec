#!/usr/bin/env python
# -*- coding: utf-8 -*-
import package.demo as demo
print demo.getPackageName()
print __name__

try:
    import cStringIO as StringIO
except importError:
    import StringIO
# private函数和变量“不应该”被直接引用，
# 而不是“不能”被直接引用，
# 是因为Python并没有一种方法可以完全限制访问private函数或变量，
# 但是，
# 从编程习惯上不应该引用private函数或变量
# 