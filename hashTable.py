class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.data = [None] * self.size
    
    def _hash(self, key):
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i]) * 1) % len(self.data);
        return hash
                
    def set(self, key, value):
        address = self._hash(key)
        if self.data[address] is None:
            self.data[address] = []
        self.data[address].append([key, value])

    def get(self, key):
        address = self._hash(key)
        currentBucket = self.data[address]
        if currentBucket:
            for i in range(len(currentBucket)):
                if currentBucket[i][0] == key:
                    return currentBucket[i][1]
        return None

myHashTable = HashTable(100)
myHashTable.set('082124606606', 'Rony Setyawan')
print(myHashTable.get('082124606606'))