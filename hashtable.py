
class HashTable(object):

    def __init__(self, length):
        self.table = [[None] for i in range(0, length)]
        self.length = len(self.table)

    def hash_func(self, key):
        return hash(key) % self.length

    def search(self, key):
        for item in self.table[self.hash_func(key)]:
            if item == key:
                return True
        return False

    def insert(self, key):
        if self.search(key) is True:
            print "Key is already in hash table."
            return
        else:
            if self.table[self.hash_func(key)] == [None]:
                self.table[self.hash_func(key)] = [key]
            else:
                self.table[self.hash_func(key)].append(key)

    def delete(self, key):
        if self.table[self.hash_func(key)][0] == key:
            self.table[self.hash_func(key)][0] = None
        else:
            if self.search(key) is True:
                self.table[self.hash_func(key)].remove(key)

    # Helper print functions

    def print_table(self):
        print self.table

    def print_all_items(self):
        for item in self.table:
            for value in item:
                print value

# Uncomment below to test by instantiating and populating

test_table = HashTable(10)
test_table.insert("amber")
test_table.insert("this5")
test_table.insert("another thing")
test_table.insert("aluminum")
test_table.insert(5)
test_table.insert("fifteen")
test_table.insert("amber")

test_table.print_table()
