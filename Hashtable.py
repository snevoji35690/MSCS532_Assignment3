import random

class HashTable:
    def __init__(self, size=101):
        self.size = size  # number of buckets
        self.table = [[] for _ in range(size)]
        self.p = 10**9 + 7  # large prime
        self.a = random.randint(1, self.p - 1)
        self.b = random.randint(0, self.p - 1)

    def _hash(self, key):
        # Convert key to an integer hash
        if isinstance(key, str):
            key = sum(ord(c) for c in key)
        elif not isinstance(key, int):
            key = hash(key)

        return ((self.a * key + self.b) % self.p) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        bucket = self.table[index]

        # Check if the key exists and update
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        # Insert new key-value pair
        bucket.append((key, value))

    def search(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
        return False

    def display(self):
        for i, bucket in enumerate(self.table):
            if bucket:
                print(f"Bucket {i}: {bucket}")

# -------------------------
# Example usage
# -------------------------
if __name__ == "__main__":
    ht = HashTable()

    ht.insert("apple", 10)
    ht.insert("banana", 20)
    ht.insert("orange", 30)

    print("Search 'banana':", ht.search("banana"))
    print("Search 'grape':", ht.search("grape"))

    ht.delete("banana")
    print("After deleting 'banana':", ht.search("banana"))

    ht.display()
