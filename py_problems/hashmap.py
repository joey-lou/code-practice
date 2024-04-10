# implement linear probing


class HashMap:
    def __init__(self, size: int = 32):
        self.keys = [None] * size
        self.values = [None] * size
        self.size = size
        self.filled_size = 0

    def __getitem__(self, key):
        idx = hash(key) % self.size
        while self.keys[idx] is not None:
            if self.keys[idx] == key:
                return self.values[idx]
            idx += 1
        raise KeyError(f"{key=} is not found!")

    def __setitem__(self, key, value):
        if self.filled_size == self.size:
            raise RuntimeError("Can not insert to hashmap anymore!")
        idx = hash(key) % self.size
        while self.keys[idx] is not None:
            if self.keys[idx] == key:
                self.values[idx] = value
                return
            idx += 1
        self.keys[idx] = key
        self.values[idx] = value
        self.filled_size += 1

    def __delitem__(self, key):
        idx = hash(key) % self.size
        while self.keys[idx] is not None:
            if self.keys[idx] == key:
                self.keys[idx] = None
                self.values[idx] = None
                self.filled_size -= 1
                return
            idx += 1
        raise KeyError(f"Can not delete {key=}, not found!")

    def __len__(self):
        return self.filled_size

    def __iter__(self):
        return iter(k for k in self.keys if k is not None)

    def __repr__(self):
        s = f"{self.__class__.__name__}" + "{"
        for key in self:
            s += f"{key}:{self[key]}, "
        s = s.rstrip(", ") + "}"
        return s


hash_map = HashMap(4)
hash_map["cat"] = 1
hash_map["dog"] = 2
print(hash_map, len(hash_map))

hash_map["dog"] = 5
print(hash_map, len(hash_map))
del hash_map["cat"]
print(hash_map, len(hash_map))
hash_map["bird"] = 3
hash_map["elephant"] = 2
print(hash_map, len(hash_map))
hash_map["kangroo"] = 9
