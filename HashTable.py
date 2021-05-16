class HashTable() :
    def __init__(self) :
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key) :                     #Key-String
        h = 0
        for char in key :
            h += ord(char)
        return h % self.MAX                        #100-Size of the list

t = HashTable()
t.get_hash('march 6')                               #It will give Ans-> 9

