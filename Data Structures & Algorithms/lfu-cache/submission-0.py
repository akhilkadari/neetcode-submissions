'''
Approach: Brute Force
- store each keys value, access freq, last access timestamp
- maintain a counter that increases whenever a key is accessed or updated
- each entry represents:
    - key: [value, freq, last_used_time]
- when cacheis full we scan every entry and find key
    - lowest freq
    - oleest timestamp if freq are equal

Approach: Doubly linked list:
1. 
key_node:
    1 -> Node(key=1, value=100, freq=2)
    2 -> Node(key=2, value=200, freq=1)
    3 -> Node(key=3, value=300, freq=1)

frequency_to_linked_list hashmap:
    frequency 1:
        HEAD <-> key2 <-> key 3 <-> TAIL

Minimum Frequency:
    self.min_frequency = 1
'''

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        
        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = 0
    
    def add_to_end(self, node):
        previous_node = self.tail.prev
        previous_node.next = node
        node.prev = previous_node

        node.next = self.tail
        self.tail.prev = node

        self.size+=1

    def remove(self, node):
        previous_node = node.prev
        next_node = node.next

        previous_node.next = next_node
        next_node.prev = previous_node

        node.prev = None
        node.next = None

        self.size -= 1

    def remove_first(self):
        if self.size == 0:
            return None
        least_recent = self.head.next
        self.remove(least_recent)

        return least_recent


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_node = {}
        self.freq_to_list = {}
        self.min_freq = 0
    
    def _update_frequency(self, node):
        old_freq = node.freq
        old_list = self.freq_to_list[old_freq]

        old_list.remove(node)

        if old_freq == self.min_freq and old_list.size == 0:
            self.min_freq +=1 
        node.freq += 1

        if node.freq not in self.freq_to_list:
            self.freq_to_list[node.freq] = DoublyLinkedList()
        
        self.freq_to_list[node.freq].add_to_end(node)

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        node = self.key_to_node[key]
        self._update_frequency(node)
        return node.value        

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.value = value
            self._update_frequency(node)
            return
        if len(self.key_to_node) == self.capacity:
            min_list = self.freq_to_list[self.min_freq]
            node_to_remove = min_list.remove_first()
            del self.key_to_node[node_to_remove.key]
    
        new_node = Node(key, value)
        self.key_to_node[key] = new_node
        if 1 not in self.freq_to_list:
            self.freq_to_list[1] = DoublyLinkedList()
        self.freq_to_list[1].add_to_end(new_node)

        self.min_freq = 1
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)