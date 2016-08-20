

class Node(object):

    def __init__(self, data, next=None):
        self.data = data 
        self.next = next 

    def as_string(self):

        out = []
        n = self 

        while n: # while there are nodes
            out.append(str(n.data)) # append node data to list out 
            n = n.next # n becomes the next node in a linked list 

        return "".join(out) # return the string-ified nodes 

        # >>> Node(3, Node (2, Node (1))).as_string()
        # '321'

    def remove_node(node):

        if not node.next: # ensures not the tail node
            raise ValueError("No node.next!") # raises value error 

        node.data = node.data.next # move data 
        node.next = node.next.next # move pointer

    def reverse_list(head):
        """ 
        Given a head node, return head node of new, reversed linked list. 

        >>> LinkList = Node(1, Node(2, Node(3)))
        >>> reverse_list(LinkList).as_string() # return the reversed list as a string

        '321'

        """

        out_head = None
        n = head 

        while n:
            out_head = Node(n.data, out_head)
            n = n.next

        return out_head            





