#linked list

#"hello" -> "hey" -> "hi" ->None

class node:

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None


first_node = Node("hello")
print(first_node.next) 


next_node = Node("bye")
print(next_node.next)

third_node = Node("hi")
print(third_node.next)

#make next node first_node's next 
first_node.next = next_node
next_node.next = third_node 

head = first_node 
tail = third_node #(points to None)


#traverse 
#read or visit each node 
current = head 
while current != None:
  #visit the Node 
  print(current.data)
  # move on to the next node 
  current = current.next 


#crud = create, read, update/replace/append, remove/delete, etc. 

new_node = Node("hi")
#append this Node to the end of the linked list 

#set tail from None to new_node 
tail.next = new_node
tail = new_node


#delete  Node from the trail 
#reassining tail to head and prev tail to none 
current = head
while current != None:
  current = current.next 
  if current.next == tail: #we are at one before the tail 
    break
print(current.data)

current.next = None #removing the current tail
tail = current #resetting the tail 





class node: #component of linked list class

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

class LinkedList:
  def __init__(self, item_list=None) # if nothing is provided item list will be None, if something is provided then the list will be whatever is passed 
    pass


  #update
  def append(self, new_node):
    #the linked list is empty
    if self.tail is None:
      self.head = new_node 
      self.tail = new_node
    else: #the linked has nodes 
      self.tail.next = new_node
      self.tail = new_node

  #read all items in list
  def print_list(self):
    current = self.head 
    while current != None:
      print(current.data)
      current = current.next

  def delete_from_tail(self):
      current = self.head
      while != None:
        if current.next == self.tail:
          break
        current = current.next
        #have the node right before the tail  so i stop and break at that point 
      current.next = None #the tail is deleted by setting it to None
      self.tail = current # we set the tail to the current node after deleting 

#creating a linked list in two ways: 
#empty list 
  my_ll = LinkedList()
  my_ll.append(Node("hello"))
  my_ll.append(Node("ho"))
  my_ll.append(Node("io"))



  my_ll.delete_from_tail(Node("ho"))
  my_ll.delete_from_tail(Node("io"))

  # print(my_ll.head)
  # print(my_ll.tail)

 #dynamic array 
  # my_ll = LinkedList(["he", "hi", "ho"])



