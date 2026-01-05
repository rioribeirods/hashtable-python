BLANK = object()

from typing import NamedTuple, Any, List

class Pair(NamedTuple):
    key: Any
    value: Any

class HashTable:
    def __init__(self, capacity=8):
        if capacity < 1:
            raise ValueError("Capacity must be a positive number")
        self._buckets: List[List[Pair]] = [[] for _ in range(capacity)]
        self._capacity = capacity
        self._load_factor_threshold = 0.7
        self._pairs = self._buckets
        self._slots = self._buckets

    def __len__(self):
        return self._capacity

    def __setitem__(self, key, value):
        index = self._index(key)
        bucket = self._buckets[index]

        for i, pair in enumerate(bucket):
            if pair.key == key:
                bucket[i] = Pair(key, value)
                return

        bucket.append(Pair(key, value))

        if self.load_factor > self._load_factor_threshold:
            self._resize()

    def __getitem__(self, key):
        index = self._index(key)
        bucket = self._buckets[index]

        for pair in bucket:
            if pair.key == key:
                return pair.value

        raise KeyError(key)

    def __contains__(self, key):
        try:
            self[key]
            return True
        except KeyError:
            return False

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __delitem__(self, key):
        index = self._index(key)
        bucket = self._buckets[index]

        for i, pair in enumerate(bucket):
            if pair.key == key:
                del bucket[i]
                return

        raise KeyError(key)

    def _index(self, key):
        return hash(key) % self._capacity

    def _resize(self):
        old_buckets = self._buckets
        self._capacity *= 2
        self._buckets = [[] for _ in range(self._capacity)]

        for bucket in old_buckets:
            for pair in bucket:
                index = self._index(pair.key)
                self._buckets[index].append(pair)

    @property
    def load_factor(self):
        return self.size / self._capacity if self._capacity > 0 else 0

    @property
    def size(self):
        return sum(len(bucket) for bucket in self._buckets)

    @property
    def pairs(self):
        all_pairs = []
        for bucket in self._buckets:
            for pair in bucket:
                all_pairs.append((pair.key, pair.value))
        return set(all_pairs)

    @property
    def keys(self):
        return {pair.key for bucket in self._buckets for pair in bucket}

    @property
    def values(self):
        return [pair.value for bucket in self._buckets for pair in bucket]

    @property
    def capacity(self):
        return self._capacity

    def __iter__(self):
        yield from self.keys

    def __str__(self):
        pairs = []
        for key, value in self.pairs:
            pairs.append(f"{key!r}: {value!r}")
        return "{" + ", ".join(pairs) + "}"

    @classmethod
    def from_dict(cls, dictionary, capacity=None):
        hash_table = cls(capacity or len(dictionary) * 10)
        for key, value in dictionary.items():
            hash_table[key] = value
        return hash_table

    def __repr__(self):
        cls = self.__class__.__name__
        return f"{cls}.from_dict({str(self)})"

    def __eq__(self, other):
        if self is other:
            return True
        if type(self) is not type(other):
            return False
        return self.pairs == other.pairs

    def copy(self):
        return HashTable.from_dict(dict(self.pairs), self.capacity)

    @staticmethod
    def have_same_elements(list1, list2):
        return sorted(list1) == sorted(list2)

    def clear(self):
        self._buckets = [[] for _ in range(self._capacity)]

    def pop(self, key, default=None):
        try:
            value = self[key]
            del self[key]
            return value
        except KeyError:
            if default is not None:
                return default
            raise

    def popitem(self):
        if self.size == 0:
            raise KeyError("popitem(): hash table is empty")
        
        for bucket in self._buckets:
            if bucket:
                pair = bucket.pop()
                return (pair.key, pair.value)
            
    def update(self, other=None, **kwargs):
        if other is not None:
            if hasattr(other, 'items'):
                for key, value in other.items():
                    self[key] = value
            else:
                for key, value in other:
                    self[key] = value
        
        for key, value in kwargs.items():
            self[key] = value

    def setdefault(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            self[key] = default
            return default