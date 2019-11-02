import collections


class Node(object):
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val


def level_order_print(tree):
    if not tree:
        return
    nodes = collections.deque([tree])
    current_count, next_count = 1, 0
    while len(nodes) != 0:
        current_node = nodes.popleft()
        current_count -= 1
        print(current_node.val,)
        if current_node.left:
            nodes.append(current_node.left)
            next_count += 1
        if current_node.right:
            nodes.append(current_node.right)
            next_count += 1
        if current_count == 0:
            # finished printing current level
            print '\n',
            current_count, next_count = next_count, current_count


root = Node(1)

root.left = Node(2)
root.right = Node(3)
level_order_print(root)
