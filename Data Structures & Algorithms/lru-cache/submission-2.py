class LRUCache:

    def __init__(self, capacity: int):
        self.cache = deque()
        self.dic = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.dic:
            if self.cache[-1] != key:
                self.cache.remove(key)
                self.cache.append(key)
            return self.dic[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic[key] = value
            if self.cache[-1] != key:
                self.cache.remove(key)
                self.cache.append(key)
        else:
            if len(self.cache) == self.capacity:
                del_key = self.cache.popleft()
                del self.dic[del_key]
            self.cache.append(key)
            self.dic[key] = value
