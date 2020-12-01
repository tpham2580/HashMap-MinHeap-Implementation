# Course: CS261 - Data Structures
# Assignment: 5
# Student: Timothy Pham
# Description: MinHeap Implementation using Dynamic Array


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.heap.length() == 0

    def add(self, node: object) -> None:
        """
        adds a new object to the MinHeap maintaining heap property
        Runtime complexity of this implementation must be O(logN).
        """
        self.heap.append(node)
        # getting the length should be O(1) since we are using the __len__ built in
        current_index = self.heap.length() - 1
        current = self.heap.get_at_index(current_index)
        if (current_index - 1) // 2 < 0:
            parent_index = 0
        else:
            parent_index = (current_index - 1) // 2
        parent = self.heap.get_at_index(parent_index)
        while current < parent:
            self.heap.swap(current_index, parent_index)
            current_index = parent_index
            current = self.heap.get_at_index(current_index)
            if (current_index - 1) // 2 < 0:
                parent_index = 0
            else:
                parent_index = (current_index - 1) // 2
            parent = self.heap.get_at_index(parent_index)

    def get_min(self) -> object:
        """
        returns an object with a minimum key without removing it from
        the heap. If the heap is empty, the method raises a MinHeapException.
        Runtime complexity of this implementation is O(1).
        """
        if self.is_empty():
            raise MinHeapException
        return self.heap.get_at_index(0)

    def _heapify(self, array, index, loop=1):
        """helper function to recursively find the smallest value"""

        smallest = index

        # setting the children
        left = 2 * index + 1
        right = 2 * index + 2

        # when the left child is smaller than parent
        if left < array.length() and array[left] < array[smallest]:
            smallest = left

        # when the right child is smaller than parent
        if right < array.length() and array[right] < array[smallest]:
            smallest = right

        if smallest != index:
            array.swap(index, smallest)
            self._heapify(array, smallest, loop + 1)

    def remove_min(self) -> object:
        """
        This method returns an object with a minimum key and removes it from
        the heap. If the heap is empty, the method raises a MinHeapException.
        Runtime complexity of this implementation must be O(logN).
        """

        if self.is_empty():
            raise MinHeapException

        last_item_index = self.heap.length() - 1

        # swapping minimum with last item in DA
        self.heap.swap(0, last_item_index)

        # deleting last item and popping it
        min_item = self.heap.pop()

        # if empty after pop()
        if self.is_empty():
            return min_item
        current_index = 0

        # finding minimum value child
        self._heapify(self.heap, current_index)

        return min_item

    def build_heap(self, da: DynamicArray) -> None:
        """
        receives a dynamic array with objects in any order and builds a
        proper MinHeap from them. Current content of the MinHeap is lost.
        Runtime complexity of this implementation must be O(N).
        """
        new_heap = DynamicArray()
        for index in range(da.length()):
            new_heap.append(da[index])

        for index in range(new_heap.length() // 2 - 1, -1, -1):
            self._heapify(new_heap, index)

        self.heap = new_heap
        return


# BASIC TESTING
if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)

    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())

    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty():
        print(h, end=' ')
        print(h.remove_min())

    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)
    da.set_at_index(0, 500)
    print(da)
    print(h)
