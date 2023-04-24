class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return None
        else:
            dequeued_node = self.front
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return dequeued_node.value

if __name__ == '__main__':
    q = Queue()
    q.enqueue("Java")
    q.enqueue("DotNet")
    q.enqueue("PHP")
    q.enqueue("HTML")
    print("popleft : ", q.dequeue())
    print("leftmost element : ", q.front.value)
    print("pop : ", q.dequeue())
    print("leftmost element : ", q.front.value)
