class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # Dummy nodes
        self.left = Node(0, 0)   # LRU side
        self.right = Node(0, 0)  # MRU side

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev = node.prev
        next_node = node.next

        prev.next = next_node
        next_node.prev = prev

    def insert(self, node):
        # Insert at the MRU side
        prev = self.right.prev
        next_node = self.right

        prev.next = node
        node.prev = prev
        node.next = next_node
        next_node.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Recently used -> move to MRU
        self.remove(node)
        self.insert(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Remove old node
            self.remove(self.cache[key])

        # Create new node and make it most recently used
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        # Remove LRU node if capacity exceeded
        if len(self.cache) > self.capacity:
            lru = self.left.next

            self.remove(lru)
            del self.cache[lru.key]

        #TIme and space is O(1) and O(capacity) respectively