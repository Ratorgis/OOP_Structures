from data_structure import Node, Tree

a = 5
b = 4

Wood = Tree()
Wood.add(a)
Wood.add(b) 

print(Wood, '\n', Wood.root.value,  '\n', Wood.root.left_descendant.value)