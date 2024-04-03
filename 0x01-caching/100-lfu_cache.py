#!/usr/bin/env python3
""" LFUCache class for LFU caching """

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache inherits from BaseCaching
    and implements a LFU (Least Frequently Used)
    caching strategy.
    """

    def __init__(self):
        """
        Initialize the cache with an empty dictionary,
        an empty frequency counter,
        and an empty usage order list.
        """
        super().__init__()
        self.frequency = {}  # Track frequency of access for each key
        self.usage_order = []  # Track usage order for ties

    def put(self, key, item):
        """
        Add an item to the cache,
        following the LFU and LRU eviction strategies.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            self._update_frequency(key)  # Update frequency and usage order

            # Enforce maximum items limit (LFU and LRU eviction)
            if len(self.cache_data) > self.MAX_ITEMS:
                discarded_key = self._evict_lfu_lru()
                print("DISCARD: {}".format(discarded_key))
                del self.cache_data[discarded_key]

    def get(self, key):
        """
        Get an item from the cache, updating its frequency and usage order.
        """
        if key is not None and key in self.cache_data:
            self._update_frequency(key)
            return self.cache_data[key]

        return None

    def _update_frequency(self, key):
        """
        Update the frequency and usage order of a key after access.
        """
        self.frequency[key] = self.frequency.get(key, 0) + 1
        self.usage_order.remove(key)  # Move to the back (LRU)
        self.usage_order.append(key)

    def _evict_lfu_lru(self):
        """
        Evict the least frequently used item, using LRU as a tiebreaker.
        """
        # Find items with the lowest frequency
        min_freq = min(self.frequency.values())
        candidates = [k for k, v in self.frequency.items() if v == min_freq]

        # Break ties using LRU (least recently used)
        return candidates[self.usage_order.index(candidates[0])]
