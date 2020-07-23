#!/usr/bin/env python3
"""
Implementation of the NoDict assignment
"""

__author__ = 'Tim(helped by: PyDan x Tif)'


class Node:
    def __init__(self, key, value=None):
        """Initialize the class Node with key/value"""
        self.key = key
        self.hash = hash(self.key)
        self.value = value

    def __repr__(self):
        """Print a human-readable representation of Node class key/value contents"""
        return f'{self.__class__.__name__}({self.key}, {self.value})'

    def __eq__(self, other):
        """Node class object should be able to compare itself to other Node objects"""
        return self.key == other.key


class NoDict:
    def __init__(self, num_buckets=10):
        """Initialize NoDict with arbitrary default size of 10 internal 'buckets', but can be overridden for more or fewer buckets."""
        self.buckets = [[] for i in range(num_buckets)]
        self.num_buckets = num_buckets
        
    def __repr__(self):
        """Return string representation of the contents of the buckets"""
        return '\n'.join([f'{self.__class__.__name__}.{i}:{bucket}' for i, bucket in enumerate(self.buckets)])

    def add(self, key, value=None):
        """Accept a new key and value, and store it into the `NoDict` instance. However, this method should not allow duplicate keys"""
        new_node = Node(key, value)
        bucket = new_node.hash % self.num_buckets
        for b in self.buckets[bucket]:
            if b == new_node:
                self.buckets[bucket].remove(b) 
        self.buckets[bucket].append(new_node)

    def get(self, key):
        """If the key is found in the `NoDict` class, return its associated value. If the key is not found, raise a `KeyError` exception"""
        node_to_find = Node(key)
        bucket = node_to_find.hash % self.num_buckets
        for b in self.buckets[bucket]:
            if node_to_find == b:
                return b.value
        raise KeyError(f'{key} not found')

    def __getitem__(self, key):
        """Implement this magic "dunder" method within the `NoDict` class to enable square-bracket _reading_ behavior"""
        return self.get(key)

    def __setitem__(self, key, value):
        """Implement this magic "dunder" method within the `NoDict` class to enable square-bracket _assignment_ behavior"""
        self.add(key, value)

