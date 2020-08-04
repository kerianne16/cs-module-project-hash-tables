class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.hashtable = [None] * capacity
        self.capacity = capacity
        self.itemsContained = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.hashtable)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return (self.itemsContained / self.get_num_slots())

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381

        for c in key:
            hash = (hash * 33 + ord(c))

        return (hash % self.capacity)

        # hash = 5381
        # byte_array = key.encode()
        # for byte in byte_array:
        #     hash = ((hash * 33) ^ byte) % 0x100000000

        # return hash % self.capacity

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity


# modify to handle collions


    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # if empty spot in hashtable array
        if (self.hashtable[self.djb2(key)] == None):
            self.hashtable[self.djb2(key)] = HashTableEntry(key, value)
            self.itemsContained += 1
        else:
            current = self.hashtable[self.djb2(key)]  # initialize current

            # loop until you find the node with .next value as None (the end of the linked list)
            while (current.next != None):
                # if at any point current.key == key you are searching for, then replace value accordingly
                if (current.key == key):
                    current.value = value
                    return
                current = current.next

            # if current.key == key you are searching for, then replace value accordingly
            # need this additional check here for replacing values, as the previous loop doesn't check at the tail node that could be the node needed to be replaced
            if (current.key == key):
                current.value = value
                return

            # set next of the end node to the value you want to add to the next in line in the linked list
            current.next = HashTableEntry(key, value)
            self.itemsContained += 1

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # if hashtable at that index is not empty
        if self.hashtable[self.djb2(key)]:

            # if only 1 item in the hashable at that index
            if self.hashtable[self.djb2(key)].next == None:
                self.hashtable[self.djb2(key)] = None
                return
            # if more than 1 item in the hashtable at that index
            else:
                current = self.hashtable[self.djb2(key)]  # initialize current
                prev = None

                # loop over entire linked list until found correct node
                while (current != None):
                    # if found node to delete
                    if (current.key == key):
                        # if prev is none (so we are at the head of the linked list)
                        if (prev == None):
                            # make new head of linked list the next node after the head
                            self.hashtable[self.djb2(key)] = current.next
                        else:
                            # link prev and current next node together to unnattach deleted node
                            prev.next = current.next
                        return

                    # reassign prev and current if item was not found
                    prev = current
                    current = current.next

        else:
            print('Key not found')

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
