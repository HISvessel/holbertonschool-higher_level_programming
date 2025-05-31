#!/usr/bin/python3
"""This module contains a modified class of a list,
which enables us to see the capacity to modify the behaviour
of the list methods, as well as other methods"""


class VerboseList(list):

    """this class VerboseList inherits from the list object,
    and this allows us to modify the hehavour and the messages
    that are performed from the following methods
    the append method, which prints that an item was added
    the extend, which shows us the items that were extended
    the remove method, which confirms that an item was deleted
    the pop method, which pops the method at index. If an
    index is not provided, we leave the function to perform its
    default setting, which is to remove the last element of the list"""

    def append(self, item):
        print(f"Added [{item}] to the list.")
        super().append(item)

    def extend(self, iterable):
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, item):
        if item in self:
            print(f"Removed [{item}] from the list.")
            super().remove(item)
        else:
            print(f"[{item}] does not exist on list")

    def pop(self, item=-1):
        if len(self) > 0:
            print(f"Popped [{self[item]}] from the list.")
            super().pop(item)
        else:
            print("No item to pop from list")
            return None
