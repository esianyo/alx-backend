#!/usr/bin/env python3
""" FIFOCache class for FIFO caching """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache inherits from BaseCaching
    and implements a FIFO (First-In-First-Out)
    caching strategy.
    """

    def __init__(self):
        """
        Initialize the cache with an empty dictionary and an empty order list.
        """
        super().__init__()
        self.cache_order = []

    def put(self, key, item):
        """
        Add an item to the cache, following the FIFO strategy.

        Args:
            key (str): Key to identify the cached item.
            item (object): The item to be cached.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.cache_order.append(key)  # Add key to the order list (FIFO)

            # Enforce maximum items limit (FIFO eviction)
            if len(self.cache_order) > self.MAX_ITEMS:
                # Discard the oldest item (first in)
                discarded_key = self.cache_order.pop(0)
                del self.cache_data[discarded_key]
                print("DISCARD: {}".format(discarded_key))

    def get(self, key):
        """
        Get an item from the cache by its key.

        Args:
            key (str): Key to identify the cached item.

        Returns:
            object: The cached item if found, None otherwise.
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]

        return None
