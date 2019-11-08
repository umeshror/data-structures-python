"""
remainder method

e.g empty has table with m = 11
    h(item) = item % 11
1.  55 ==> 55%11 ==> 0
2.  54 ==> 54%11 ==> 10
3.  26 ==> 26%11 ==> 4
4.  31 ==> 31%26 ==> 9

load_factor =  number of items/ size_of_arr(table_size)
"""


class HashTable(object):
    """
    Hashtable using remainder method
    """

    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    def hash_method(self, key):
        """
        Remainder method is used as hash_method
        :param key: Key to convent in hash value
        :return: hash value
        """
        return key % self.size

    def rehash(self, old_hash_value):
        """
        Simple rehash function to to solve collision issue.
        :param old_hash_value: old hash value where value already exists
        :return:
        """
        return (old_hash_value + 1) % self.size

    def put(self, key, value):
        """
        Converts key in hashvalue
        Stores key and value in self.keys[hashvalue] and self.values[hashvalue]
        :param key: key
        :param value: value
        """
        hash_value = self.hash_method(key)
        # if hash_value doest not present in self.keys
        if self.keys[hash_value] == None:
            self.keys[hash_value] = key
            self.values[hash_value] = value
        # if hash_value present in self.keys, find next available slot
        else:
            next_hash_value = self.rehash(hash_value)

            while self.keys[next_hash_value] != None and \
                            self.keys[next_hash_value] != key:
                next_hash_value = self.rehash(next_hash_value)

            # Set new key, if NONE
            if self.keys[next_hash_value] == None:
                self.keys[next_hash_value] = key
                self.values[next_hash_value] = value

            # Otherwise replace old value
            else:
                self.values[next_hash_value] = value

    def get(self, key):
        """
        Return items for given key
        :param key: key to find value for
        :return: value for the key
        """
        # Set up variables for our search
        hash_value = self.hash_method(key)
        value = None
        stop = False
        found = False
        position = hash_value

        # Until we discern that its not empty or found (and haven't stopped yet)
        while self.keys[position] != None and not found and not stop:

            if self.keys[position] == key:
                found = True
                value = self.values[position]
            else:
                position = self.rehash(position)
                if position == hash_value:
                    stop = True
        return value

    # Special Methods for use with Python indexing
    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

h = HashTable(5)
h[1] = 'one'
h[2] = 'two'
h[3] = 'three'
print(h[1])
#'one'
h[1] = 'new_one'
print(h[1])
#'new_one'
print(h[4])
# None