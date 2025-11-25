class BinHeap:
    class Node:
        def __init__(self, val, num):
            self.val = val
            self.num = num
            self.next = None
    
    def __init__(self, head):
        self.head = self.Node(head, 1)
        
    def insert(self, val):
        self.current = self.head
        num = 1
        while self.current.next:
            self.current = self.current.next
            num += 1
        self.current.next = self.Node(val, num)
        
    def insert_batch(self, list):
        self.current = self.head
        num = 1
        while self.current.next:
            self.current = self.current.next
            num += 1
        for i in list:
            self.current.next = self.Node(i, num)
            num += 1
            self.current = self.current.next
            
    def print_heap(self):
        self.current = self.head
        while self.current.next:
            print(self.current.val)
            self.current = self.current.next
    
heap = BinHeap(3)
heap.insert(4)
heap.print_heap()