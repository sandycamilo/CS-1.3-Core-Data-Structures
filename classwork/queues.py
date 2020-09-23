#CREATE a queue data structure
#front at index 0
#back at index n - 1
my_queue = []

#UPDATE, ADD
#enqueue
my_queue.append("A")

#DELETE
#dequeue
my_queue.pop(0)

#READ
#front 
print(my_queue[0])

# ___________________________________

class Queue: 
  def __init__(self):
    #create an empty queue
    #put the front at index 0 
    #back at index n - 1 
    self.my_queue = []

  # ADDS the item to the back of the Queue
  #if the back is at index n - 1
  def enqueue(self, item):
    self.my_queue.append(item)


  def dequeue(self):
    #remove item from the beg of the list 
    self.my_queue.pop(0)

#look at the item at the front of queue
  def front(self):
    return.self.my_queue[0]
