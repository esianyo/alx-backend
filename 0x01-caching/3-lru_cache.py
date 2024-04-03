#!/usr/bin/env python3
""" LRUCache class for LRU caching """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache inherits from BaseCaching
    and implements a LRU (Least Recently Used)
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
        Add an item to the cache, following the LRU strategy.

        Args:
            key (str): Key to identify the cached item.
            item (object): The item to be cached.
        """
        if key is not None and item is not None:
            # Update the order list if the key exists (move it to the front)
            try:
                self.cache_order.remove(key)
            except ValueError:
                pass
            self.cache_order.append(key)  # Add key to the front (LRU)

            # Enforce maximum items limit (LRU eviction)
            if len(self.cache_order) > self.MAX_ITEMS:
                # Discard the least recently used item (at the end)
                discarded_key = self.cache_order.pop(0)
                del self.cache_data[discarded_key]
                print("DISCARD: {}".format(discarded_key))

            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item from the cache by its key, updating the order list (LRU).

        Args:
            key (str): Key to identify the cached item.

        Returns:
            object: The cached item if found, None otherwise.
        """
        if key is not None and key in self.cache_data:
            # Update the order list if the key exists (move it to the front)
            try:
                self.cache_order.remove(key)
                self.cache_order.append(key)
            except ValueError:
                pass
            return self.cache_data[key]

        return None
