from data_structure import Tree

Wood = Tree()

with open('./test.txt', 'r') as f:
    n = list(f.readlines())

for k in n:
    i = list(k.split())
    if i[0] == "ADD":
        Wood.add(int(i[1]))
    elif i[0] == "SEARCH":
        Wood.find(int(i[1]))
    elif i[0] == "PRINTTREE":
        Wood.printtree()
