#!/usr/bin/env python3
""" BasicCache module """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache class """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        Adds an item to the cache.
        """
        if key is not None or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Gets an item from Cache"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
