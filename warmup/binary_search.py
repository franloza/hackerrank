class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def lca(root, v1, v2):
    parents_v1 = []
    findParents(root, v1, parents_v1)

    parents_v2 = []
    findParents(root, v2, parents_v2)

    lca = -1
    for pair in zip(parents_v1, parents_v2):
        if pair[0].info == pair[1].info:
            lca = pair[0]
        else:
            break
    return lca


def findParents(node, v, parents):
    if parents is None:
        parents = []
    parents.append(node)

    if node.info == v:
        return True

    if node.left is not None:
        found = findParents(node.left, v, parents)
        if found:
            return found
    if node.right is not None:
        found = findParents(node.right, v, parents)
        if found:
            return found
    parents.pop()
    return False


# Read from input
# tree = BinarySearchTree()
# t = int(input())
#
# arr = list(map(int, input().split()))
#
# for i in range(t):
#   tree.create(arr[i])
#
# v = list(map(int, input().split()))
#
# ans = lca(tree.root, v[0], v[1])
# print(ans.info)

# Toy case
tree = BinarySearchTree()
t = 8

arr = [8, 4, 9, 1, 2, 3, 6, 5]

for i in range(t):
  tree.create(arr[i])

v = [1, 2]

ans = lca(tree.root, v[0], v[1])
print(ans.info)