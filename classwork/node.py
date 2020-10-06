class Node:

    def __init__(self, data):
        self.data = data

        #left and right will point to other nodes
        self.left = None
        self.right = None

    node1 = Node(9)
    node2 = Node(3)
    node3 = Node(10)

    #building the tree
    root = node1

    node1.left = node2
    node.right = node3


    #new node of value of 12 and make it child to node of value of 10 

    node4 = Node(12)
    node3.right = node4

    #search algorithm for binary search tree 
    def search(root, target):
        #base case, stops the recursion 
        #1. once we have looked through everything and didnt find it
        #2. we have found it!
        if node is None:
            return None
        #second base case= if the node's data is equal to the taget value
        if node.data == target:
            #return the node, because we found it
            return node 
        #recursive case, calls function within itself 
        #if the data is less than the target we go to the right(looking for something that is bigger)
        if node.data < target:
            return search(node.right, target)
        else: #go left (looking for a smaller element)
            reutnr search(node.left, target)

    #calling the function to search for 12 
    result = search(root, 12)


    #trying to find an open space - does not rearrange it 
    def insert(node, new_node):
        if new_node.data > node.data:
            #put new child on the right if there is space 
            if node.right is None:
                node.right = new_node
                return 
            #otherwise keep looking
            else:
                insert(node.right, new_node)
        if new_node.data < node.data:
            #put the new child on the left if there is space
            if node.left is None:
                node.left = new_node
                return
            #otherwise keep looking 
            else:
                insert(node.left, new_node)

    insert(root, Node(4))

    #write delete(node, target)

    #in order traversal
    def in_order_traversal(node):
        if node != None:
            #traverse
            in_order_traversal(node.left)
            print(node.data)
            in_order_traversal(node.right)
        # else:
        #     return None 
    in_order_traversal(root) 
    