#!/usr/bin/env python3
""" Basic Dictionalry """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ No limit Caching system inherited from BaseCache """
    def put(self, key, item):
        """ Assign to dict """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Return linked value """
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
