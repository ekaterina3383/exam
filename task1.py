class AVL:
    class Node:
        def __init__(self, val, l, r):
            self.val = val
            self.left = None
            self.right = None
            self.size = 0
            self.l = l
            self.r = r
    
    def __init__(self, head):
        self.head = self.Node(head, l, r)
    
    def insert(self, val):
        self.current = self.head
        while self.current.left or self.current.right:
            if val <= self.current.val:
                self.current.left.size += 1
                if self.current.left:
                    self.current = self.current.left
                else:
                    self.current.left = self.Node(val)
            else:
                self.current.right.size += 1
                if self.current.right:
                    self.current = self.current.right
                else:
                    self.current.right = self.Node(val)
       
    def count_in_range(self):
        current = self.head
        counter = 0
        self.DFS(counter, current)

    def DFS(self, counter):
        if self.current >= l and self.current <= r:
            counter += 1
        if self.current.left:
            self.DFS(counter, self.current.left)
        if self.current.right:
            self.DFS(counter, self.current.right)
        return counter