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


class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class CustQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, key):
        newNode = Node(key)
        newNode.next = self.head
        if self.head is not None:
            self.head.prev = newNode
        self.head = newNode
        if self.tail is None:
            self.tail = newNode

        self.size += 1

    def pop(self, key=-1) -> int:
        if key == -1:
            if self.size > 0:
                rt_value = self.tail.value
                if self.size > 1:
                    tmp_node = self.tail.prev
                    self.tail = tmp_node
                    self.tail.next = None
                    self.size -= 1
                    return rt_value
                else:
                    self.head = None
                    self.tail = None
                    return rt_value
        else:
            tmp_node = self.head
            for i in range(self.size):
                if tmp_node.value == key:
                    prev_node = tmp_node.prev
                    next_node = tmp_node.next
                    if prev_node or next_node:
                        if prev_node and next_node:
                            prev_node.next = next_node
                            next_node.prev = prev_node
                        elif next_node is None:
                            prev_node.next = None
                            self.tail = prev_node
                        else:
                            next_node.prev = None
                            self.head = next_node
                    else:
                        self.head = None
                        self.tail = None

                    self.size -= 1
                    return key
                tmp_node = tmp_node.next

        return -1

    def __str__(self):
        node = self.head
        rt_str = ""
        for i in range(self.size):
            rt_str = rt_str + str(node.value) + " "
            node = node.next
        return rt_str


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.lRU_dict = {}
        self.lRU_queue = CustQueue()

    def get(self, key: int) -> int:
        if key in self.lRU_dict:
            self.lRU_queue.pop(key)
            self.lRU_queue.push(key)
            return self.lRU_dict[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.lRU_dict:
            if self.size < self.capacity:
                self.size += 1
            else:
                lru = self.lRU_queue.pop()
                print("lru:", lru)
                self.lRU_dict.pop(lru)

            self.lRU_dict[key] = value
            self.lRU_queue.push(key)
        else:
            self.lRU_dict[key] = value
            self.lRU_queue.pop(key)
            self.lRU_queue.push(key)

