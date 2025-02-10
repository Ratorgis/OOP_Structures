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
    def printtree(self):
        return tree_visualization(self.root, 0)

