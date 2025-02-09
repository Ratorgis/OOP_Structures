def bypass(new_elem, addres, local_height):
    local_height += 1
    if new_elem.value > addres.value:
        if addres.right_descendant == None:
            addres.right_descendant = new_elem
            return local_height
        else:
            return bypass(new_elem, addres.right_descendant, local_height)
    elif new_elem.value < addres.value:
        if addres.left_descendant == None:
            addres.left_descendant = new_elem
            return local_height
        else:
            return bypass(new_elem, addres.left_descendant, local_height)

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

    def add(self, value):
        if self.size == 0:
            n1 = Node(value)
            self.root = n1 
            self.size += 1
        else:
            n1 = Node(value)
            self.lheight = 0
            self.lheight = bypass(n1, self.root, self.lheight)
            if self.lheight + 1 > self.height:
                self.height = self.lheight + 1
            self.size += 1
    def height(self):
        print(self.height + 1)


