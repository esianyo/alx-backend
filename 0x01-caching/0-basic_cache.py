#!/usr/bin/env python3
""" BasicCache class for simple caching """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache inherits from BaseCaching and provides a basic caching system
    using a dictionary for storage.
    """

    def __init__(self):
        """
        Initialize the cache with an empty dictionary.
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key (str): Key to identify the cached item.
            item (object): The item to be cached.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item from the cache by its key.

        Args:
            key (str): Key to identify the cached item.

        Returns:
            object: The cached item if found, None otherwise.
        """
        if key is not None:
            return self.cache_data.get(key)
