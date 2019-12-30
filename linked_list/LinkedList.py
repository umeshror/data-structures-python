class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return "{}, Node({})".format(str(self.val), str(self.next))


def generate_nodes(arr):
    """
    :param arr: List of values
    :return: Head of Linked List
    """
    if not arr:
        return arr
    node = Node(arr[0])
    head = node
    for item in arr[1:]:
        node.next = Node(item)
        node = node.next
    return head


def traverse_list(head):
    data = []
    while head:
        data.append(head.val)
        head = head.next
    return data
