class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n1.next = n2
n2.next = n3

head = None
prev = None
current = n1
while current:
    next = current.next
    current.next = prev
    prev = current
    if not next:
        head = current
    current = next



print(head.value)
while head.next:
    head = head.next
    print(head.value)


