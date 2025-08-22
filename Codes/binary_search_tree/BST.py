from Codes.binary_search_tree.Node import Node

class BinarySearchTree:
    def __init__(self):
        self.__root = None

    def insert(self, value: int) -> None:
        new_node = Node(value)

        if self.__root is None:
            self.__root = new_node
        else:
            current = self.__root
            while current:
                if value < current.get_value():
                    next_node = current.get_left_child()
                    if next_node is None:
                        current.set_left_child(new_node)
                        new_node.set_parent(current)
                else:
                    next_node = current.get_right_child()
                    if next_node is None:
                        current.set_right_child(new_node)
                        new_node.set_parent(current)

                current = next_node

    def in_order_traversal(self):
        self.__root.in_order_traversal()

if __name__ == '__main__':
    bst = BinarySearchTree()

    for i in range(10):
        x = int(input())
        bst.insert(x)

    bst.in_order_traversal()