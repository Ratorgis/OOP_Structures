from data_structure import Tree

Wood = Tree()

a = list(map(int, input().split()))

for i in a:
    Wood.add(i)

Wood.all_elem()