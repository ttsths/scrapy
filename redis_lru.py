# -*- encoding: utf-8 -*-
'''
利用OrderDict实现LRU（最近最少使用淘汰算法）
但是LRU 算法需要消耗大量的额外内存进行swap
@File    :   redis_lru.py    
@Contact :   shentuhaisan@gmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/6/21 下午10:58   shentu      1.0         None
'''
from collections import OrderedDict
class LRUDict(OrderedDict):
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = OrderedDict

    def __setitem__(self, key, value):
        old_value = self.items.get(key)
        if old_value is not  None:
            self.items.pop(key)
            self.items[key] = value
        elif len(self.items) < self.capacity:
            self.items[key] = value
        else:
            self.items.popitem(last=True)
            self.items[key] = value

    def __getitem__(self, key):
        value = self.items.get(key)
        if value is not None:
            self.items.pop[key]
            self.items[key] = value
        return value

    def __repr__(self):
        return  repr(self.items)