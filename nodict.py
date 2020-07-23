#!/usr/bin/env python3
"""
Implementation of the NoDict assignment
"""

__author__ = 'Tim(helped by: PyDan x Tif)'


class Node:
    def __init__(self, key, value=None):
        """"""
        self.key = key
        self.hash = hash(self.key)
        self.value = value

    def __repr__(self):
        """"""
        return f'{self.__class__.__name__}({self.key}, {self.value})'

    def __eq__(self, other):
        """"""
        return self.key == other.key


class NoDict:
    def __init__(self, num_buckets=10):
        """"""
        self.buckets = [[] for i in range(num_buckets)]
        self.num_buckets = num_buckets
        
    def __repr__(self):
        """"""
        return '\n'.join([f'{self.__class__.__name__}.{i}:{bucket}' for i, bucket in enumerate(self.buckets)])

    def add(self, key, value=None):
        """"""
        new_node = Node(key, value)
        bucket = new_node.hash % self.num_buckets
        for b in self.buckets[bucket]:
            if b == new_node:
                self.buckets[bucket].remove(b) 
        self.buckets[bucket].append(new_node)

    def get(self, key):
        """"""
        node_to_find = Node(key)
        bucket = node_to_find.hash % self.num_buckets
        for b in self.buckets[bucket]:
            if node_to_find == b:
                return b.value
        raise KeyError(f'{key} not found')

    def __getitem__(self, key):
        """"""
        return self.get(key)

    def __setitem__(self, key, value):
        """"""
        self.add(key, value)

