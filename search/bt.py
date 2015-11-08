import Queue


class Node:
    def __init__(self, name=None):
        self.name = name
        self.right = None
        self.left = None


def inorder_traverse(node):
    if node.left:
        inorder_traverse(node.left)
    print node.name
    if node.right:
        inorder_traverse(node.right)


def bfs(node):
    if node:
        queue = Queue.Queue()
        queue.put(node)
        while not queue.empty():
            n = queue.get()
            if n.left:
                queue.put(n.left)
            print n.name
            if n.right:
                queue.put(n.right)


if __name__ == '__main__':
    A = Node('a')
    B = Node('b')
    C = Node('c')
    D = Node('d')
    E = Node('e')
    F = Node('f')
    G = Node('g')
    A.left = B
    A.right = C
    B.left = D
    B.right = E
    C.left = G
    C.left = F
    C.right = G

    print('Breath First Search')
    bfs(A)

    print('\nIn-order Search')
    inorder_traverse(A)
