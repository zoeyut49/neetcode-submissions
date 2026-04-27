class TimeMap:

    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = []
        self.dic[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""
        array = self.dic[key]
        res = ""
        l, r = 0, len(array) - 1
        while l <= r:
            index = (l + r) // 2
            if array[index][0] <= timestamp:
                res = array[index][1]
                l = index + 1
            else:
                r = index - 1
        return res
