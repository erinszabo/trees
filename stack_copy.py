"""
There has to be a way to import my stack file from my data structure folder
but ill figure out how some other day...
For now I made this copy. Also I think I should have been able to import Stack like this:
    from pythonds.basic import Stack
but it didn't work...
"""


class Stack:  # a stack of blocks
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):  # place a new block on the stack O(1)
        self.items.append(item)

    def pop(self):  # look at and remove the top block O(1), bottom block O(n)
        return self.items.pop()

    def peek(self):  # just look at the top block O(1), bottom block O(n)
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

