__author__ = 'spark'


import Queue


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def lot(head):
    q = Queue.Queue()
    q.put(head)
    current_level = 1
    next_level = 0
    line = ''
    while not q.empty():
        node = q.get()
        line = line + ' ' + str(node.value)
        current_level -= 1
        if node.left:
            q.put(node.left)
            next_level += 1
        if node.right:
            q.put(node.right)
            next_level += 1
        if current_level == 0:
            current_level = next_level
            next_level = 0
            print line
            line = ''



if __name__ == '__main__':
    n3 = Node(3)
    n7 = Node(7)
    n15 = Node(15)
    n20 = Node(20)
    n9 = Node(9)
    n1 = Node(1)
    n9.left = n15
    n9.right = n20
    n7.left = n1
    n3.left = n7
    n3.right = n9
    lot(n3)


#   3
#  7 9
# 1  15 20