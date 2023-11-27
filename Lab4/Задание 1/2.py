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
    print("Вершины, которые имеют больше двух приемников: ", end="")
    c = 0
    for i in list_nodes:
        if len(i.to_edges) > 2:
            c += 1
            print(i.name, end=" ")
    if c == 0:
        print("нет", end="")
    print()


def b():
    print("Вершины, которые не имеют предшественников: ", end="")
    c = 0
    for i in list_nodes:
        if len(i.from_edges) == 0:
            c += 1
            print(i.name, end=" ")
    if c == 0:
        print("нет", end="")
    print()


def c():
    for i in list_nodes:
        print("Для вершины %d предшественники вершины"%(i.name), *i.from_edges)


def d():
    print("Вершины, которые имеют только одного приемника ", end="")
    c = 0
    for i in list_nodes:
        if len(i.to_edges) == 1:
            c += 1
    if c == 0:
        print("не имеются")
    else:
        print("имеются")


list_nodes = []

n = int(input("n = "))
while n > 10:
    print("n <= 10")
    n = int(input("n = "))
for i in range(n):
    list_nodes.append(Node(i))
print('Введите "стоп", если не хотите большое добавлять вершины')
while True:
    input_data = input().split()
    if len(input_data) == 1:
        break
    else:
        fist_edge, second_edge = int(input_data[0]), int(input_data[1])
        list_nodes[fist_edge].add_from_edge(second_edge)
        list_nodes[second_edge].add_to_edge(fist_edge)

print("a)")
a()

print("б)")
b()

print("в)")
c()

print("г)")
d()
