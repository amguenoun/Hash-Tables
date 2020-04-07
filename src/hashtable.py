# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        hash_key = 5381
        for char in key:
            hash_key = (( hash_key << 5) + hash_key) + ord(char)
        return hash_key


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index] is not None:
            # hash collision logic here
            current = self.storage[index]
            while current:
                if current.key == key:
                    current.value = value
                    break
                elif current.next is None:
                    current.next = LinkedPair(key, value)
                    break
                else:
                    current = current.next

        else:
            self.storage[index] = LinkedPair(key, value)



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index] is None: #Checks if empty
            print('Empty')
        else:
            current = self.storage[index] #captures head of linked list
            prev = None
            if current.key == key: # Remove first case
                if current.next is None: #Only item in list
                    self.storage[index] = None
                else: #Items afterwards
                    self.storage[index] = current.next
            else:
                while current:
                    if current.key == key: # Removes if corrent by moving prev's next to current's next
                        prev.next = current.next
                        break
                    else:
                        prev = current
                        current = current.next
                    



    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index] is None:
            return None
        else:
            current = self.storage[index]
            while current:
                if current.key == key:
                    return current.value
                current = current.next

            return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # self.capacity = self.capacity * 2
        # new_hash = [None] * self.capacity
        # for i in range(len(self.storage)):
        #     if self.storage[i] is not None:
        #         current = self.storage[i]
        #         while current:
        #             index = self._hash_mod(current.key)
        #             if new_hash[index] is not None:
        #                 new_current = new_hash[index]
        #                 while new_current:
        #                     if new_current.next is None:
        #                         new_current.next= LinkedPair(current.key, current.value)
        #                         break
        #                     else:
        #                         new_current = new_current.next
        #             else:
        #                 new_hash[index] = LinkedPair(current.key, current.value)
        #             current = current.next

        # self.storage = new_hash

        self.capacity = self.capacity * 2
        new_table = HashTable(self.capacity)
        for i in range(len(self.storage)):
            if self.storage[i] is not None:
                current = self.storage[i]
                while current:
                    new_table.insert(current.key, current.value)
                    current = current.next

        self.storage = new_table.storage



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
