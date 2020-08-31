class MyHashSet:

    def __init__(self):
        self.size = 10000
        self.tab = [None] * self.size

    def calculate_hash_value(self, key):
        return key % self.size

    def add(self, key: int) -> None:
        hash = self.calculate_hash_value(key)

        if self.tab[hash] is None:
            self.tab[hash] = [key]
        else:
            self.tab[hash].append(key)

    def remove(self, key: int) -> None:
        hash = self.calculate_hash_value(key)

        if self.tab[hash] != None:
            while key in self.tab[hash]:
                self.tab[hash].remove(key)

    def contains(self, key: int) -> bool:
        hash = self.calculate_hash_value(key)

        if self.tab[hash] is not None and key in self.tab[hash]:
            return True
        else:
            return False



if __name__ == "__main__":
    # Your MyHashSet object will be instantiated and called as such:
    obj = MyHashSet()
    key = 45
    obj.add(key)
    print(obj.contains(key))
    obj.remove(key)
    print(obj.contains(key))