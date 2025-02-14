def bypass(addres):
    if (addres.left_descendant != None) and (addres.right_descendant != None):
        bypass(addres.left_descendant)
        print(addres.value)
        return bypass(addres.right_descendant)
    elif (addres.left_descendant == None) and (addres.right_descendant != None):
        print(addres.value)
        return bypass(addres.right_descendant)
    elif (addres.left_descendant != None) and (addres.right_descendant == None):
        bypass(addres.left_descendant)
        return print(addres.value)
    else:
        return print(addres.value)

def search(elem, addres):
    if addres.value > elem:
        if addres.left_descendant == None:
            print("NO")
        else:
            search(elem, addres.left_descendant)
    elif addres.value < elem:
        if addres.right_descendant == None:
            print("NO")
        else:
            search(elem, addres.right_descendant)
    else:
        if elem == addres.value:
            return print("YES")
        else:
            return print("NO")

def tree_visualization(addres, height):
    if (addres.left_descendant != None) and (addres.right_descendant != None):
        tree_visualization(addres.right_descendant, height + 1)
        print("." * height, addres.value)
        return tree_visualization(addres.left_descendant, height + 1)
    elif (addres.right_descendant == None) and (addres.left_descendant != None):
        print('.' * height, addres.value)
        return tree_visualization(addres.left_descendant, height + 1)
    elif (addres.left_descendant == None) and (addres.right_descendant != None):
        tree_visualization(addres.right_descendant, height + 1)
        return print('.' * height, addres.value)
    else:
        return print('.' * height, addres.value)

def accommodation(new_elem, addres, local_height):
    local_height += 1
    if new_elem.value > addres.value:
        if addres.right_descendant == None:
            addres.right_descendant = new_elem
            return local_height
        else:
            return accommodation(new_elem, addres.right_descendant, local_height)
    elif new_elem.value < addres.value:
        if addres.left_descendant == None:
            addres.left_descendant = new_elem
            return local_height
        else:
            return accommodation(new_elem, addres.left_descendant, local_height)

class Node():
    def __init__(self, value):
        self.value = value
        self.left_descendant = None
        self.right_descendant = None

class Tree():
    def __init__(self):
        self.root = None
        self.size = 0
        self.height = 0
        self.lheight = 0
        self.arr = []
    def add(self, value):
        if value == 0:
            return
        elif value in self.arr:
            return print("ALREADY")
        else:
            self.arr.append(value)
            if self.size == 0:
                n1 = Node(value)
                self.root = n1 
                self.size += 1
            else:
                n1 = Node(value)
                self.lheight = 0
                self.lheight = accommodation(n1, self.root, self.lheight)
                if self.lheight + 1 > self.height:
                    self.height = self.lheight + 1
                self.size += 1
            print("DONE")
    def height(self):
        return print(self.height + 1)
    def size(self):
        return print(self.size)
    def all_elem(self):
        return bypass(self.root)
    def find(self, elem):
        return search(elem, self.root)
    def tree_output(self):
        return tree_visualization(self.root, 0)

class Dot():
    def __init__(self, element) -> None:
        self.element = element
        self.next = None

class LinkedList():
    def __init__(self) -> None:
        self.head_addres = None
        self.len = 0
    def front(self):
        return self.head_addres.element
    def push_front(self, element): 
        e1 = Dot(element)
        e1.next = self.head_addres
        self.head_addres = e1
        self.len += 1
    def push_back(self, element): 
        if self.len == 0:
            self.push_front(element)
        else:
            cur = self.head_addres
            while cur.next != None:
                cur = cur.next
            cur.next = Dot(element)
        self.len += 1
    def pop_back(self): 
        if self.len == 1:
            self.head_addres = None
        elif self.len == 2:
            self.head_addres.next = None
        else:            
            cur = self.head_addres
            cur1 = cur.next
            while cur1.next != None:
                cur = cur.next
            cur.next = None
            self.len -= 1
    def pop_front(self): 
        if self.len > 0:
            cur = self.head_addres.next
            self.head_addres.next = None
            self.head_addres = cur
            self.len -= 1
        else:
            print('There are no elements in the list')
    def insert(self, pos, element): 
        e1 = Dot(element)
        if pos > self.len:
            print("Out of range value for list")
        else:
            cur = self.head_addres
            for i in range(pos-2):
                cur.next
            cur1 = cur.next
            cur.next = e1
            e1.next = cur1
        self.len += 1
    def erase(self, pos):
        if pos > self.len:
            print('Out of range value for list')
        else:
            cur = self.head_addres
            for i in range(pos-2):
                cur.next
            cur1 = cur.next
            cur2 = cur1.next
            cur1.next = None
            cur.next = cur2
        self.len -= 1
    def print_list(self):
        cur = self.head_addres
        print(cur.element)
        while cur.next != None:
            print(cur.element, end=' ')
            cur = cur.next
