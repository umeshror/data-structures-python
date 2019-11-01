class BinaryMinHeap(object):
    """
    Parent should be smaller than child
    """

    def __init__(self):
        self.heap_list = [0]
        self.size = 0

    def heapify_bottom_top(self, ind):
        """
        find if parent element is greater than child
        if greater then swipe them
        :param ind: integer index of list
        """
        while ind // 2 != 0:  # while ind reaches to root

            if self.heap_list[ind // 2] > self.heap_list[ind]:
                temp = self.heap_list[ind // 2]
                self.heap_list[ind // 2] = self.heap_list[ind]
                self.heap_list[ind] = temp

            ind = ind // 2

    def insert(self, value):
        """
        insert value at the end of the list then heapify it from bottoms up
        :param value: value to be added
        """
        self.heap_list.append(value)
        self.size += 1
        self.heapify_bottom_top(self.size)

    def del_min(self):
        """
        Delete the minimum from heap
        """
        min_value = self.heap_list[1]
        # replace min_value with last item from heap_list
        self.heap_list[1] = self.heap_list[self.size]
        self.size -= 1
        self.heap_list.pop()
        # heapify top to bottom to find the correct min_value and right
        # position of root element
        self.heapify_top_bottom(1)
        return min_value

    def heapify_top_bottom(self, ind):
        """
        Heapify top to bottom to find the correct min_value and right
        position of root element
        :param ind: ind from the point top to bottom should start
        """
        while (ind * 2) <= self.size:  # till it reaches size of list

            min_child_ind = self.min_child_ind(ind)

            if self.heapList[ind] > self.heapList[min_child_ind]:
                # replace parent with child
                temp = self.heapList[ind]
                self.heapList[ind] = self.heapList[min_child_ind]
                self.heapList[min_child_ind] = temp
            ind = min_child_ind

    def min_child_ind(self, ind):
        """
        return minimum child of the parent
        :param ind: index of the parent
        :return: index of the minimum child
        """

        if (ind * 2) + 1 > self.size:  # till it reaches size of list
            return ind * 2
        else:
            if self.heap_list[ind * 2] < self.heap_list[ind * 2 + 1]:
                return ind * 2
            else:
                return ind * 2 + 1

    def build_heap(self, heap_list):
        ind = len(heap_list) // 2
        self.size = len(heap_list)
        self.heap_list = [0] + heap_list[:]
        while (ind > 0):
            self.heapify_top_bottom(ind)
            ind -= 1
