# -*- coding: utf-8 -*-
"""
Python3中有两种字符序列类型:bytes和str。
    bytes:实例包含原始的8位值
    str:包含Unicode字符
Python2也有两种表示字符序列的类型，分别叫做str和unicode
    与Python3不同
    str:包含原始的8位值
    unicode：实例包含Unicode字符
把Unicode字符表示为二进制数据有许多方法，最常见的就是将数据编码为utf-8.
使用 encode 和 decode
"""
"""
在Python中使用原始8位值与Unicode字符时，有两个问题要注意:
第一个问题: 可能会出现在Python2中
    如果str只包含7位ASCII字符，那么unicode和str实例几乎就成了同一种类型
    而在Python3中，str与bytes实例是绝不会等价的，即使是空字符串也不行
第二个问题: 可能会出现在Python3中
    如果通过内置的open函数获取了文件句柄，该句柄会默认采用utf-8编码格式来操作文件
    而在python2中，文件操作的默认编码是二进制格式
"""


# 在Python3中，需要编写接受str或bytes，并总是返回str的方法:
def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode("utf-8")
    else:
        value = bytes_or_str
    return value


# 在Python3中，另外还需要编写接受str或bytes，并总是返回bytes的方法:
def to_butes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode("utf-8")
    else:
        value = bytes_or_str
    return value


# 在Python2中，需要编写接受str和unicode，并总是返回Unicode的方法:
""" Python2中运行
def to_unicode(unicode_or_str):
    if isinstance(unicode_or_str, str):
        value = unicode_or_str.decode("utf-8")
    else:
        value = unicode_or_str
    return value


def to_str(unicode_or_str):
    if isinstance(unicode_or_str, unicode):
        value = unicode_or_str.encode("utf-8")
    else:
        value = unicode_or_str
    return value
"""
