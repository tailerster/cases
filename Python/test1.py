class Node:
    def __init__(self, data, link, next):
        self.data = data
        self.link = link
        self.next = next

    def find_next(self):
        for i in range(len(self.next)):
            if self.link[i] == self.data:
                return self.next[i]


def main(x):
    n6_3 = Node(8, [], [])
    n6_2 = Node(7, [], [])
    n6_1 = Node(6, [], [])
    n6 = Node(x[0], [2020, 1968, 2008], [n6_1, n6_2, n6_3])
    n5_3 = Node(5, [], [])
    n5_2 = Node(4, [], [])
    n5_1 = Node(3, [], [])
    n5 = Node(x[0], [2020, 1968, 2008], [n5_1, n5_2, n5_3])
    n4_3 = Node(2, [], [])
    n4_2 = Node(1, [], [])
    n4_1 = Node(0, [], [])
    n4 = Node(x[3], ['SHEN', 'P4', 'LASSO'], [n4_1, n4_2, n4_3])
    n1 = Node(x[2], [1987, 1977, 1976], [n4, n5, n6])
    n_1 = Node(9, [], [])
    n = Node(x[1], ['X10', 'SELF'], [n1, n_1])

    while n:
        res = n.data
        n = n.find_next()
    return res

print(main([2020, 'X10', 1976, 'P4']))
print(main([1968, 'SELF', 1976, 'SHEN']))
