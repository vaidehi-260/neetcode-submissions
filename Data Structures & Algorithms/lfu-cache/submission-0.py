from collections import defaultdict


class Node:

    def __init__(self, key, val):

        self.key = key
        self.val = val

        self.freq = 1

        self.prev = None
        self.next = None


class DLL:

    def __init__(self):

        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left

        self.size = 0

    def insert(self, node):

        prev = self.right.prev
        nxt = self.right

        prev.next = node
        nxt.prev = node

        node.prev = prev
        node.next = nxt

        self.size += 1

    def remove(self, node):

        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

        self.size -= 1

    def removeLRU(self):

        if self.size == 0:
            return None

        lru = self.left.next

        self.remove(lru)

        return lru


class LFUCache:

    def __init__(self, capacity):

        self.cap = capacity

        self.minFreq = 0

        self.keyToNode = {}

        self.freqToList = defaultdict(DLL)

    def update(self, node):

        freq = node.freq

        self.freqToList[freq].remove(node)

        if freq == self.minFreq and self.freqToList[freq].size == 0:

            self.minFreq += 1

        node.freq += 1

        self.freqToList[node.freq].insert(node)

    def get(self, key):

        if key not in self.keyToNode:
            return -1

        node = self.keyToNode[key]

        self.update(node)

        return node.val

    def put(self, key, value):

        if self.cap == 0:
            return

        if key in self.keyToNode:

            node = self.keyToNode[key]

            node.val = value

            self.update(node)

        else:

            if len(self.keyToNode) == self.cap:

                lru = self.freqToList[self.minFreq].removeLRU()

                del self.keyToNode[lru.key]

            node = Node(key, value)

            self.keyToNode[key] = node

            self.freqToList[1].insert(node)

            self.minFreq = 1