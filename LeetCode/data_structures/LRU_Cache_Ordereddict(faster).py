# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
#
# Implement the LRUCache class:
#
# LRUCache(int capacity) Initialize the LRU cache with positive size capacity. int get(int key) Return the value of
# the key if the key exists, otherwise return -1. void put(int key, int value) Update the value of the key if the key
# exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this
# operation, evict the least recently used key.
#
# The functions get and put must each run in O(1) average time complexity.
#
# Constraints:
#
#     1 <= capacity <= 3000
#     0 <= key <= 104
#     0 <= value <= 105
#     At most 2 * 105 calls will be made to get and put.


from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lRU_dict = OrderedDict()
        self.size = 0

    def get(self, key: int) -> int:
        if key in self.lRU_dict:
            self.lRU_dict.move_to_end(key)
            return self.lRU_dict[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.lRU_dict:
            if self.size == self.capacity:
                self.lRU_dict.popitem(last=False)
                self.lRU_dict[key] = value
            else:
                self.lRU_dict[key] = value
                self.size += 1
        else:
            self.lRU_dict[key] = value
            self.lRU_dict.move_to_end(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

def test_LRUCache():
    lRUCache = LRUCache(2)
    lRUCache.put(1, 1)
    lRUCache.put(2, 2)
    assert lRUCache.get(1) == 1
    lRUCache.put(3, 3)
    assert lRUCache.get(2) == -1
    lRUCache.put(4, 4)
    assert lRUCache.get(1) == -1
    assert lRUCache.get(3) == 3
    assert lRUCache.get(4) == 4