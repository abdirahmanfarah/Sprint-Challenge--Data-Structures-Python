from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # check if storage is at capacity
        if self.storage.length == self.capacity:
            # replace value of head
            self.current = self.storage.head
            self.storage.remove_from_head()
            self.storage.add_to_head(item)
            # current is now next value of head
            self.current = self.current.next
            self.storage.head = self.current

        # if storage is not at capacity
        elif self.storage.length < self.capacity:
            # add to tail
            self.storage.add_to_tail(item)
            # current is now at head
            self.current = self.storage.head



    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        node = self.storage.head
        # get the items in the list in the order they were put in there
        while node != None:
            list_buffer_contents.append(node.value)
            node = node.next
        # if there are no items, return an empty array


        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
