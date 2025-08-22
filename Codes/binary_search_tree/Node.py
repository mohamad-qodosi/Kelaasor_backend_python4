from __future__ import annotations

class Node:
    def __init__(self, value: int, parent: Node=None) -> None:
        self.__value = value
        self.__parent = parent
        self.__right_child = None
        self.__left_child = None

    def get_value(self) -> int:
        return self.__value

    def get_parent(self) -> Node:
        return self.__parent

    def get_left_child(self) -> Node:
        return self.__left_child

    def get_right_child(self) -> Node:
        return self.__right_child

    def set_value(self, new_value: int) -> None:
        assert isinstance(new_value, int)
        self.__value = new_value

    def set_parent(self, new_parent: Node) -> None:
        assert isinstance(new_parent, Node)
        self.__parent = new_parent

    def set_right_child(self, new_right_child: Node) -> None:
        assert isinstance(new_right_child, Node)
        self.__right_child = new_right_child

    def set_left_child(self, new_left_child: Node) -> None:
        assert isinstance(new_left_child, Node)
        self.__left_child = new_left_child

    def add_child(self, value):
        if value < self.__value:
            if self.__left_child is None:
                self.__left_child = Node(value=value, parent=self)
            self.__left_child.add_child(value)
        else:
            if self.__right_child is None:
                self.__right_child = Node(value, self)
            self.__right_child.add_child(value)

    def in_order_traversal(self, level=0):
        if self.__left_child:
            self.__left_child.in_order_traversal(level + 1)
        print('----' * level, self.__value)
        if self.__right_child:
            self.__right_child.in_order_traversal(level + 1)
