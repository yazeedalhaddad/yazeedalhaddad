class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self,value):
        new_node= Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        self.length -= 1
        temp.prev = None
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -=1
        return temp
    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        if index < self.length//2+1:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp
        else:
            temp = self.tail
            for _ in range(self.length - index - 1):
                temp = temp.prev
            return temp
    def set_value(self,index,value):
        temp = get(index)
        if temp is None:
            return False
        temp.value = value
        return True
    def insert(self,index,value):
        if index == 0:
            self.prepend(value)
            return True
        if index == self.length or self.length == 0:
            self.append(value)
            return True
        else:
            new_node = Node(value)
            before = self.get(index-1)
            if before is not None:
                temp = before.next
                before.next = new_node
                new_node.prev = before
                temp.prev = new_node
                new_node.next = temp
                self.length +=1
                return True
            return False
    def remove(self,index):
        if index >= self.length or index < 0:
            return None
        if index == 0:
            temp = self.pop_first()
            return temp
        if index == self.length - 1:
            temp = self.pop()
            return temp
        else:
            before = self.get(index - 1)
            temp = before.next
            before.next = temp.next
            temp.next.prev = before
            temp.next = None
            temp.prev = None
            self.length -= 1
            return temp
    def swap_first_last(self):
        if self.length == 0 or self.length == 1:
            return None
        first = self.head.value
        self.head.value = self.tail.value
        self.tail.value = first
        return True
    def reverse(self):
        if self.length == 0 or self.length == 1:
            return None
        temp = self.tail
        for _ in range(self.length):
            post = temp.prev
            temp.prev = temp.next
            temp.next = post
            temp = temp.next
        temp = self.head
        self.head = self.tail
        self.tail = temp
        return True
    def is_palindrome(self):
        if self.length == 0 or self.length == 1:
            return True
        back = self.tail
        front = self.head
        for _ in range(self.length//2):
            if back.value != front.value:
                return False
            back = back.prev
            front = front.next
        return True
    def swap_pairs(self):
        if self.length == 0 or self.length == 1:
            return None
        temp = self.head
        for _ in range(self.length//2):
            temp2 = temp.value
            temp.value = temp.next.value
            temp.next.value = temp2
            temp = temp.next.next
        return True
