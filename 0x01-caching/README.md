## Caching Project Readme

**Introduction**

This project implements various caching strategies in Python, providing classes for basic caching, FIFO (First-In-First-Out), LIFO (Last-In-First-Out), LRU (Least Recently Used), and MRU (Most Recently Used) caching.

**Structure**

The project consists of the following files:

* `base_caching.py`: Defines a base class `BaseCaching` with common functionalities for all caching implementations.
* `0-basic_cache.py`: Implements the `BasicCache` class, a simple dictionary-based cache.
* `1-fifo_cache.py`: Implements the `FIFOCache` class, following the FIFO eviction policy.
* `2-lifo_cache.py`: Implements the `LIFOCache` class, following the LIFO eviction policy.
* `3-lru_cache.py`: Implements the `LRUCache` class, following the LRU eviction policy.
* `4-mru_cache.py`: Implements the `MRUCache` class, following the MRU eviction policy.

**Usage**

Each caching class can be used independently. Here's an example for `BasicCache`:

```python
from base_caching import BaseCaching

cache = BasicCache()
cache.put("key1", "value1")
print(cache.get("key1"))  # Output: value1
```

**Explanation of Caching Strategies**

* **Basic Caching:** Stores key-value pairs in a dictionary for simple retrieval.
* **FIFO (First-In-First-Out):** Evicts the oldest added item when the cache reaches its maximum capacity.
* **LIFO (Last-In-First-Out):** Evicts the most recently added item when the cache reaches its maximum capacity.
* **LRU (Least Recently Used):** Evicts the item that hasn't been accessed for the longest time when the cache reaches its maximum capacity.
* **MRU (Most Recently Used):** Evicts the most recently accessed item when the cache reaches its maximum capacity (opposite of LRU).

**Testing**

The project assumes the existence of separate `main.py` files that handle testing for each caching class. You'll need to implement the testing logic in these files.

**Additional Notes**

* All caching classes inherit from the `BaseCaching` class, which can be extended for further functionalities.
* The `MAX_ITEMS` constant defined in `base_caching.py` specifies the maximum capacity of the cache.
