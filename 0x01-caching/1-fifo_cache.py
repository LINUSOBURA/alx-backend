#!/usr/bin/env python3
"""FIFO Caching"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO Caching Class"""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
         Adds an item to the cache.
         If the cache is full, the least recently used item is discarded.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            self.cache_data.pop(first_key)
            print("DISCARD: {}".format(first_key))

    def get(self, key):
        """
         Gets an item from Cache
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
