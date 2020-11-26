#beans -> 1.85
#Corn -> 2.38
# Rice -> 1.92

#pythons dictionary is a hashtable

# array - data structure used to store th data
# hash function - function to convert key into an array index
# collision handling



class HashTable:
    def __init__(self):
        self.MAX=100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self,key,val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self,key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self,key):
        h = self.get_hash(key)
        self.arr[h] = None


t = HashTable()

#print(t.get_hash('march 6'))
t['march 6'] = 130
t['march 7'] = 20
t['march 8'] = 20

del t['march 6']
print(t.arr)
#print(t['march 6'])
