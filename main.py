from data_structure import Tree

Wood = Tree()
a = list(map(int, input().split()))
a.pop()

for i in a:
    Wood.add(i)

for n in Wood.all_elem():
    print(n)