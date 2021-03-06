
# want to remove a linked list node 
# iterate to find the node
# then reset pointers


class Node(object):
    """ Class in a linked list. """

    def __init__(self, data, next=None):
        self.data = data 
        self.next = next 

    def as_string(self):
        """ Represent data for this node and its successors as a string.

        >>> Node(3).as_string()
        '3'

        >>> Node(3, Node(2, Node(1))).as_string() 
        '321'

        """

        out = []
        n = self 

        while n:
            out.append(str(n.data))
            n = n.next 

        return "".join(out)

    def remove_node(node): # Node 2 --> 1, 3, 4 
        """ 
        Given a node in a linked list, remove it. 
        Does not return anything; just changes the list in place.

        """

        if not node.next:
            raise ValueError("Cannot remove tail node!")

        node.data = node.next.data 
        node.next = node.next.next 
