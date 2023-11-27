class Node:
    def __init__(self, name):
        self.name = name
        self.edges = []

    def add_edge(self, edge):
        if self.edges.count(edge) == 0:
            self.edges.append(edge)


def adjacency_table():
    adjacency = []
    for i in range(n):
        adjacency.append([0] * n)

    for node in list_nodes:
        for edge in node.edges:
            adjacency[node.name][edge] = 1
    return adjacency


def a():
    adjacency = adjacency_table()
    print("Таблица смежности:")
    for i in adjacency:
        print(*i)

    print("Петли", end=" ")
    for i in range(n):
        if adjacency[i][i] == 1:
            return "имеются"
    return "не имеются"


def b():
    adjacency = adjacency_table()
    print("Таблица смежности:")
    for i in adjacency:
        print(*i)

    print("Вершина, не смежная с другими", end=" ")
    for row in adjacency:
        if row.count(1) == 0:
            return "имеется"
    return "не имеется"


def c():
    adjacency = adjacency_table()
    print("Таблица смежности:")
    for i in adjacency:
        print(*i)

    for i in range(len(adjacency)):
        print("Для %d вершины смежные вершины: " % (i), end=" ")
        for j in range(len(adjacency[i])):
            if i != j:
                print(j, end=" ")
        print()


def d():
    adjacency = adjacency_table()
    print("Таблица смежности:")
    for i in adjacency:
        print(*i)

    print("Вершина, смежная со всеми другими", end=" ")
    for row in adjacency:
        if row.count(0) == 0:
            return "имется"
    return "не имеется"


def e():
    adjacency = adjacency_table()
    print("Таблица смежности:")
    for i in adjacency:
        print(*i)

    for i in range(len(adjacency)):
        print("Степень вершины %d: %d" % (i, adjacency[i].count(1)), end=" ")
    print()


def f():
    adjacency = adjacency_table()
    print("Таблица смежности:")
    for i in adjacency:
        print(*i)
    print("Вершины со тепенью 1:", end=" ")
    c = 0
    for i in range(len(adjacency)):
        if adjacency[i].count(1) == 1:
            c += 1
            print(i, end=" ")
    if c == 0:
        print("нет", end=" ")
    print()


def g():
    adjacency = adjacency_table()
    print("Таблица смежности:")
    for i in adjacency:
        print(*i)
    max_degree = 0
    for i in range(len(adjacency)):
        if adjacency[i].count(1) > max_degree:
            max_degree = adjacency[i].count(1)
    print("Степень графа:", max_degree)


list_nodes = []

n = int(input("n = "))
while n > 10:
    print("n <= 10")
    n = int(input("n = "))
for i in range(n):
    list_nodes.append(Node(i))
for i in range(n):
    fist_edge, second_edge = map(int, input().split())
    list_nodes[fist_edge].add_edge(second_edge)
    list_nodes[second_edge].add_edge(fist_edge)

print("a)")
print(a(), end="\n\n")
print("б)")
print(b(), end="\n\n")
print("в)")
c()
print("\n")
print("г)")
print(d(), end="\n\n")
print("д)")
e()
print("\n")
print("e)")
f()
print("\n")
print("ж)")
g()
print("\n")
