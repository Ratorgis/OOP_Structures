from data_structure import Tree

Wood = Tree()
a = list(map(int, input().split()))
a.pop()

for i in a:
    Wood.add(i)
