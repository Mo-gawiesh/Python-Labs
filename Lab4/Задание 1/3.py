class Node:
    def __init__(self, name):
        self.name = name
        self.from_edges = []
        self.to_edges = []

    def add_from_edge(self, edge):
        if self.from_edges.count(edge) == 0:
            self.from_edges.append(edge)

    def add_to_edge(self, edge):
        if self.to_edges.count(edge) == 0:
            self.to_edges.append(edge)


def a():
    print("Номера вершин, имеющие и предшественников, и приемников:", end=" ")
    count = 0
    for node in list_nodes:
        if len(node.from_edges) > 0 and len(node.to_edges):
            count += 1
            print(node.name, end=" ")
    if count == 0:
        print("нет", end="")
    print()


def b():
    print("Список дуг графа:", end=" ")
    for edge in list_edges:
        print(f"{edge[0]}->{edge[1]}", end=" ")
    print()


def c():
    max_priem = 0
    list_max = [list_nodes[i].name]
    for node in list_nodes:
        if len(node.to_edges) > max_priem:
            max_priem = len(node.to_edges)
            list_max = [node.name]
        elif len(node.to_edges) == max_priem:
            list_max.append(node.name)
    print("Номер(-а) вершин(-ы), имеющая(-ие) наибольнее число преемников:", *list_max)


def d():
    list_reap_node = []
    for i in range(len(adjacency_table)):
        for j in range(len(adjacency_table[i])):
            if adjacency_table[i][j] == adjacency_table[j][i] == 1 and j != i:
                if list_reap_node.count(i) == 0:
                    list_reap_node.append(i)
                if list_reap_node.count(j) == 0:
                    list_reap_node.append(j)
    print("Число вершин, соединенные дугами в обоих направлениях:", len(list_reap_node))


list_nodes = []
list_edges = []
adjacency_table = []

n = int(input("n = "))
while n > 10:
    print("n <= 10")
    n = int(input("n = "))
for i in range(n):
    list_nodes.append(Node(i))
print("""Пример
0->1->2

0 1 0
0 0 1
0 0 0 """)
print('Введители матрицу смежности:')
for i in range(n):
    adjacency_table.append(list(map(int, input().split())))
for i in range(len(adjacency_table)):
    for j in range(len(adjacency_table)):
        if adjacency_table[i][j] == 1:
            list_edges.append([i, j])
            list_nodes[i].add_from_edge(list_nodes[j])
            list_nodes[j].add_to_edge(list_nodes[i])

print("a)")
a()

print("б)")
b()

print("в)")
c()

print("г)")
d()
