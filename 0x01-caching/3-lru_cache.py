#!/usr/bin/env python3
""" LRU Caching """

from collections import OrderedDict

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache class
    """

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Adds an item in the cache
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            f_key, _ = self.cache_data.popitem(last=False)
            print("DISCARD: {}".format(f_key))

        self.cache_data[key] = item

    def get(self, key):
        """
        Gets an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
