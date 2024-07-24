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

            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_key = next(reversed(self.cache_data))
                self.cache_data.pop(last_key)
                print("DISCARD: {}".format(last_key))

            self.cache_data[key] = item

    def get(self, key):
        """
        Gets an Item from cache
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
