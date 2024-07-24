#!/usr/bin/env python3
""" FIFOCache module """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache class """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        Adds an item to the cache.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            self.cache_data.pop(next(reversed(self.cache_data)))
            print("DISCARD: {}".format(next(reversed(self.cache_data))))

    def get(self, key):
        """
        Gets an Item from cache
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
