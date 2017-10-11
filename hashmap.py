
class Hashmap(object):

    def __init__(self, length):
        self.table = [[] for i in range(0, length)]
        self.length = len(self.table)

    def hash_func(self, key):
        return hash(key) % self.length

    def get(self, key):
        for item in self.table[self.hash_func(key)]:
            if item[0] == key:
                return item[1]
        return "Key not found."

    def set(self, key, value):
        if self.get(key) != "Key not found." or not self.table[self.hash_func(key)]:
            self.table[self.hash_func(key)] = [(key, value)]
        else:
            self.table[self.hash_func(key)].append((key, value))

    def delete(self, key):
        if self.get(key) != "Key not found.":
            self.table[self.hash_func(key)].remove((key, self.get(key)))

    # Helper print functions

    def print_table(self):
        print self.table

    def print_all_items(self):
        for item in self.table:
            for key, value in item:
                print (key, value)

# Uncomment below to test by instantiating and populating

test_table = Hashmap(10)
test_table.set("color", "blue")
test_table.set("this5", "that5")
test_table.set("another thing", "its value")
test_table.set("metal", "aluminum")
test_table.set(5, 10)
test_table.set("number", "fifteen")
test_table.set("another thing", "different")
test_table.set("and how about", "this")


test_table.print_table()
