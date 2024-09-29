class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    def pop(self):
        if self.length == 0 :
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -=1
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
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    def get(self,index):
        if self.length <= index or index < 0:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    def set_value(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    def insert(self,index,value):
        if index < 0 or index>self.length:
            return False
        if index == self.length:
            return self.append(value)
        elif index == 0:
            return self.prepend(value)
        else:
            new_node = Node(value)
            temp = self.get(index-1)
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
            return True
    def remove(self,index):
        if index < 0 or index>=self.length:
            return None
        if index == self.length - 1:
            return self.pop()
        elif index == 0:
            return self.pop_first()
        else:
            pre = self.get(index-1)
            temp = pre.next
            pre.next = pre.next.next
            temp.next = None
            self.length -= 1
            return temp
    def reverse(self):
        if self.length == 1 or self.length == 0:
            return False
        temp = self.head
        before = None
        after = temp.next
        for _ in range(self.length):
            temp.next = before
            before = temp
            temp = after
            if after.next is not None:
                after = after.next
        temp = self.head
        self.head = self.tail
        self.tail = temp
    def find_middle_node(self):
        fast = self.head
        slow = self.head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        return slow
    def has_loop(self):
        slow = self.head
        fast = self.head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False
    def partition_list(self, x):
        for i in range(self.length-1):
            before = self.head
            after = self.head.next
            for _ in range(self.length-i-1):
                if before.value >= x and after.value < x :
                    temp = before.value
                    before.value = after.value
                    after.value = temp
                before = before.next
                after = after.next
    def remove_duplicates(self):
        temp = self.head
        values = set()
        while temp != None:
            values.add(temp.value)
            temp = temp.next
        self.head = None
        self.tail = None
        self.length = 0
        for value in values:
            if self.head is None:
                self.head = Node(value)
                self.length += 1
                continue
            self.append(value)
    def binary_to_decimal(self):
        postion = self.length - 1
        temp = self.head
        dec = 0
        for _ in range(self.length):
            if temp.value == 0:
                postion -=1
            elif temp.value == 1:
                dec += (2 ** postion)
                postion -= 1
            temp = temp.next
        return dec
    def reverse_between(self,m,n):
        if self.length == 0 or m == n:
            return None
        if m != 0:
            subhead = self.head
            for _ in range(m-1):
                subhead = subhead.next
            before = subhead.next
            subtail = before
            temp = before.next
            after = temp.next
        else:
            before = None
            temp = self.head
            after = temp.next
        for _ in range(n-m):
            temp.next = before
            before = temp
            temp = after
            if after != None:
                after = after.next
        if m != 0 :
            subtail.next = temp
            subhead.next = before
        else:
            temp.next = before
            self.head = temp
def find_kth_from_end(link,index):
    slow = link.head
    fast = link.head
    for _ in range(index):
        if fast == None:
            return None
        fast= fast.next
    while fast != None:
        fast = fast.next
        slow = slow.next
    return slow
