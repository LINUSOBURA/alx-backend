#!/usr/bin/env python3
""" BasicCache module """

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        Adds an item to the cache.
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

    def get(self, key):
        """ Gets an item from Cache"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
