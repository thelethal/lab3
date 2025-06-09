#
# Author: Muhammad Nazmul Hossain
# Student Number:105085229
#
# Place the code for your lab 3 here.  Read the specs carefully.  
#
# To test, run the following command :
#     python test_lab3.py
#

class DoublyLinked:
    class Node:
        def __init__(self, data=None, next_node=None, prev_node=None):
            self.data = data
            self.next = next_node
            self.prev = prev_node

        def get_data(self):
            return self.data

        def get_next(self):
            return self.next

        def get_previous(self):
            return self.prev

    def __init__(self):
        self.head = None
        self.tail = None

    def get_front(self):
        return self.head

    def get_back(self):
        return self.tail

    def push_front(self, data):
        new_node = self.Node(data, self.head, None)
        if self.head is not None:
            self.head.prev = new_node
        else:
            # List was empty, so tail is also the new node
            self.tail = new_node
        self.head = new_node

    def push_back(self, data):
        new_node = self.Node(data, None, self.tail)
        if self.tail is not None:
            self.tail.next = new_node
        else:
            # List was empty, so head is also the new node
            self.head = new_node
        self.tail = new_node

    def pop_front(self):
        if self.head is None:
            raise IndexError('pop_front() used on empty list')
        data = self.head.data
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        else:
            # List became empty, so tail must be None too
            self.tail = None
        return data

    def pop_back(self):
        if self.tail is None:
            raise IndexError('pop_back() used on empty list')
        data = self.tail.data
        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None
        else:
            # List became empty, so head must be None too
            self.head = None
        return data


class Sentinel:
    class Node:
        def __init__(self, data=None, next_node=None, prev_node=None):
            self.data = data
            self.next = next_node
            self.prev = prev_node

        def get_data(self):
            return self.data

        def get_next(self):
            return self.next

        def get_previous(self):
            return self.prev

    def __init__(self):
        self.sentinel = self.Node()
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

    def get_front(self):
        return self.sentinel.next if self.sentinel.next != self.sentinel else None

    def get_back(self):
        return self.sentinel.prev if self.sentinel.prev != self.sentinel else None

    def push_front(self, data):
        new_node = self.Node(data, self.sentinel.next, self.sentinel)
        self.sentinel.next.prev = new_node
        self.sentinel.next = new_node

    def push_back(self, data):
        new_node = self.Node(data, self.sentinel, self.sentinel.prev)
        self.sentinel.prev.next = new_node
        self.sentinel.prev = new_node

    def pop_front(self):
        if self.sentinel.next == self.sentinel:
            raise IndexError('pop_front() used on empty list')
        data = self.sentinel.next.data
        self.sentinel.next = self.sentinel.next.next
        self.sentinel.next.prev = self.sentinel
        return data

    def pop_back(self):
        if self.sentinel.prev == self.sentinel:
            raise IndexError('pop_back() used on empty list')
        data = self.sentinel.prev.data
        self.sentinel.prev = self.sentinel.prev.prev
        self.sentinel.prev.next = self.sentinel
        return data
