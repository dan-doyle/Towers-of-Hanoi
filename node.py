class Node:
    """
    A class to represent a Node.

    ...

    Attributes
    ----------
    value : int, float, str
        specific value held by node
    link_node : node
        node that this node links to

    Key Methods
    -------
    get_next_node():
        returns linked node

    set_next_node(link_node):
        links node to another node

    get_value():
        returns value held by node
    """
    def __init__(self, value, link_node=None):
        self.value = value
        self.link_node = link_node

    def set_next_node(self, link_node):
        self.link_node = link_node

    def get_next_node(self):
        return self.link_node

    def get_value(self):
        return self.value
