class Node:

    def __init__(self, left, right, value):
        self.left = left
        self.right = right
        self.value = value


class BinaryTree:

    def __init__(self, root=None):
        self.size = 0
        self.root = root

    def insert(self, node):
        print("*" * 20)
        if self.root is None:
            self.root = node
        else:
            self._insert(self.root, node)

    def _insert(self, curr_node, node):
        if curr_node.left is None or curr_node.right is None:
            if curr_node.value >= node.value:
                curr_node.left = node
                self.size += 1
                print("Current node value is ", curr_node.value, " so inserted ", node.value, " to left")
            else:
                self.size += 1
                curr_node.right = node
                print("Current node value is ", curr_node.value, " so inserted ", node.value, " to right")
        else:
            if curr_node.value > node.value:
                print(curr_node.value, "So needs to traverse left to insert ", node.value)
                self._insert(curr_node.left, node)
            elif curr_node.value < node.value:
                print(curr_node.value, "So needs to traverse right to insert ", node.value)
                self._insert(curr_node.right, node)
            else:
                print("Value already in the tree")

    def get_length(self):
        return self.size

    def print_tree_in_order(self):
        if self.get_length() <= 0:
            return "Empty Tree"
        else:
            self._print_tree_in_order(self.root)

    def _print_tree_in_order(self, curr_node):
        if curr_node is not None:
            self._print_tree_in_order(curr_node.left)
            print(curr_node.value)
            self._print_tree_in_order(curr_node.right)

    def print_tree_post_order(self):
        if self.get_length() <= 0:
            return "Empty Tress"
        else:
            self._print_tree_post_order(self.root)

    def _print_tree_post_order(self, curr_node):
        if curr_node is not None:
            self._print_tree_post_order(curr_node.left)
            self._print_tree_post_order(curr_node.right)
            print(curr_node.value)

    def print_tree_pre_order(self):
        if self.get_length() <= 0:
            return "Empty Tree"
        else:
            self._print_tree_pre_order(self.root)

    def _print_tree_pre_order(self, curr_node):
        if curr_node is not None:
            print(curr_node.value)
            self._print_tree_pre_order(curr_node.left)
            self._print_tree_pre_order(curr_node.right)


root_node = Node(None, None, 100)
node1 = Node(None, None, 150)
node2 = Node(None, None, 90)
node3 = Node(None, None, 80)
node4 = Node(None, None, 120)
node5 = Node(None, None, 190)
node6 = Node(None, None, 30)
binary_tree = BinaryTree(root_node)
binary_tree.insert(node1)
binary_tree.insert(node2)
binary_tree.insert(node3)
binary_tree.insert(node4)
binary_tree.insert(node5)
binary_tree.insert(node6)
print("== In Order ==")
binary_tree.print_tree_in_order()
print("== Post Order ==")
binary_tree.print_tree_post_order()
print("== Pre Order ==")
binary_tree.print_tree_pre_order()
