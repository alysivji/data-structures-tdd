'''Basic datastructures implemented in Python'''
from collections import deque


class Stack:

    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def peek(self):
        return self.items[len(self.items) - 1]

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []


def reverse_string(my_string):
    stack = Stack()

    for letter in my_string:
        stack.push(letter)

    modified_string = ''
    while not stack.is_empty():
        modified_string += stack.pop()

    return modified_string


class Queue:

    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.appendleft(item)

    def dequeue(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
